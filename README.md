# Download Aeronet Data - DAD

This repository provides a python script to automatically download data from AERONET Web Data Service Help platform.

The Dataset includes AERONET Aerosol Optical Depth - Version 3 - level1.5 or level2.0 data (direct sun algorithm) and AERONET inversion data.

## Input file

The input file is contained in folder [01-input_dir](https://github.com/fabioslopes/download_aeronet_data/tree/master/01-input_dir). It is a csv file with all necessary information for download products from AERONET database.
The input file contain 11 columns with the following fields: 
1. year_initial: Initial year for data retrieval
2. month_initial: Initial month for data retrieval
3. day_initial: Initial day for data retrieval
4. year_final: End year for data retrieval
5. month_final: End month for data retrieval
6. day_final: end day for data retrieval
7. site: The station name to be downloaded, ex: Sao_Paulo is the name of AERONET sattion setup in São Paulo city in Brazil. The AERONET database site list can be checked in the file [aeronet_locations_v3](https://github.com/fabioslopes/download_aeronet_data/blob/master/aeronet_locations_v3.csv)
8. level - is the level of AERONET data, ex: 20 for level2.0 data or 15 for level1.5 data
9. avg - is the data format average - fo all points use AVG=10 and for daily average use AVG=20
10. products: is the data products to be downloaded 
   - siz - Size distribution
   - rin	- Refractive indicies (real and imaginary)
   - cad -	Coincident AOT data with almucantar retrieval
   - vol	- Volume concentration, volume mean radius, effective radius and standard deviation
   - tab -	AOD absorption
   - aod - AOD extinction
   - ssa	- Single scattering albedo
   - asy -	Asymmetry factor
   - frc -	Radiative Forcing
   - lid - Lidar and Depolarization Ratios
   - flx - Spectral flux
   - pfn - Phase function
   - pfncoarse - coarse mode phase functions
   - pfnfine - fine mode phase functions
   - directsun - Aerosol Optical Depth from AERONET direct sun measurements
11. download - use "on" to turn it on download or "off" to turn it off the download

Once you have adjusted the input.csv file, set up the output directory name on dad.py file (01-rawdata is the default) and run it to start the AERONET data download. 

More information about data, products and how to download, please, check the [AERONET Web Data Service Help](https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_v3)
