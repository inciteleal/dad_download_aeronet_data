"""
Created on Mon Feb  1 13:54:12 2021
@author: Fábio J. S. Lopes

Download Aeronet Data - DAD

Python script to automatically download data from AERONET Web Data Service Help platform. 
Dataset includes AERONET Aerosol Optical Depth - Version 3 - level1.5 or level2.0 data 
(direct sun algorithm) and AERONET inversion data

More information: Check AERONET Version 3 Web Service Help
https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_v3

Last update: November 6, 2025 by hbarbosa
  - prints info to the user
  - removed index for loop on filenames
  - formated comments in the code
  - BUG FIX: removed HTML format when downloading directsun product
  - simpler formating of strings used in filenames
  - BUG FIX: force using ',' as separator in linux as well
  - Feature: data now saved to 01-rawdata/site_name/
  - BUG FIX: Disable default progress bar, since aeronet website does not give file length
"""

import os
import ssl
import wget
import platform
import pandas as pd

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context

# Creating the folder for raw data download from AERONET web data service 
rootdir = os.getcwd()
outputdir = '01-rawdata'
dircontents = os.sep.join([rootdir, outputdir])
if not os.path.exists(dircontents):
        os.makedirs(dircontents)

# Reading the input data to download AERONET data from web data service
print('Locating input files...')
inputdatadir = '01-input_dir'
inputfilename = 'input1'
inputdir = os.sep.join([rootdir, inputdatadir])
filenames = [name for name in os.listdir(inputdir) if name.startswith(inputfilename)]
print('Number of input files to read:', len(filenames))
print('List of input files found:')
print(filenames)

for afile in filenames:
        newfile = os.sep.join([inputdir, afile])
        print('Reading input file:', newfile)

        # bug 6-nov-2025 force using ',' as separator in all operating systems
        filedata = pd.read_csv(newfile, sep=',' )
        print('Number of products requested:', len(filedata))
        
        # loop over each line of the input file
        for i in range(0,len(filedata)):
            
            # download only if the download flag is 'on'
            if filedata['download'][i] == 'on':
                print('Processing product: ' + filedata['products'][i])

                # use f-strings with formatting
                fileyearin = f'{filedata["year_initial"][i]:04d}'
                fileyearfinal = f'{filedata["year_final"][i]:04d}'
                filemonthin = f'{filedata["month_initial"][i]:02d}'
                filemonthfinal = f'{filedata["month_final"][i]:02d}'
                filedayin = f'{filedata["day_initial"][i]:02d}'
                filedayfinal = f'{filedata["day_final"][i]:02d}'
                filelevel = str(filedata["level"][i])

                filenameout = fileyearin+filemonthin+filedayin+'_'+\
                              fileyearfinal+filemonthfinal+filedayfinal+'_'+\
                              filedata['site'][i]+'_level'+filelevel+'.'+filedata['products'][i]
                
                url = 'https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_inv_v3?site='+filedata['site'][i]+\
                      '&year='+fileyearin+'&month='+filemonthin+'&day='+filedayin+\
                      '&year2='+fileyearfinal+'&month2='+filemonthfinal+'&day2='+filedayfinal+\
                      '&product='+filedata['products'][i].upper()+'&AVG='+str(filedata['avg'][i])+'&ALM'+filelevel+'=1&if_no_html=1'
                
                if filedata['products'][i] == 'pfncoarse':
                        url = 'https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_inv_v3?site='+filedata['site'][i]+\
                              '&year='+fileyearin+'&month='+filemonthin+'&day='+filedayin+\
                              '&year2='+fileyearfinal+'&month2='+filemonthfinal+'&day2='+filedayfinal+\
                              '&product=PFN&AVG='+str(filedata['avg'][i])+'&ALM'+filelevel+'=1&if_no_html=1&pfn_type=1'

                if filedata['products'][i] == 'pfnfine':                                
                        url = 'https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_inv_v3?site='+filedata['site'][i]+\
                              '&year='+fileyearin+'&month='+filemonthin+'&day='+filedayin+\
                              '&year2='+fileyearfinal+'&month2='+filemonthfinal+'&day2='+filedayfinal+\
                              '&product=PFN&AVG='+str(filedata['avg'][i])+'&ALM'+filelevel+'=1&if_no_html=1&pfn_type=2'

                #bug 6-nov-2025 missing if_no_html=1 in the directsun url
                if filedata['products'][i] == 'directsun':
                        url = 'https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_v3?site='+filedata['site'][i]+\
                                '&year='+fileyearin+'&month='+filemonthin+'&day='+filedayin+\
                                '&year2='+fileyearfinal+'&month2='+filemonthfinal+'&day2='+filedayfinal+\
                                '&AOD'+filelevel+'=1&AVG='+str(filedata['avg'][i])+'&ALM'+filelevel+'=1&if_no_html=1'

                # create a sub-folder for this aeronet site
                sitedir = f'{filedata['site'][i]}'
                dircontents = os.sep.join([rootdir, outputdir, sitedir])
                if not os.path.exists(dircontents):
                       os.makedirs(dircontents)
                fullpathfilenameout = os.sep.join([dircontents, filenameout])

                if os.path.exists(fullpathfilenameout):
                    print('    => File already exists. Skipping...')
                    continue
                else:
                    print('    => Downloading:', filenameout)

                # Disable default progress bar, since aeronet website does not give file length
                filename = wget.download(url, out=fullpathfilenameout, bar=None)

# -- end of script --
