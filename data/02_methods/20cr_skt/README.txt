20th Century Reanalysis v3: surface temperature anomaly, 40S-40N

File:      20CR_anom_40S40N.nc (NetCDF, 14 MB)
Variable:  skt, anomaly in K (same size as degrees C) relative to 1991-2020. Over the ocean
           this is the prescribed sea surface temperature (SODAsi.3); over land, model skin temperature.
Domain:    40S-40N, 0-359E, 1 degree grid. Dimensions time (180), lat (81), lon (360).
Time:      12-month means of JULY to JUNE, stored as "years since 1836-01-01". The time
           value t covers July (1836+t) to June (1837+t), so it contains the winter (DJF)
           of year 1837+t. Label it with that year: year = 1837 + t. Open with decode_times=False.
Used in:   practicals/02_methods (group tasks only).

Source:    NOAA PSL via KNMI Climate Explorer; https://psl.noaa.gov/data/20thC_Rean/
Citation:  Slivinski, L. C., et al. (2019). Q. J. R. Meteorol. Soc., 145, 2876-2908.
           https://doi.org/10.1002/qj.3598
Processing: cropped from the global file with scripts/make_subsets.py.
