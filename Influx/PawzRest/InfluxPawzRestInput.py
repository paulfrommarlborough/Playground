import argparse
import sys

class influxpawz_inputs:
 
    # not type casting the inputs should be string.

    def __init__(self):        
        self.pawzusername=""
        self.pawzpwd =""
        print('InfluxPawzInput,  init...')
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--influx', help='influx web tag')
        self.parser.add_argument('--pawz', help='pawz web tag')

        self.parser.add_argument('--pawzusername', help='username')
        self.parser.add_argument('--pawzpassword', help='password')        

        self.parser.add_argument('--influxusername', help='username')
        self.parser.add_argument('--influxpassword', help='password')        

        self.parser.add_argument('--date', help='data date')        

    def parse(self):  
        print('InfluxPawzInput,  parse...')  
        self.args = self.parser.parse_args()        
        self.validate()

    def validate(self):
        # -does zip exist
        print(f'InfluxPawzInput, validate..., ')

        if self.args.pawzusername is None:            
            self.pawzusername = 'admin'
        else:
            self.pawzusername = self.args.pawzusername

        if self.args.pawzpassword is None:            
            self.pawzpwd = 'pawz1'
        else:
            self.pawzpwd = self.args.pawzpassword

        if self.args.influxusername is None:            
            self.influxusername = 'admin'
        else:
            self.influxusername = self.args.influxusername

        if self.args.influxpassword is None:            
            self.influxpwd = 'pawz1'
        else:
            self.influxpwd = self.args.influxpassword


        if self.args.date is None:            
            self.datewanted = '10-23-2021'
        else:
            self.datewanted = self.args.date

        if self.args.pawz is None:            
            self.pawzwebsite = 'http://localhost'
        else:
            self.pawzwebsite = self.args.pawz

        if self.args.influx is None:            
            self.influxwebsite = 'http://localhost:8086'
        else:
            self.influxwebsite = self.args.influx

        return True
