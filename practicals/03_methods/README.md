# 03 Methods three: introduction to Bayesian modelling

Build a Bayesian statistical model from scratch with nothing but NumPy and SciPy: Bayes' theorem on a coin, a conjugate prior, and then a hand-written Metropolis MCMC sampler that fixes a physically impossible regression on real glacier-melt data. One notebook to read before class (its first cell gives the aims and learning outcomes), and group tasks for the session.

## Guides

| File | Contents |
| --- | --- |
| [`Setup_Guide_Python_and_VS_Code.pdf`](../02_methods/Setup_Guide_Python_and_VS_Code.pdf) | (In the Methods 02 folder.) Update the Python environment, install VS Code, choose the right kernel, test the installation; troubleshooting |
| [`Using_Claude_Code_as_a_Tutor.pdf`](../02_methods/Using_Claude_Code_as_a_Tutor.pdf) | (In the Methods 02 folder.) Optional: sign in to Claude Code in VS Code and use it as a tutor beside the notebook |

If your environment worked for Methods 02, it works here: this session adds **no new packages** (numpy, scipy, pandas and matplotlib only).

## Notebooks and files

| File | Contents |
| --- | --- |
| [`Methods_03_Bayesian_Modelling.ipynb`](Methods_03_Bayesian_Modelling.ipynb) | The main notebook, to read and run before the session. Part 1: Bayes' theorem and a conjugate prior on a coin. Parts 2-4: glacier melt vs temperature, a frequentist fit that breaks the physics, and a hand-written Metropolis sampler that fixes it |
| [`Group_tasks.ipynb`](Group_tasks.ipynb) | Group tasks for the session (do not start them beforehand): global warming rate (HadCRUT5), the timing of the Holocene onset (NGRIP), and an Arctic sea-ice forecast with a prior from climate models |
| [`check_setup.py`](check_setup.py) | Checks that your Python installation and the data are ready |
| [`bayes_helpers.py`](bayes_helpers.py) | Short helper functions used by the group tasks (the same sampler and models as the main notebook, in fewer lines). Keep it in this folder |
| [`figures/`](figures/) | Source images used by the main notebook (keep the folder next to it) |

## Data needed

All data are in the repository, in [`data/03_methods/`](../../data/03_methods/). Nothing to download.

| Folder | What it is |
| --- | --- |
| `glacier_melt/` | Daily melt and air temperature, Spitsbergen, summer 1999 (main notebook) |
| `hadcrut5/` | Annual global temperature anomaly 1850-2025 with uncertainties (Task 1) |
| `ngrip/` | NGRIP ice-core d18O, 20-year means, GICC05 timescale (Task 2) |
| `seaice/` | September Arctic sea-ice area 1901-2024 (Task 3) |

Each folder has a short `README.txt` with source, citation and variable descriptions.

## How to run

Before the session (about an hour):

1. Get the latest files: `git pull` in your copy of the repository, or download the ZIP again.
2. Activate the environment you used for Methods 02 (`conda activate pfc`). No update needed this time.
3. Test the installation:

       cd practicals/03_methods
       python check_setup.py

   The last line must say `ALL OK`.
4. Open the repository folder in VS Code, open the main notebook, choose the `pfc` kernel and run it from top to bottom. Read the text as you go, answer the two *Your turn* boxes, and write down two questions for class. Work on a copy of the notebook, not the original.

Open the notebooks from inside `practicals/03_methods/`: the data paths are relative to that folder. If something goes wrong, see the troubleshooting table in the setup guide, or post the full error message in the course channel and say which operating system you use.

## What to submit

Nothing. Bring your questions and your laptop with the environment working.
