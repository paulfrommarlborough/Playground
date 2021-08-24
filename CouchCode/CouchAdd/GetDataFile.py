import sys
from datetime import datetime
from datetime import timedelta
import winreg
import zipfile
import glob, os

#---------------------------------------------------------------------
#  GetDataFile
#     class for input finding CPC file and zipping it.
#  
# inputs:  Date,OS
#---------------------------------------------------------------------

class GetDataFile:
 
    # not type casting the inputs should be string.

    def __init__(self, host, os, date, workdir):        
        self.os = os
        self.host = host
        self.date = date
        self.zip = None
        self.work_dir = workdir
        self.data_dir = None                        
        self.cpclist = []
        self.zip = None
        self.data_filter=None
        self.data_filer1=None
        self.data_prefix = 'ecp'
    
    # GetDataDir:  get directory and setup filters
    #              so we can wildcard find the data files
    #
    def GetDataDir(self):   
        local_os = self.os.lower()
        if local_os == 'windows':
            status = self.GetDataDirFromRegistry(r'SOFTWARE\\PERFCAP\\PM', "DataDirectory")            
            self.data_filter="*.cpc"               # get all files
            self.data_filter1 = "*_1.cpc"          # filter to get first file for the date
            self.data_prefix  = "ecp"
        elif local_os == 'vmware esx':
            status = self.GetDataDirFromRegistry(r'SOFTWARE\\PERFCAP\\ecap_monitor_esx', "DataDirectory")
            self.data_filter="*.cpc*"
            self.data_filter1 = "*.cpc-1"
            self.data_prefix  = "ecpv"
        elif local_os == 'mssql':
            status = self.GetDataDirFromRegistry(r'SOFTWARE\\PERFCAP\\ecap_monitor_mssql', "DataDirectory")
            self.data_filter="*.csv"
            self.data_filter1 = "*.csv"
            self.data_prefix  = "ecpm"
        else:
            print(f'GetDataFiles,  Unknown OS..., {local_os}')
            return 0
        return 1

    # GetDataDirFromRegistry:   fetch the data directory path from the registry
    #

    def GetDataDirFromRegistry(self, REG_PATH, REG_LABEL):
        datadir=None        
        try:
            root = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
            regkey = winreg.OpenKeyEx(root, REG_PATH, 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY ) 
            datadir, type_ = winreg.QueryValueEx(regkey, REG_LABEL)           
        except FileNotFoundError as e:
            print(f'registry exception...')
            return 0

        self.data_dir = datadir            # we could return:  the datadir, but just set in class
        winreg.CloseKey(regkey)
        print (f'Data Directory : {datadir}')        
        return 1

    
    # GetCPCData: create touple list that matches : host  + date 
    #   - need to make sure we are case compare insensitive...

    def GetCPCData(self):
        status=0
        if self.data_dir == None or self.data_dir == "":
            return 0

        self.zip = f'{self.work_dir}\\{self.data_prefix}_{self.host}_{self.date}.zip'   # zip for output...
        os.chdir(self.data_dir)
        lhost = self.host.lower()
        ldate = self.date.lower()
        lhost_sep = f'{lhost}_'                    # make sure we get the right file  rgesxi vs rgesxi1
        
        for file in glob.glob(self.data_filter):
            lfile = file.lower()
            if ldate in lfile:
                if lhost_sep in lfile:
                    cpcfile_path = f'{self.data_dir}\\{file}'                    
                    self.cpclist.append([cpcfile_path, file])
                    status = 1
        return status

    #
    # GetFileDates: loop through all files and get all unique dates
    #               will be a lot of duplicates checked...  case insensitive 

    def GetFileDates(self):
             
        os.chdir(self.data_dir)                
        self.date_list=[]
        for file in glob.glob(self.data_filter1):
            lfile = file.lower()         
            strs = lfile.split('_')                   # split once. - will get [ecp,hostname,2021aug21,1.cpc]  or 2021aug21.cpc
            strdate = strs[2].split('.')              # split 2nd - if we have a . remove it  strdate will be same as strs[2]
            if strdate not in self.date_list:
                self.date_list.append(strdate)

    #
    # zip_it:  loop through touples list and files to zip (discard path info in zip)
    #
    def zip_it(self):
        print(f'Zip: Create {self.zip}')
        with zipfile.ZipFile(self.zip, 'w', zipfile.ZIP_DEFLATED) as myzip:
            while len(self.cpclist) > 0:
                filetuple = self.cpclist.pop()    
                print(f'   Zip Add:  { filetuple[1]}')    
                myzip.write(filetuple[0], arcname=filetuple[1])
        
    #    
    # GetAllDates:
    #  build up date lists for each known OS : skip the current date
    #-----------------------------------------------------------

    def  GetAllDates(self):
        self.os_date_list = [ ['WINDOWS', [] ] ,                           
                           ['VMWare ESX', [] ],   
                           ['MSSQL', [] ] 
                        ]       
        datetoday = datetime.now().strftime('20%y%b%d').lower()
        for os_data in self.os_date_list:
            self.os = os_data[0]            
            self.GetDataDir()
            self.GetFileDates()

            for datep in self.date_list:    # very inefficent
                if datep[0] in datetoday:      # dont want todays file.
                    continue
                os_data[1].append(datep)   

            self.date_list = None                
        return 
