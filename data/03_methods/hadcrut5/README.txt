HadCRUT5 annual global temperature anomaly, 1850-2025

File:      hadcrut5.csv (186 rows, comma-separated, header row). Copy of data/01_methods/hadcrut5/hadcrut5.csv.
Columns:   year, global_anomaly (degrees C), nh_anomaly, sh_anomaly,
           global_lower_ci, global_upper_ci (bounds of the 95% uncertainty range of the global anomaly, degrees C)
Baseline:  anomalies relative to 1961-1990, the standard HadCRUT5 baseline (the 1961-1990 mean of the global
           anomaly in this file is 0.008 degrees C, consistent with that baseline).
Licence:   to be confirmed against the Met Office terms (as for data/01_methods/hadcrut5).
Used in:   practicals/03_methods (group tasks, Task 1): the measurement error of each year is taken as
           half the width of the uncertainty range, (upper - lower) / 2, treated as a 2-sigma range -> 1 sigma = (upper - lower) / 4.
Source:    Morice, C.P. et al. (2021), J. Geophys. Res. Atmos. 126, e2019JD032361. https://doi.org/10.1029/2019JD032361
           https://www.metoffice.gov.uk/hadobs/hadcrut5/
