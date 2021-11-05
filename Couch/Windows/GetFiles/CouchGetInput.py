import argparse
import sys
import json
from datetime import datetime
from datetime import timedelta

#  we can have an input file :  say --os Windows --input_file C:\input.json
#     we can get all os with windows

class couchinputs:

    # not type casting the inputs should be string.

    def __init__(self):        
        print('CouchInputs,  init...')
        self.all_files = 0
        self.operations_list = []                       # MAKE A LIST
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--host', help='system name tag')
        self.parser.add_argument('--yesterday', help='get only yesterday', action="store_true")
        self.parser.add_argument('--os', help='operating system tag')
        self.parser.add_argument('--ip', help='ip address')
        self.parser.add_argument('--date', help='data date')
        self.parser.add_argument('--workdir', help='working directory')
        self.parser.add_argument('--server', help='couchdb server')
        self.parser.add_argument('--username', help='username')
        self.parser.add_argument('--password', help='password')        
        self.parser.add_argument('--input-file', type=argparse.FileType('r'),dest='input_file')        
        
    def parse(self):  
        print('CouchInputs,  parse...')
        self.args = self.parser.parse_args()        
        status  = self.validate()
        return status

    def validate(self):
        # -does zip exist
        print(f'CouchInputs,  validate..., ')

        # do we default to yesterday - or None
        if self.args.date is None:  
            if self.args.yesterday is None:
                self.date = None          
            else:
                now = datetime.now() - timedelta(1)
                self.date = now.strftime("20%y%b%d").lower()     
        else:
            self.date = self.args.date.lower()

        if self.args.host is None:            
            self.host = None
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

        if self.args.server is None:            
            self.server = '127.0.0.1:5984'
        else:
            self.server = self.args.server

        if self.args.username is None:            
            self.username = 'admin'
        else:
            self.username = self.args.username

        if self.args.password is None:            
            self.password = 'pawz1'
        else:
            self.password = self.args.password

        if self.args.workdir is None:            
            self.work_dir = None
        else:
            self.work_dir = self.args.workdir
    
        #----------------------------
        # get input file
        #----------------------------

        hostdata = None
        if self.args.input_file is not None:
            str_inputfile = self.args.input_file.name    # has to be a string type.
            print(f'Importing from  {str_inputfile}')
            with open(str_inputfile) as file:            
                hostdata = json.load(file)           

        #----------------------------
        # get stub file
        #----------------------------

        if self.work_dir is None:
            str = "stub.json"
        else:
            str = f"{self.work_dir}\\stub.json"
        
        try:
            with open(str) as file:            
                stubdata = json.load(file)
                newdata = stubdata.copy()
        except:
            print(f'unable top open {self.work_dir}\\stub.file')
            return False
        #----------------------------
        # figure out what data to get
        #----------------------------

        if self.date is not None:
            if self.host is not None:
                # have date and host
                for j in stubdata['collector_settings']:                            
                    j['date'] = self.date              
                    j['name'] = self.host
                    j['os'] = self.os
                    j['ip'] = self.ip
                    j['zip'] = None
                    newentry = j.copy()
                    print(newentry)
                    self.operations_list.append(newentry)
            else:
                # no host but we have a date.
                print("have date no host")
                for i in hostdata['collector_settings']:       
                    for j in stubdata['collector_settings']:                            
                        j['date'] = self.date              
                        j['name'] = i['name']
                        j['os'] = i['os']
                        j['ip'] = i['ip']
                        j['zip'] = None
                        newentry = j.copy()
                        print(newentry)
                        self.operations_list.append(newentry)


        else:     # no date   - how do we get all dates or yesterday?
            if self.host is not None:
                print("have host, no date")
                
        print(self.operations_list)
        return True
