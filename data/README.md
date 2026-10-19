# Data

Datasets used in the numerical practicals. Each practical's README says which files it needs.

## Adding data (instructors)

- Keep the repository's total data under about 50 MB. GitHub rejects any single file over 100 MB.
- Group datasets by session: one numbered folder per session, matching the practical folder (`data/01_methods/`). Inside it, put each dataset in its own subfolder, for example `data/01_methods/<dataset-name>/`.
- Next to each dataset add a short `README.md` (or `README.txt`) giving the source, citation, licence, variables and units, and the date it was downloaded.
- For larger files, upload them to the shared Google Drive folder below (not to this repository) and list them in the table, marked as "Google Drive". Add a download note to the practical that uses them.

## Large files (Google Drive)

Files too large for GitHub are kept in this shared folder:

**[Large data files (Google Drive)](https://drive.google.com/drive/folders/1twf3I61XYz9OJd5w4TMSsBQ7c2f5sMUO?usp=sharing)**

Group-exercise datasets are in the "Group-exercise datasets" subfolder of that folder. Put each file in the matching `data/<session>/<dataset-name>/` folder on your computer (for example `data/01_methods/hadcrut5/`). Keep the file name unchanged.

## Contents

| Folder or file | Description | Source and licence | Used in | Location |
| --- | --- | --- | --- | --- |
| `01_methods/hadcrut5/` | Annual global, NH and SH temperature anomalies, 1850–2025 (CSV) | Met Office Hadley Centre / CRU, licence to be confirmed | *(not yet assigned)* | GitHub |
| `02_methods/coralhydro2k/` | CoralHydro2k v1.0.1: 179 coral δ18O and Sr/Ca records in LiPD format (Walter et al., 2023) | LiPDverse, https://lipdverse.org/CoralHydro2k/ | `practicals/02_methods` | GitHub |
| `02_methods/hadisst1_djf/` | HadISST1 winter (DJF) sea surface temperature 1900–2000, 40°S–40°N, NetCDF (Rayner et al., 2003) | Met Office Hadley Centre, https://www.metoffice.gov.uk/hadobs/hadisst/ | `practicals/02_methods` | GitHub |
| `02_methods/20cr_skt/` | 20CRv3 July–June surface temperature anomaly 1836–2015, 40°S–40°N, NetCDF (Slivinski et al., 2019) | NOAA PSL, https://psl.noaa.gov/data/20thC_Rean/ | `practicals/02_methods` (group tasks) | GitHub |
| *(session TBC)*`/ersstv5/ersstv5.nc` | NOAA ERSSTv5 sea surface temperature (NetCDF) | NOAA, to be confirmed | *(not yet assigned)* | Google Drive (to be uploaded) |

