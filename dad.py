"""
Created on Mon Feb  1 13:54:12 2021
@author: Fábio J. S. Lopes

Download Aeronet Data - DAD

Python script to automatically download data from AERONET Web Data Service Help platform. 
Dataset includes AERONET Aerosol Optical Depth - Version 3 - level1.5 or level2.0 data 
(direct sun algorithm) and AERONET inversion data

More information: Check AERONET Version 3 Web Service Help
https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_v3

"""

import wget
import os
import pandas as pd

'''Creating the folder for raw data download from AERONET web data service'''
rootdir = os.getcwd()
outputdir = '01-rawdata'
dircontents = os.sep.join([rootdir, outputdir])
if not os.path.exists(dircontents):
        os.makedirs(dircontents)

'''Reading the input data to download AERONET data from web data service'''
inputdatadir = '01-input_dir'
inputfilename = 'input1'
inputdir = os.sep.join([rootdir, inputdatadir])
filenames = [name for name in os.listdir(inputdir) if name.startswith(inputfilename)]
nfiles=len(filenames)

print(filenames)
filenameout = []

for x in range(0, len(filenames)):
        newfile = os.sep.join([inputdir, filenames[x]])
        filedata = pd.read_csv(newfile)
        for i in range(0,len(filedata)):

                if filedata['download'][i] == 'on':
                        
                        if filedata['month_initial'][i] < 10: 
                                filemonthin = '0'+ str(filedata['month_initial'][i])
                        else:
                                filemonthin = str(filedata['month_initial'][i])
                        if filedata['month_final'][i] < 10:
                                filemonthfinal = '0'+ str(filedata['month_final'][i])
                        else:
                                filemonthfinal = str(filedata['month_final'][i])
                        if filedata['day_initial'][i] < 10: 
                                filedayin = '0'+ str(filedata['day_initial'][i])
                        else:
                                filedayin = str(filedata['day_initial'][i])
                        if filedata['day_final'][i] < 10:
                                filedayfinal = '0'+ str(filedata['day_final'][i])
                        else:
                                filedayfinal = str(filedata['day_final'][i])
                        if filedata['level'][i] == 10:
                                filelevel = '10'
                        elif filedata['level'][i] == 15:
                                filelevel = '15'
                        else:
                                filelevel = '20'  
                        filenameout = str(filedata['year_initial'][i])+filemonthin+filedayin+'_'+\
                                      str(filedata['year_final'][i])+filemonthfinal+filedayfinal+'_'+\
                                      filedata['site'][i]+'_level'+filelevel+'.'+filedata['products'][i]
                        
                        url = 'https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_inv_v3?site='+filedata['site'][i]+\
                              '&year='+str(filedata['year_initial'][i])+'&month='+filemonthin+'&day='+filedayin+\
                              '&year2='+str(filedata['year_final'][i])+'&month2='+filemonthfinal+'&day2='+filedayfinal+\
                              '&product='+filedata['products'][i].upper()+'&AVG='+str(filedata['avg'][i])+'&ALM'+filelevel+'=1&if_no_html=1'
                        
                        if filedata['products'][i] == 'pfncoarse':
                                url = 'https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_inv_v3?site='+filedata['site'][i]+\
                                      '&year='+str(filedata['year_initial'][i])+'&month='+filemonthin+'&day='+filedayin+\
                                      '&year2='+str(filedata['year_final'][i])+'&month2='+filemonthfinal+'&day2='+filedayfinal+\
                                      '&product=PFN&AVG='+str(filedata['avg'][i])+'&ALM'+filelevel+'=1&if_no_html=1&pfn_type=1'

                        if filedata['products'][i] == 'pfnfine':                                
                                url = 'https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_inv_v3?site='+filedata['site'][i]+\
                                      '&year='+str(filedata['year_initial'][i])+'&month='+filemonthin+'&day='+filedayin+\
                                      '&year2='+str(filedata['year_final'][i])+'&month2='+filemonthfinal+'&day2='+filedayfinal+\
                                      '&product=PFN&AVG='+str(filedata['avg'][i])+'&ALM'+filelevel+'=1&if_no_html=1&pfn_type=2'

                        if filedata['products'][i] == 'directsun':
                                url = 'https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_v3?site='+filedata['site'][i]+\
                                        '&year='+str(filedata['year_initial'][i])+'&month='+filemonthin+'&day='+filedayin+\
                                        '&year2='+str(filedata['year_final'][i])+'&month2='+filemonthfinal+'&day2='+filedayfinal+\
                                        '&AOD'+filelevel+'=1&AVG='+str(filedata['avg'][i])
                                                
                        filename = wget.download(url, out=os.sep.join([dircontents, filenameout]))
