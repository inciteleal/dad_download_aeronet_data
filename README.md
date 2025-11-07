# Download Aeronet Data - DAD

This repository provides a python script to automatically download data from AERONET Web Data Service Help platform.

The Dataset includes AERONET Aerosol Optical Depth - Version 3 - level1.5 or level2.0 data (direct sun algorithm) and AERONET inversion data.

## Requirements

To use this script, you need pandas and python-wget libraries. You can install these libraries the usual way:

```
pip install pandas wget 
```

In the case of Anaconda, you need to install the python-wget package from conda-forge, because the wget package will actually give you an executable on the command line, not the python module. Hence: 

```
conda install -c conda-forge python-wget
conda install pandas
```

## Downloading AERONET data

After downloading this package and installing the required libraries,
you need to run the dad.py script to download AERONET data.  You can
do that on the command line:

```
python3 dad.py
```

Or in an interactive sesion, for instance using ipython:

```
In [1]: run dad.py
```

The script will read all the input files in the 00-input_dir/ folder,
and download all the AERONET products listed in each file.  The files,
exactly as downloaded from the AERONET website, are saved in the
00-rawdata/ folder.

You can set up one input file for each station that you are
interested, and run the script only once. See the next section to
understand how to modify the input file for your needs. The example
distributed in this repository is for the station in Sao Paulo,
Brazil.


## Input file

The input file is contained in folder
[00-input_dir](https://github.com/inciteleal/dad_download_aeronet_data/tree/master/00-input_dir)
. It is a csv file with all necessary information for downloading
products from AERONET database.  The input file contain 11 columns
with the following fields:

1. year_initial: Initial year for data retrieval
2. month_initial: Initial month for data retrieval
3. day_initial: Initial day for data retrieval
4. year_final: End year for data retrieval
5. month_final: End month for data retrieval
6. day_final: end day for data retrieval
7. site: The station name to be downloaded (see next section)
8. level - is the level of AERONET data, ex: 20 for level2.0 data or 15 for level1.5 data
9. avg - is the data format average - fo all points use AVG=10 and for daily average use AVG=20
10. products: is the data products to be downloaded 
   - siz - Size distribution
   - rin - Refractive indicies (real and imaginary)
   - cad -	Coincident AOT data with almucantar retrieval
   - vol - Volume concentration, volume mean radius, effective radius and standard deviation
   - tab -	AOD absorption
   - aod - AOD extinction
   - ssa - Single scattering albedo
   - asy -	Asymmetry factor
   - frc -	Radiative Forcing
   - lid - Lidar and Depolarization Ratios
   - flx - Spectral flux
   - pfn - Phase function
   - pfncoarse - coarse mode phase functions
   - pfnfine - fine mode phase functions
   - directsun - Aerosol Optical Depth from AERONET direct sun measurements
11. download - use "on" to turn it on download or "off" to turn it off the download

Once you have adjusted the input.csv file, set up the output directory
name on dad.py file (01-rawdata is the default) and run it to start
the AERONET data download.

More information about data, products and how to download, please,
check the [AERONET Web Data Service
Help](https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_v3)

## AERONET site names

The sample input file was prepared for downloading data from the
AERONET station in Sao Paulo, Brazil. You can find this file here: 
[input1_sao_paulo.csv](https://github.com/inciteleal/dad_download_aeronet_data/blob/master/00-input_dir/input1_sao_paulo.csv),

Important points:

1. The AERONET Web Data Service is **case sensitive**, which means you
need to use "Sao_Paulo" and not "sao_paulo" or "SAO_PAULO". 

2. If you try to download data from a station that does not exist (e.g., wrong name), the
AERONET Web Data Service <ins>will return data for all stations</ins>.  The
download would never finish (too much data)!!!

You should always double-check the site name, which you can find on the AERONET website. We provide a list here, but please understand that this might not be up-do-date: 
[aeronet_locations_v3](https://github.com/inciteleal/dad_download_aeronet_data/blob/master/aeronet_locations_v3.csv)

