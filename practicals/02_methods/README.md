# 02 Methods two: computational techniques for paleoclimate research

Open proxy data in the LiPD format, then use PCA and EOF analysis to ask whether tropical coral records capture El Niño–Southern Oscillation (ENSO), and take a short look at their power spectra. One notebook to read before class (its first cell gives the aims and learning outcomes), and group tasks for the session.

## Guides

| File | Contents |
| --- | --- |
| [`Setup_Guide_Python_and_VS_Code.pdf`](Setup_Guide_Python_and_VS_Code.pdf) | Update the Python environment, install VS Code, choose the right kernel, test the installation; troubleshooting |
| [`Using_Claude_Code_as_a_Tutor.pdf`](Using_Claude_Code_as_a_Tutor.pdf) | Optional: sign in to Claude Code in VS Code and use it as a tutor beside the notebook, including how to adapt code safely |

Start with the setup guide. Use the second guide if you want Claude as a tutor while you work.

## Notebooks and files

| File | Contents |
| --- | --- |
| [`Methods_02_Paleoclimate_Computational_Techniques.ipynb`](Methods_02_Paleoclimate_Computational_Techniques.ipynb) | The main notebook, to read and run before the session. Part 1: open and query LiPD files, draw a map. Part 2: PCA on corals, EOF on sea surface temperature, compare the two, and a short look at their power spectra |
| [`Group_tasks.ipynb`](Group_tasks.ipynb) | Group tasks for the session (do not start them beforehand): Tasks 1–5, and a bonus Task 6 for groups that finish early |
| [`Spectral_analysis_primer.ipynb`](Spectral_analysis_primer.ipynb) | Optional short primer on spectral analysis (sine waves, red noise, windows), with a synthetic series; no data needed |
| [`check_setup.py`](check_setup.py) | Checks that your Python installation and the data are ready |
| [`paleo_helpers.py`](paleo_helpers.py) | Short helper functions used by the group tasks. Keep it in this folder |
| [`figures/`](figures/) | Source images (already embedded in the notebook; you do not need to open them) |

## Data needed

All data are in the repository, in [`data/02_methods/`](../../data/02_methods/). Nothing to download from Google Drive.

| Folder | What it is |
| --- | --- |
| `coralhydro2k/` | 179 coral records (δ18O and Sr/Ca), LiPD format |
| `hadisst1_djf/` | Winter sea surface temperature 1900–2000, 40°S–40°N |
| `20cr_skt/` | Surface temperature anomalies 1836–2015 (July–June means), 40°S–40°N (group tasks only) |

Each folder has a short `README.txt` with source, citation and variable descriptions.

## How to run

Before the session (about an hour; the setup guide has every step in detail):

1. Get the latest files: `git pull` in your copy of the repository, or download the ZIP again.
2. Update your environment from the repository root (this adds pyleoclim, pylipd and xeofs), then activate it:

       conda env update -f environment.yml
       conda activate pfc

   If the update reports conflicts, make a separate environment instead: `conda env create -f environment.yml -n pfc_methods2`, then `conda activate pfc_methods2`.
3. Test the installation (needs internet the first time):

       cd practicals/02_methods
       python check_setup.py

   The last line must say `ALL OK`.
4. Open the repository folder in VS Code, trust it, open the main notebook, choose the `pfc` kernel and run it from top to bottom. Read the text as you go and write down two questions for class. Work on a copy of the notebook, not the original.

Open the notebooks from inside `practicals/02_methods/`: the data paths are relative to that folder. If something goes wrong, see the troubleshooting table in the setup guide, or post the full error message in the course channel and say which operating system you use.

## What to submit

Nothing. Bring your questions and your laptop with the environment working.
