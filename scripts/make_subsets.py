"""Record of how the data in data/02_methods were prepared (instructor use; students do not need to run this).

Crops the global HadISST1 DJF and 20CR files to 40S-40N, all longitudes.
Run from the repository root:  python scripts/make_subsets.py <src_dir> <dst_dir>
  src_dir: folder holding the original global files HadISST1_DJF.nc and 20CR_anom.nc (not in this repository)
  dst_dir: data/02_methods
Domain: 40S-40N, 0-360E. This keeps every CoralHydro2k record used in the practical (Red Sea to Atlantic)
inside the grid. Longitudes are handled in 0-360.
"""
import sys
from pathlib import Path
import xarray as xr

LAT = (-40, 40)
LON = (0, 360)

def crop(ds):
    ds = ds.assign_coords(lon=(ds.lon % 360)).sortby("lon").sortby("lat")
    return ds.sel(lat=slice(*LAT), lon=slice(*LON))

def main(src, dst):
    src, dst = Path(src), Path(dst)
    jobs = [
        ("HadISST1_DJF.nc", dst / "hadisst1_djf" / "HadISST1_DJF_40S40N.nc"),
        ("20CR_anom.nc",    dst / "20cr_skt"     / "20CR_anom_40S40N.nc"),
    ]
    for name, out in jobs:
        ds = xr.open_dataset(src / name, decode_times=False)
        sub = crop(ds)
        # drop attributes that carry personal account identifiers (the Climate Explorer URL contains one)
        sub.attrs = {k: v for k, v in sub.attrs.items() if "EMAIL=" not in str(v)}
        sub.attrs["subset_note"] = (f"Cropped to lat {LAT[0]} to {LAT[1]}, lon {LON[0]} to {LON[1]} E "
                                    f"from {name} with scripts/make_subsets.py")
        enc = {v: {"zlib": True, "complevel": 4} for v in sub.data_vars}
        out.parent.mkdir(parents=True, exist_ok=True)
        sub.to_netcdf(out, encoding=enc)
        print(f"{out}: {out.stat().st_size/1e6:.2f} MB, dims {dict(sub.sizes)}")

if __name__ == "__main__":
    main(*sys.argv[1:3])
