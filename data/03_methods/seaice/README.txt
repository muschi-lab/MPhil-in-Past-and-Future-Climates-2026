September Northern Hemisphere sea-ice area, 1901-2024

File:      sia_series_1901_2024.csv (124 rows, comma-separated, header row)
Columns:   year        calendar year
           sia_sep_nh  September Arctic sea-ice AREA, million km2  (used in Task 3)
           sia_mar_nh, sia_sep_sh, sia_feb_sh   other months/hemispheres (not used)
           tau_sia     ASSUMED 1-sigma measurement error, million km2: 0.50 (1901-1949),
                       0.25 (1950-1978), 0.10 (1979-2024). These values are a teaching assumption,
                       not a published uncertainty product. Say so in any analysis.
           source      IAPICE1 (1901-2019) or HadISST-adjusted (2020-2024)
Caveat:    the series is spliced at 2019/2020 (IAPICE1 reconstruction, then bias-adjusted HadISST1.1).
           Any change detected at 2019/2020 is likely the join, not climate.
Sources:   Semenov, V.A. et al. (2024), Adv. Atmos. Sci. 41, 1483. https://doi.org/10.1007/s00376-024-3320-x
           Rayner, N.A. et al. (2003), J. Geophys. Res. 108, 4407. https://doi.org/10.1029/2002JD002670
Used in:   practicals/03_methods (group tasks, Task 3).
