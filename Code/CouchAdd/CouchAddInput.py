import argparse
import sys
from datetime import datetime
from datetime import timedelta

#  CouchAddInput:  
#     class for input handing : command line processing with   argparse
#  


class couchinputs:
 
    # not type casting the inputs should be string.

    def __init__(self):        
        print('init couch input...')
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--host', help='system name tag')
        self.parser.add_argument('--os', help='operating system tag')
        self.parser.add_argument('--ip', help='ip address')
        self.parser.add_argument('--zip', help='zip file to attach')
        self.parser.add_argument('--date', help='data date')
        print('init couch input...DONE')

    def parse(self):  
        print('parse couch input...')
        self.args = self.parser.parse_args()
        print('parse couch input...DONE')
        self.validate()

    def validate(self):
        # -does zip exist
        print(f'check existence of {self.args.zip}')
        #if date is null then set to yesterday
        print(f'check date {self.args.date}')

        if self.args.date is None:            
            now = datetime.now() - timedelta(1)
            self.date = now.strftime("20%y%b%d")         
        else:
            self.date = self.args.date

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

        self.filename= f'{self.host}_{self.date}'
        self.date_added = datetime.now().strftime("%d-%b-20%y %H:%M")          
        return 1
        
       
