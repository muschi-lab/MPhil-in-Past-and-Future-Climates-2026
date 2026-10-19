"""Small helper functions shared by the 02_methods notebooks.

Everything here is also written out step by step in the main notebook, so you can
see what each helper does. The group-task notebook imports them to save time.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import xarray as xr
import pyleoclim as pyleo
from pylipd.lipd import LiPD

# Data live two folders up: practicals/02_methods/ -> repo root -> data/02_methods/
DATA = Path(__file__).resolve().parent.parent.parent / "data" / "02_methods"
CORAL_DIR = DATA / "coralhydro2k"
SST_FILE = DATA / "hadisst1_djf" / "HadISST1_DJF_40S40N.nc"
SKT_FILE = DATA / "20cr_skt" / "20CR_anom_40S40N.nc"


def load_coral_table(path=CORAL_DIR):
    """Read all LiPD files in a folder and return one row per time series."""
    lipd = LiPD()
    lipd.load_from_dir(str(path))
    _, df = lipd.get_timeseries(lipd.get_all_dataset_names(), to_dataframe=True)
    # Sort so that row order is the same on every computer (file order differs between systems).
    return df.sort_values(["dataSetName", "paleoData_TSid"]).reset_index(drop=True)


def select_long_d18o(df, first=1890, last=1980, max_step=0.25):
    """d18O records that start before `first`, end after `last` and have a
    median spacing between samples of at most `max_step` years."""
    out = df[(df["paleoData_variableName"] == "d18O")
             & (df["minYear"] < first) & (df["maxYear"] > last)]
    # Some series called 'd18O' are reconstructed SEAWATER d18O (TSid ends in '_sw'),
    # not measured coral d18O. They are a different variable, so drop them.
    out = out[~out["paleoData_TSid"].str.contains("_sw")]
    # nanmedian ignores missing time stamps; the tiny tolerance avoids float round-off
    # (a record with spacing 0.2500840 is a quarterly record).
    step = out["year"].apply(lambda x: np.nanmedian(np.abs(np.diff(np.asarray(x, float)))))
    return out[step <= max_step + 1e-3]


def to_geoseries(row):
    """Turn one table row into a pyleoclim GeoSeries."""
    return pyleo.GeoSeries(
        time=row["year"], value=row["paleoData_values"],
        time_name="Year", value_name="d18O",
        time_unit=row["yearUnits"], value_unit=row["paleoData_units"],
        lat=row["geo_meanLat"], lon=row["geo_meanLon"],
        elevation=row["geo_meanElev"], archiveType=row["archiveType"],
        label=row["dataSetName"], auto_time_params=False, verbose=False)


def djf_mean(g, min_obs=1):
    """Winter (Dec-Jan-Feb) mean of a GeoSeries.

    December belongs to the NEXT year, so 'DJF 1998' = Dec 1997 + Jan 1998 + Feb 1998.
    This is the same convention as the HadISST file. Years with fewer than
    `min_obs` samples in the winter window are dropped.
    """
    t = np.asarray(g.time, float)
    x = np.asarray(g.value, float)
    year = np.floor(t)
    month = np.floor((t - year) * 12) + 1
    keep = np.isin(month, [12, 1, 2]) & np.isfinite(x)
    season_year = year[keep] + (month[keep] == 12)
    s = pd.Series(x[keep]).groupby(season_year).agg(["mean", "count"])
    s = s[s["count"] >= min_obs]
    return pyleo.GeoSeries(
        time=s.index.values, value=s["mean"].values, time_name="Year",
        value_name="d18O", time_unit="year CE", lat=g.lat, lon=g.lon,
        label=g.label, auto_time_params=False, verbose=False)


def prepare_corals(df_long, start=1900, stop=1980):  # integer years start..stop inclusive (81 points)
    """Detrend -> DJF mean -> common 1900-1980 annual axis -> standardise."""
    ms = pyleo.MultipleGeoSeries([to_geoseries(r) for _, r in df_long.iterrows()],
                                 time_unit="year CE")
    ms = ms.detrend(method="emd")
    ms = pyleo.MultipleGeoSeries([djf_mean(g) for g in ms.series_list], time_unit="year CE")
    ms = ms.common_time(method="interp", start=start, stop=stop, step=1)
    return ms.standardize()


def load_sst(path=SST_FILE, start=1900, stop=1980):
    """DJF sea-surface temperature (deg C), 40S-40N, all longitudes (0-360), with a 'year' coordinate."""
    sst = xr.open_dataset(path)["sst"].load()
    sst = sst.sel(time=slice(str(start), str(stop)))
    return sst.assign_coords(year=("time", sst.time.dt.year.values))
