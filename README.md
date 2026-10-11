# MPhil in Past and Future Climates 2026

![MPhil in Past and Future Climates](assets/pfc_logo.jpg)

Python scripts, guides and datasets for the numerical practicals of the MPhil in Past and Future Climates (2026-27), University of Cambridge.

## Get the materials

**Option A: download a ZIP (no Git needed).** Click the green **Code** button at the top of this page, then **Download ZIP**, and unzip it somewhere you can find it, for example `Documents/PastFutureClimates`.

**Option B: clone with Git.** In a terminal:

```bash
git clone https://github.com/muschi-lab/MPhil-in-Past-and-Future-Climates-2026.git
cd MPhil-in-Past-and-Future-Climates-2026
git pull   # run this later to pick up new practicals
```

## Set up Python

You need Python 3.10 or later. The simplest route is [Miniforge](https://github.com/conda-forge/miniforge), which includes `conda`.

```bash
conda env create -f environment.yml
conda activate pfc
jupyter lab
```

If you prefer `pip`, create a virtual environment and run `pip install -r requirements.txt`.

## What is in this repository

| Folder or file | Contents |
| --- | --- |
| `practicals/` | One folder per numerical practical, each with its own README, scripts and notebooks |
| `data/` | Datasets used in the practicals (see `data/README.md`) |
| `environment.yml` | Conda environment used for all practicals |
| `requirements.txt` | The same packages for `pip` users |

### Large files

Larger datasets are not stored in this repository. They are in a shared Google Drive folder:

**[Large data files (Google Drive)](https://drive.google.com/drive/folders/1twf3I61XYz9OJd5w4TMSsBQ7c2f5sMUO?usp=sharing)**

Group-exercise datasets are in the "Group-exercise datasets" subfolder of that folder. Download the file you need and place it in the matching `data/<dataset-name>/` folder. Each dataset's `README.md` says where it belongs. See [`data/README.md`](data/README.md) for the full list.

## How to use a practical

1. Open the practical's folder in `practicals/` and read its `README.md` first.
2. Run the scripts or notebooks from inside that folder, so relative paths to `../../data` work.
3. Work on a copy of any script you want to change, so `git pull` does not clash with your edits.

## Questions

Ask in the practical session or contact the course director. For problems with the code itself, open an Issue on this repository using the **Issues** tab and say which practical and script it concerns, paste the full error message, and say which operating system you use.
