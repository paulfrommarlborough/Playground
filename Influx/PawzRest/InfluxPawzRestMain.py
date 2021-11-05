# InfluxPawzRestMain.py
#
#    Main Entry for taking PAWZ from rest and feeding it into influxdb
#----------------------------------------------------------------------

# from logging import NullHandler
import time
import json
from datetime import datetime
from urllib.request import urlopen

from InfluxWriter import InfluxWriter
from InfluxPawzRestInput import influxpawz_inputs
from InfluxPawzRestSettings import influxpawz_settings
from InfluxPawzRestWorker import influxpawz_worker


#----------------------------------------
# Notes: make multi-threading loading...
#----------------------------------------

#hostname='palladium'

#---------------------------------------------
# MAIN worker 
#---------------------------------------------
def main(ifpSettings):

    # get node list...    
    ifpWorker = influxpawz_worker(ifpSettings.pawzusername, ifpSettings.pawzpwd, ifpSettings.pawzwebsite, 
                          ifpSettings.influxusername, ifpSettings.influxpwd, ifpSettings.influxwebsite)
    ifpSettings.GetNodeInfo()
    

    #load or each node.
    nNodes= len(ifpSettings.node_list)
    print(f'Process {nNodes} From PAWZ to InfluxDb')
    
    for i in range (0, nNodes):
        node_name = ifpSettings.node_list[i]['Name']
        node_os = ifpSettings.node_list[i]['OS']   
        print(f'Load {node_name},{node_os},{ifpSettings.datewanted}')
        ifpWorker.Load(node_name, node_os, ifpSettings.datewanted)

    endtime = datetime.now()
#---------------------------------
# main
#---------------------------------

if __name__ == "__main__":    

    ifpInput = influxpawz_inputs()
    ifpInput.parse()
    bstatus = ifpInput.validate()
    if bstatus == True:
        starttime = datetime.now()
        ifpSettings = influxpawz_settings(ifpInput.datewanted, ifpInput.pawzusername, ifpInput.pawzpwd, ifpInput.pawzwebsite, 
                                    ifpInput.influxusername, ifpInput.influxpwd, ifpInput.influxwebsite)
        main(ifpSettings)
 
        endtime = datetime.now()
        duration = endtime - starttime    
        print(f'PAWZ export to Influx done : in {duration}')