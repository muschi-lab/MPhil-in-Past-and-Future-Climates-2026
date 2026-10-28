"""Check that the Python environment and the data are ready for Methods 03.

Run from inside practicals/03_methods:  python check_setup.py
The last line must say ALL OK.
"""
import sys
from pathlib import Path

ok = True

def check(label, fn):
    global ok
    try:
        fn()
        print(f"  OK   {label}")
    except Exception as e:
        ok = False
        print(f"  FAIL {label}: {e}")

print("1. Python packages")
check("numpy", lambda: __import__("numpy"))
check("scipy", lambda: __import__("scipy.stats"))
check("pandas", lambda: __import__("pandas"))
check("matplotlib", lambda: __import__("matplotlib.pyplot"))

print("2. Helper file")
check("bayes_helpers.py imports", lambda: __import__("bayes_helpers"))

print("3. Data files")
def data_dir():
    here = Path(__file__).parent
    d = next((p for p in (here / "../../data/03_methods", here / "../data") if (p / "ngrip").is_dir()), None)
    if d is None:
        raise FileNotFoundError("data folder not found: run from practicals/03_methods (see README)")
    return d

def check_file(sub):
    f = data_dir() / sub
    if not f.exists():
        raise FileNotFoundError(f)

check("glacier melt (Glac_Melt.csv)", lambda: check_file("glacier_melt/Glac_Melt.csv"))
check("HadCRUT5 (hadcrut5.csv)", lambda: check_file("hadcrut5/hadcrut5.csv"))
check("NGRIP (ngrip_d18o_20yr.csv)", lambda: check_file("ngrip/ngrip_d18o_20yr.csv"))
check("sea ice (sia_series_1901_2024.csv)", lambda: check_file("seaice/sia_series_1901_2024.csv"))

print("4. A tiny MCMC run")
def tiny_mcmc():
    import numpy as np
    import bayes_helpers as bh
    rng = np.random.default_rng(0)
    x = np.arange(50.0)
    y = 1.0 + 0.2 * (x - x.mean()) / 10 + rng.normal(0, 0.1, 50)
    logp, info = bh.trend_model(x, y)
    samples, acc = bh.run_mcmc(logp, [1.0, 0.0, 0.5], [0.03, 0.02, 0.02], iterations=4000, burnin=1000)
    assert 0.1 < acc < 0.9, f"odd acceptance rate {acc:.0%}"
    assert abs(samples[:, 1].mean() - 0.2) < 0.1, "slope estimate off"

check("sampler recovers a known slope", tiny_mcmc)

print()
print("ALL OK" if ok else "PROBLEMS FOUND - see FAIL lines above (and the README).")
sys.exit(0 if ok else 1)
