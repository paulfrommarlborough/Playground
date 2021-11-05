
import json
from datetime import datetime
from logging import error
from urllib.request import urlopen

class influxpawz_settings:
 
    # not type casting the inputs should be string.

    def __init__(self,  dw, pu, pp, pws, iu, ip, iws): 
        self.pawzwebsite = pws
        self.influxwebsite= iws
        self.pawzusername = pu
        self.pawzpwd = pp
        self.datewanted = dw      
        self.influxusername = iu
        self.influxpwd = ip
        self.node_list = []             # list of dictionary items



    # get all nodes and OS

    def GetNodeInfo(self):
        url = f"{self.pawzwebsite}/restful/getNodeConfig_v150/{self.pawzusername}/{self.pawzpwd}/All/epoch"
        response = urlopen(url)
        try:
            data_json = json.loads(response.read())
        except:
            print('exception caught')
            return

#        print(data_json)

        # ether is set...
        results = None
        x = None

        try:
            x = data_json['ERROR']
        except:
            pass

        try:
            results = data_json['Result']
        except:
            pass

        if x != None:
            if x == "User Authentication Failure":
                print ( f'GetConfig Error: {x}')
                return 

        if results == None:
            print('GetConfig :no results')
            return

        rResults = len(results)
        for r in range(0, rResults):
            node_name = None
            node_os = None
#            print(results[r])
            node_name = results[r]['Node']
#           node_name = node_name.replace("'", "")

            try:
                node_os = results[r]['Data'][0]['Operating System']
 #               node_os = node_os.replace("'", "")
            except:
                pass
#            print(f'GetConfig:  {node_name}  {node_os}')
            thisdict = {
                "Name": node_name,
                "OS": node_os
            }
            self.node_list.append(thisdict)
        return
