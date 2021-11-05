# InfluxPawzRestWorker.py
#
#    Main worker
#      keeping the urls seperate even though there is a bunch of the same.
#----------------------------------------------------------------------

from datetime import datetime
import json
from urllib.request import urlopen

from InfluxWriter import InfluxWriter

class influxpawz_worker:
 
    # not type casting the inputs should be string.

    def __init__(self, u, p, pws, iu, ip, iws): 
        self.pawzusername = u
        self.pawzpwd = p
        self.influxuser = iu
        self.influxpwd = ip
        self.pawzwebsite = pws
        self.influxwebsite = iws
        self.hostname=None
        self.datewanted = None 
        self.node_list = []                                  # list of dictionary items
        self.url_list = []
        self.verbose = 0

    # --------------------------------------
    # LOAD
    #---------------------------------------

    def Load(self, node, os, dw):
        starttime = datetime.now()
        if self.verbose == 1:
            print(f'PAWZ to InfluxDB worker...{node}')
        self.hostname = node
        self.datewanted= dw

        ifxWriter = InfluxWriter( self.influxwebsite, self.influxuser, self.influxpwd, 'perfcap', 'PAWZrest')    # influx, org + dataabase
        ifxWriter.Setup()

        self.BuildUrls(os)

        for x in range(0, len(self.url_list)):
            url = self.url_list[x]
            #if self.verbose == 1:
            print(f'Load: {url}')    

            response = urlopen(url)
            try:
                data_json = json.loads(response.read())
            except:
                print('exception caught')
                continue

            rResults = len(data_json['Result'])

            if rResults == 0:
                continue

            if rResults == 1:
                result_one = json.dumps(data_json['Result'][0])
                result_one = result_one.replace('"','')
                result_one = result_one.strip() 
                if result_one == 'No Data Found':
                    print(url)
                    print(result_one)
                    continue

            for r in range(0, rResults):
                data_nodename= data_json['Result'][r]['Node']
                data_metric = data_json['Result'][r]['Metric']
                data_submetric = data_json['Result'][r]['SubMetric']
                data_counter = data_json['Result'][r]['Counter']
                data_graphtitle = data_json['Result'][r]['Graph Title']

                if self.verbose == 1:
                    print(f" Process Node: {data_json['Result'][r]['Node']} , GraphTitle : {data_json['Result'][r]['Graph Title']} ")

                len1 = len(data_json['Result'][r]['Data'])
                for i in range(0, len1):
                    datavalue= data_json['Result'][r]['Data'][i]['Value']
                    if datavalue == "HOLE":
                        continue

                    timevalue = data_json['Result'][r]['Data'][i]['Time']
                    data_counter1 = data_counter.replace(' ', '\\ ')
            
                    data_graphtitle1 = data_graphtitle.replace(' ', '\\ ')
                    data_submetric1 = data_submetric.replace(' ',  '\\ ')

                    tval = int(timevalue)                     # python3 only int  has unlimted size
                    tval = tval * 1000000000                   # seconds to nano-sec  - 1,000,000,000 * secs

                    #line for input into influx
                    #encapsulating in '' adds the single quotes with the field. 

                    #influx_data_prefix=f"{data_metric},Node='{data_nodename}',Metric='{data_metric}',Submetric='{data_submetric1}',Counter='{data_counter1}',GraphTitle='{data_graphtitle1}' Value={datavalue} {timevalue}"
            
                    # metric is the measurement
                    influx_data_prefix=f"{data_metric},Node={data_nodename},Submetric={data_submetric1},Counter={data_counter1},GraphTitle={data_graphtitle1} Value={datavalue} {tval}"
                    ifxWriter.Write(influx_data_prefix)

        endtime = datetime.now()
        duration = endtime - starttime
        self.url_list.clear()
        # call gc ?        
        print(f'Load: {self.hostname} done  in {duration}')

    #-------------------------------------
    # URLS : for Windows
    #-------------------------------------

    def buildurl_windows(self):
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/Utilization/Total%20Processor%20Time/{self.datewanted}/epoch" )
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Top%20Image/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Processor/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Mode/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/Average%20Queue%20Length/Average%20Queue%20Length/{self.datewanted}/epoch")

        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Overall%20IO%20Rate/IO%20Rate/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Response%20Time/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Rate/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Data%20Rate/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Queue%20Length/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Images%20by%20IO%20Rate/ALL/{self.datewanted}/epoch")

        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Utilization/Memory%20Utilization/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Allocation/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Top%20Images%20by%20Memory%20Used/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Process/Count/Processes/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/NIC/Data%20Sent/All/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/NIC/Data%20Received/All/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardFavorites_V150/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Process/All/CPU%20Utilization%20(%25)/{self.datewanted}/epoch")
        # windows specific
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardFavorites_V150/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Process/All/Private%20Bytes/{self.datewanted}/epoch")

    def buildurl_linux(self):
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/Utilization/Total%20Processor%20Time/{self.datewanted}/epoch" )
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Top%20Image/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Processor/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Mode/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/Average%20Queue%20Length/Average%20Queue%20Length/{self.datewanted}/epoch")

        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Overall%20IO%20Rate/IO%20Rate/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Response%20Time/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Rate/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Data%20Rate/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Queue%20Length/ALL/{self.datewanted}/epoch")
#        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Images%20by%20IO%20Rate/ALL/{self.datewanted}/epoch")

        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Utilization/Memory%20Utilization/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Allocation/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Top%20Images%20by%20Memory%20Used/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Process/Count/Processes/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/NIC/Data%20Sent/All/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/NIC/Data%20Received/All/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardFavorites_V150/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Process/All/CPU%20Utilization%20(%25)/{self.datewanted}/epoch")

    def buildurl_aix(self):
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/Utilization/Total%20Processor%20Time/{self.datewanted}/epoch" )
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Top%20Image/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Processor/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Mode/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/Average%20Queue%20Length/Average%20Queue%20Length/{self.datewanted}/epoch")

        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Overall%20IO%20Rate/IO%20Rate/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Response%20Time/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Rate/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Data%20Rate/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Queue%20Length/ALL/{self.datewanted}/epoch")
#        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Images%20by%20IO%20Rate/ALL/{self.datewanted}/epoch")

        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Utilization/Memory%20Utilization/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Allocation/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Top%20Images%20by%20Memory%20Used/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Process/Count/Processes/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/NIC/Data%20Sent/All/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/NIC/Data%20Received/All/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardFavorites_V150/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Process/All/CPU%20Utilization%20(%25)/{self.datewanted}/epoch")

    def buildurl_solaris(self):
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/Utilization/Total%20Processor%20Time/{self.datewanted}/epoch" )
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Top%20Image/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Processor/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Mode/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/Average%20Queue%20Length/Average%20Queue%20Length/{self.datewanted}/epoch")

        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Overall%20IO%20Rate/IO%20Rate/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Response%20Time/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Rate/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Data%20Rate/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Queue%20Length/ALL/{self.datewanted}/epoch")
#        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Images%20by%20IO%20Rate/ALL/{self.datewanted}/epoch")

        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Utilization/Memory%20Utilization/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Allocation/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Top%20Images%20by%20Memory%20Used/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Process/Count/Processes/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/NIC/Data%20Sent/All/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/NIC/Data%20Received/All/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardFavorites_V150/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Process/All/CPU%20Utilization%20(%25)/{self.datewanted}/epoch")
    
    def buildurl_hpux(self):
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/Utilization/Total%20Processor%20Time/{self.datewanted}/epoch" )
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Top%20Image/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Processor/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Mode/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/Average%20Queue%20Length/Average%20Queue%20Length/{self.datewanted}/epoch")

        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Overall%20IO%20Rate/IO%20Rate/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Response%20Time/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Rate/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Data%20Rate/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Queue%20Length/ALL/{self.datewanted}/epoch")
#        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Images%20by%20IO%20Rate/ALL/{self.datewanted}/epoch")

        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Utilization/Memory%20Utilization/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Allocation/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Top%20Images%20by%20Memory%20Used/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Process/Count/Processes/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/NIC/Data%20Sent/All/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/NIC/Data%20Received/All/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardFavorites_V150/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Process/All/CPU%20Utilization%20(%25)/{self.datewanted}/epoch")

    def buildurl_vmware(self):
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/Utilization/Total%20Processor%20Time/{self.datewanted}/epoch" )
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Top%20VM/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Processor/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/MHZ%20Usage/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/MHZ%20Usage%20by%20VM/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/Ready%20Time%20by%20VM/ALL/{self.datewanted}/epoch")
        
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Overall%20IO%20Rate/IO%20Rate/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Response%20Time/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Rate/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Data%20Rate/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Queue%20Length/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20VM%20by%20IO%20Rate/ALL/{self.datewanted}/epoch")

        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Utilization/Memory%20Utilization/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Allocation/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Top%20VM%20by%20Memory%20Used/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Balloon%20Driver%20by%20VM/ALL/{self.datewanted}/epoch")

        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Network/Network%20Data%20Rate/Network%20Data%20Rate/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/VM/Count/VMs/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/NIC/Data%20Sent/All/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/NIC/Data%20Received/All/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardFavorites_V150/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/VM/All/CPU%20MHZ/{self.datewanted}/epoch")
      
    def buildurl_openvms(self):
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/Utilization/Total%20Processor%20Time/{self.datewanted}/epoch" )
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Top%20Image/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Processor/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/By%20Mode/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/Average%20Queue%20Length/Average%20Queue%20Length/{self.datewanted}/epoch")

        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Overall%20IO%20Rate/IO%20Rate/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Response%20Time/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Rate/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Data%20Rate/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Disks%20by%20Queue%20Length/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Disk/Top%20Images%20by%20IO%20Rate/ALL/{self.datewanted}/epoch")

        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Utilization/Memory%20Utilization/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Allocation/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Memory/Top%20Images%20by%20Memory%20Used/ALL/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Process/Count/Processes/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/NIC/Data%20Sent/All/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/NIC/Data%20Received/All/{self.datewanted}/epoch")
        self.url_list.append(f"{self.pawzwebsite}/restful/getStandardFavorites_V150/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/Process/All/CPU%20Utilization%20(%25)/{self.datewanted}/epoch")


    # need to check that hostname  =  hostname(sqlname) - does the sqlname get returned with the config?
    def buildurls_mssql(self):                                      
        self.url_list(f"{self.pawzwebsite}/restful/getStandardGraph_V120/{self.pawzusername}/{self.pawzpwd}/{self.hostname}/CPU/%25%20Utilization/ALL/{self.datewanted}/epoch")
        return

    def buildurls_emc(self):                                       
        return

    #---------------------------------------------
    # BUILD URLS
    #---------------------------------------------

    def BuildUrls(self, os):
        if os == 'Windows':
            self.buildurl_windows()
        elif os == 'Linux':
            self.buildurl_linux()
        elif os == 'VMware ESXi':
            self.buildurl_vmware()
        elif os == 'OpenVMS IA64':
            self.buildurl_openvms()
        elif os == 'Solaris':
            self.buildurl_solaris()
        elif os == 'Solaris x86':
            self.buildurl_solaris()
        elif os == 'HPUX':
            self.buildurl_hpux()
        elif os == 'IBM AIX':
            self.buildurl_aix()            
        elif os == 'MSSQL':
            self.buildurl_mssql()            
        
