import argparse
import sys
import json

from GetDataFile import GetDataFile
from datetime import datetime
from datetime import timedelta


#  CouchAddInput:  
#     class for input handing : command line processing with   argparse
#  
#     There are 3 ways to run this  (always need -workdir c:\tmp)
#          --all all with an --input input.json 
#               will load all cpc files all dates
#          or 
#          --input input.json
#             will load all for yesterday 
#          or
#          --host hostname --date yyyymmmdd  --ip ipaddress --os osname    
#              will load specific node 
# inputs are
#    --host hostname --os os --ip ip   --zip zipfile
#   or
#   --input input.json --workdir workdir --date
#
#  if no --date default to yesterday.
#
#  return  operations list. 
#--------------------------------------------------------------------

class couchinputs:
 
    # not type casting the inputs should be string.

    def __init__(self):        
        print('CouchInputs,  init...')
        self.all_files = 0
        self.operations_list = []                       # MAKE A LIST
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--host', help='system name tag')
        self.parser.add_argument('--os', help='operating system tag')
        self.parser.add_argument('--ip', help='ip address')
        self.parser.add_argument('--zip', help='zip file to attach')
        self.parser.add_argument('--date', help='data date')
        self.parser.add_argument('--workdir', help='working directory')
        self.parser.add_argument('--all', help='load all files')
        self.parser.add_argument('--input-file', type=argparse.FileType('r'),dest='input_file')        
        

    def parse(self):  
        print('CouchInputs,  parse...')
        self.args = self.parser.parse_args()        
        self.validate()

    def validate(self):
        # -does zip exist
        print(f'CouchInputs, validate..., ')
    
        if self.args.date is None:            
            now = datetime.now() - timedelta(1)
            self.date = now.strftime("20%y%b%d").lower()     
        else:
            self.date = self.args.date.lower()

        if self.args.host is None:            
            self.host = 'localhost'
        else:
            self.host = self.args.host

        if self.args.os is None:            
            self.os = 'unknown'
        else:
            self.os = self.args.os

        if self.args.ip is None:            
            self.ip = '127.0.0.1'
        else:
            self.ip = self.args.ip

        if self.args.zip is None:            
            self.zip = None
        else:
            self.zip = self.args.zip

        if self.args.workdir is None:            
            self.work_dir = None
        else:
            self.work_dir = self.args.workdir
    
        data = None
        if self.args.input_file is not None:

            if self.args.all is None:            
                self.all_files = None
            else:
                self.all_files = 1

            ##---------------------------------------
            ## if all_files : get all dates... for each .. 
            ## when adding to the operations_list loop through all dates.z
            ##---------------------------------------
            date_list = []
            if self.all_files == 1:                
                gdf = GetDataFile(None,None,None,None)
                gdf.GetAllDates()

            #-------------------------
            # import the input file., for each entry 
            #  add the corrisponding dates
            #--------------------------
            
            str_inputfile = self.args.input_file.name    # has to be a string type.
            print(f'Importing from  {str_inputfile}')
            with open(str_inputfile) as file:            
                data = json.load(file)           

                # make operations_list for spcified node(s)

                if self.all_files == 0 or self.all_files == None:       
                    for i in data['collector_settings']:                   
                        i['date'] = f'{self.date}'
                        i['dateadded'] = datetime.now().strftime("%d-%b-20%y %H:%M")   
                        i['zip'] = None
                        newentry = i.copy()
                        print(newentry)
                        self.operations_list.append(newentry)
                else:            
                    #-------------------------------------------------------
                    # all files,  : use stub.json to get good formatted entry
                    #         load stub (newdata)
                    #         copy to a newdata
                    #         for each entry in [data] inputfile
                    #           fill values 
                    #           change date for each date in datelist
                    #              copy to newentry
                    #              save to operations_list
                    #          (TBD: figure out how to do (stubdata) in code)
                    #-------------------------------------------------------

                    str = f"{self.work_dir}\\stub.json"
                    with open(str) as file:            
                        stubdata = json.load(file)
                        newdata = stubdata.copy()

                        for i in data['collector_settings']:                            
                            current_os = i['os'].lower()
                            for x in gdf.os_date_list:
                                entry_os = x[0].lower()
                                if entry_os ==  current_os:
                                    for strdate1 in x[1]:                                                                                               
                                        for j in stubdata['collector_settings']:                                            
                                            j['date'] = strdate1[0]
                                            j['dateadded'] = datetime.now().strftime("%d-%b-20%y %H:%M")   
                                            j['name'] = i['name']
                                            j['os'] = i['os']
                                            j['ip'] = i['ip']
                                            j['zip'] = None
                                        newentry = j.copy()
                                        print(newentry)
                                        self.operations_list.append(newentry)
        else:
                ## only on command line
                ##
                ## if all_files : get all dates... for the system in question
                ## when adding to the operations_list loop through all dates.z
            date_list = []
            if self.all_files == 1:                
                gdf = GetDataFile(None,None,None,None)
                gdf.GetAllDates()

            i = {}                   # empty dict
#            str = "C:\\tools\\tmp\\stub.json"
            str = f"{self.work_dir}\\stub.json"
            with open(str) as file:            
                data = json.load(file)           
                for i in data['collector_settings']:                        
                    i['date'] = f'{self.date}'
                    i['dateadded'] = datetime.now().strftime("%d-%b-20%y %H:%M")   
                    i['name'] = f'{self.host}'
                    i['os'] = f'{self.os}'
                    i['ip'] = f'{self.ip}'
                    i['zip'] = self.zip
                    newentry = i.copy()                                
                    self.operations_list.append(newentry)                       

#        print('-----------------------------------------')
#        for jdata in  self.operations_list:          
#           print(jdata)
        return 1
        
       
