import sys
import os

from os import path
from CouchGetInput import couchinputs 
from CouchCurl import couchCurl

#--------------------------------------------------------------------------
#  couchGetMain:
#
#   Main routine to handle getting document from ecapfiles database
#
#  author paul douglas                          25-aug-2021
#
# dependencies  : couchdb, requests,
#--------------------------------------------------------------------------------

def main():
    ci = couchinputs()
    ci.parse()

    for jdata in  ci.operations_list:           
#       print(jdata)    
        print(f'\nCouch Record Get: GetZip, {jdata["name"]}, {jdata["os"]}, {jdata["ip"]}, {jdata["date"]} ')
        cc = couchCurl(ci.server, ci.username, ci.password, jdata["name"], jdata["os"], jdata["ip"], jdata["date"], None, None)

        cc.checkEntry()
        if cc.already_exists == False:
            print(f'Couch Record DOESNT EXIST: ... ID: {cc.filename} ')
            continue

    print('CouchGetMain: done.')


#---------------------------------
# main
#---------------------------------

if __name__ == "__main__":    
    main()