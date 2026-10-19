"""Check that your computer is ready for the 02_methods practical.

Run it from a terminal with the pfc environment active:

    cd practicals/02_methods
    python check_setup.py

It takes about 10-20 seconds and ends with ALL OK, or tells you what to fix.
"""
import sys
import importlib
import importlib.metadata as md
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parent.parent / "data" / "02_methods"
problems = []


def ok(msg):
    print(f"  [ok]   {msg}")


def bad(msg, fix):
    print(f"  [FAIL] {msg}\n         -> {fix}")
    problems.append(msg)


print("1. Python")
if sys.version_info >= (3, 10):
    ok(f"Python {sys.version.split()[0]}")
else:
    bad(f"Python {sys.version.split()[0]} is too old",
        "activate the environment first: conda activate pfc")

print("2. Packages")
packages = [  # (import name, pip/conda name)
    ("numpy", "numpy"), ("scipy", "scipy"), ("pandas", "pandas"), ("xarray", "xarray"),
    ("netCDF4", "netCDF4"), ("matplotlib", "matplotlib"), ("cartopy", "cartopy"),
    ("sklearn", "scikit-learn"), ("pyleoclim", "pyleoclim"), ("pylipd", "pylipd"),
    ("xeofs", "xeofs"),
]
for imp, dist in packages:
    try:
        importlib.import_module(imp)
        ok(f"{dist} {md.version(dist)}")
    except Exception as err:  # noqa: BLE001
        bad(f"cannot import {imp} ({type(err).__name__}: {str(err)[:80]})",
            "conda env update -f environment.yml   (run from the repository root)")

print("3. Data files")
checks = [
    ("coralhydro2k", DATA / "coralhydro2k", "*.lpd", 179),
    ("HadISST", DATA / "hadisst1_djf", "HadISST1_DJF_40S40N.nc", 1),
    ("20CR", DATA / "20cr_skt", "20CR_anom_40S40N.nc", 1),
]
for name, folder, pattern, expected in checks:
    n = len(list(folder.glob(pattern)))
    if n == expected:
        ok(f"{name}: {n} file(s) found")
    else:
        bad(f"{name}: found {n} file(s), expected {expected} in {folder}",
            "run 'git pull' or download the repository again; keep the folder structure unchanged")

print("4. A tiny end-to-end test (reads one coral file, one NetCDF file, runs a PCA and an EOF, draws a map; needs internet the first time)")
if problems:
    print("  [skipped] fix the problems above first")
else:
    try:
        import numpy as np
        import xarray as xr
        from pylipd.lipd import LiPD
        from sklearn.decomposition import PCA
        import xeofs as xe

        first = sorted((DATA / "coralhydro2k").glob("*.lpd"))[0]
        lipd = LiPD()
        lipd.load([str(first)])
        assert len(lipd.get_all_dataset_names()) == 1
        ok(f"read LiPD file {first.name}")

        sst = xr.open_dataset(DATA / "hadisst1_djf" / "HadISST1_DJF_40S40N.nc")["sst"]
        assert sst.dims == ("time", "lat", "lon")
        ok(f"read HadISST {dict(sst.sizes)}")

        rng = np.random.default_rng(0)
        pca = PCA(n_components=2).fit(rng.normal(size=(50, 6)))
        assert pca.explained_variance_ratio_.shape == (2,)
        ok("sklearn PCA runs")

        small = sst.isel(time=slice(0, 30), lat=slice(20, 40), lon=slice(20, 60)).dropna("lat", how="all")
        small = small.fillna(float(small.mean()))
        model = xe.single.EOF(n_modes=2, center=True)
        model.fit(small, dim="time")
        assert model.scores().sizes["mode"] == 2
        ok("xeofs EOF runs")

        # cartopy downloads coastline files from the internet the first time it draws a map.
        # Do it now, so it does not fail in class.
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import cartopy.crs as ccrs
        import cartopy.feature as cfeature
        fig = plt.figure()
        ax = fig.add_subplot(projection=ccrs.PlateCarree())
        ax.coastlines(resolution="110m")
        ax.add_feature(cfeature.LAND, zorder=0)
        fig.savefig(HERE / ".map_test.png")
        plt.close(fig)
        (HERE / ".map_test.png").unlink()
        ok("cartopy can draw coastlines (the files are now downloaded)")
    except Exception as err:  # noqa: BLE001
        bad(f"end-to-end test failed ({type(err).__name__}: {str(err)[:120]})",
            "copy this whole output and send it to the instructor before the session")

print()
if problems:
    print(f"NOT READY: {len(problems)} problem(s) above. Fix them or send this output to the instructor.")
    sys.exit(1)
print("ALL OK - you are ready for the practical.")
