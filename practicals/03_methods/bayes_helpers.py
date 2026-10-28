"""Short helper functions for the Methods 03 group tasks.

Everything here repeats, in fewer lines, what the main notebook
(Methods_03_Bayesian_Modelling.ipynb) builds step by step: a Metropolis
sampler, two small models (a straight-line trend and a step change), and
loaders for the three datasets. Keep this file in the same folder as the
group-tasks notebook.
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data folder, relative to this file (repository layout, or a flat layout with data next to practicals)
_HERE = Path(__file__).parent
DATA = next((d for d in (_HERE / "../../data/03_methods", _HERE / "../data")
             if (d / "ngrip").is_dir()), _HERE / "../../data/03_methods")


# ---------------------------------------------------------------- sampler

def run_mcmc(log_posterior, initial, step_sizes, iterations=40_000, burnin=4_000, seed=42):
    """Metropolis sampler, exactly as in the main notebook (Section 6).

    Returns (samples, acceptance_rate). `samples` has one row per kept
    iteration and one column per parameter; the first `burnin` iterations
    are discarded.
    """
    rng = np.random.default_rng(seed)
    current = np.array(initial, dtype=float)
    step_sizes = np.asarray(step_sizes, dtype=float)
    current_logpost = log_posterior(current)
    if not np.isfinite(current_logpost):
        raise ValueError("The starting point has zero posterior probability; "
                         "choose an initial value inside the prior bounds.")
    samples, n_accepted = [], 0
    for i in range(iterations):
        proposed = current + rng.normal(0, step_sizes)
        proposed_logpost = log_posterior(proposed)
        if np.log(rng.random()) < proposed_logpost - current_logpost:
            current, current_logpost = proposed, proposed_logpost
            n_accepted += 1
        if i >= burnin:
            samples.append(current)
    return np.array(samples), n_accepted / iterations


def summarise(samples, names):
    """Posterior mean and 95% credible interval of each parameter, as a table."""
    lo, hi = np.percentile(samples, [2.5, 97.5], axis=0)
    return pd.DataFrame({"posterior mean": samples.mean(axis=0),
                         "2.5%": lo, "97.5%": hi}, index=names).round(3)


def plot_traces(samples, names, acceptance=None):
    """Trace plots ('hairy caterpillars'), one panel per parameter."""
    n = len(names)
    fig, axes = plt.subplots(1, n, figsize=(3.2 * n, 2.6), sharex=True)
    for ax, i in zip(np.atleast_1d(axes), range(n)):
        ax.plot(samples[:, i], lw=0.4, alpha=0.8)
        ax.set_title(names[i], fontsize=11)
        ax.set_xlabel("iteration", fontsize=9)
    title = "MCMC trace plots"
    if acceptance is not None:
        title += f" (acceptance rate {acceptance:.0%})"
    fig.suptitle(title, y=1.04)
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------- models

def trend_model(x, y, tau=None, slope_prior=None, x0=None, scale=10.0):
    """Straight-line model  y = a + b * (x - x0) / scale + noise.

    With scale=10 and x in years, b is a rate PER DECADE. `tau` (optional)
    is the known 1-sigma measurement error of each point: it is added to the
    model's own noise sigma in quadrature. `slope_prior` (optional) is a
    (mean, sd) Normal prior on b; without it the prior on b is flat.

    Returns (log_posterior, info) where info holds x0, the parameter names
    ['a', 'b', 'sigma'] and a predict(params, x_new) function.
    """
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    x0 = float(np.mean(x)) if x0 is None else float(x0)
    t = (x - x0) / scale
    tau2 = 0.0 if tau is None else np.asarray(tau, float) ** 2
    sigma_max = 10 * np.std(y)

    def log_posterior(params):
        a, b, sigma = params
        if not (0 < sigma <= sigma_max):
            return -np.inf
        lp = 0.0
        if slope_prior is not None:
            m, s = slope_prior
            lp += -0.5 * ((b - m) / s) ** 2
        var = sigma**2 + tau2
        residuals = y - (a + b * t)
        return lp - 0.5 * np.sum(residuals**2 / var + np.log(2 * np.pi * var))

    def predict(params, x_new):
        a, b, _ = params[:3]
        return a + b * (np.asarray(x_new, float) - x0) / scale

    info = dict(x0=x0, scale=scale, names=["a", "b", "sigma"], predict=predict)
    return log_posterior, info


def step_model(t, y, window):
    """Step-change model: y = mu_before for t > T, mu_after for t <= T (t = age).

    For ice-core ages (years b2k) SMALLER age = LATER in time, so mu_after is
    the level on the young side of T. `window` = (t_min, t_max) is a flat
    prior on T. Returns (log_posterior, info) with parameter names
    ['mu_before', 'mu_after', 'T', 'sigma'].
    """
    t = np.asarray(t, float)
    y = np.asarray(y, float)
    t_min, t_max = float(min(window)), float(max(window))
    sigma_max = 10 * np.std(y)

    def log_posterior(params):
        mu_b, mu_a, T, sigma = params
        if not (t_min <= T <= t_max) or not (0 < sigma <= sigma_max):
            return -np.inf
        pred = np.where(t > T, mu_b, mu_a)
        residuals = y - pred
        return -0.5 * np.sum((residuals / sigma) ** 2 + np.log(2 * np.pi * sigma**2))

    info = dict(names=["mu_before", "mu_after", "T", "sigma"])
    return log_posterior, info


# ---------------------------------------------------------------- loaders

def load_hadcrut5():
    """HadCRUT5 annual global anomalies with a 1-sigma measurement error column.

    The file gives a 95% uncertainty range; we take 1 sigma = (upper - lower) / 4.
    """
    df = pd.read_csv(DATA / "hadcrut5" / "hadcrut5.csv")
    df["tau"] = (df["global_upper_ci"] - df["global_lower_ci"]) / 4
    return df


def load_ngrip():
    """NGRIP d18O 20-year means on the GICC05 timescale (age in years b2k)."""
    return pd.read_csv(DATA / "ngrip" / "ngrip_d18o_20yr.csv")


def load_seaice():
    """September Arctic sea-ice area, 1901-2024, with the assumed tau_sia error."""
    return pd.read_csv(DATA / "seaice" / "sia_series_1901_2024.csv")


# GICC05 event ages used in Task 2 (Rasmussen et al., 2014): age b2k, maximum
# counting error (MCE, conventionally treated as about 2 sigma, years), and the
# search window we suggest (years b2k).
EVENTS = {
    "Holocene":            dict(age=11703, unc=99,  window=(11000, 12600)),
    "Younger Dryas onset": dict(age=12896, unc=138, window=(12400, 13400)),
    "Bolling onset":       dict(age=14692, unc=186, window=(14200, 15200)),
}
