HadISST1 winter (DJF) sea surface temperature, 40S-40N

File:      HadISST1_DJF_40S40N.nc (NetCDF, 6 MB)
Variable:  sst, degrees C. Dimensions time (101), lat (80), lon (360), 1 degree grid.
Domain:    39.5S to 39.5N, 0.5E to 359.5E (0-360 convention).
Time:      one value per year, 1900-2000. DJF year = year of January and February
           (DJF 1998 = Dec 1997 + Jan + Feb 1998).
Mask:      cells with gaps during 1900-1980 are NaN at all times (about 25% of the grid).
Used in:   practicals/02_methods (Part 2 and group tasks).

Source:    Met Office Hadley Centre, https://www.metoffice.gov.uk/hadobs/hadisst/
Citation:  Rayner, N. A., et al. (2003). J. Geophys. Res., 108(D14), 4407.
           https://doi.org/10.1029/2002JD002670
Processing: DJF seasonal mean and gap mask applied to the global file by the instructor;
           then cropped to 40S-40N with scripts/make_subsets.py.
