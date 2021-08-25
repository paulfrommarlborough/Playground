import sys
import os

from os import path

from CouchAddInput import couchinputs
from CouchCurl import couchCurl
from GetDataFile import GetDataFile

#--------------------------------------------------------------------------
#  couchAddMain:
#
#   Main routine to handle load of  datafile (Zip) to  CouchDB->ecapfiles database
#     save zip of cpc files for systems.  adding extra identifying 
#     columns in the database.  host, os, ip, date, dateadded + attached zip
#  author paul douglas                          23-aug-2021
#
# dependencies  : couchdb, requests,
#--------------------------------------------------------------------------------

def main():
    zip = None

    # parse inputs and get operations list

    ci = couchinputs()
    ci.parse()
    
    for jdata in  ci.operations_list:           
#       print(jdata)    
        print(f'\nCouch Record ADD: Add Entry, {jdata["name"]}, {jdata["os"]}, {jdata["ip"]}, {jdata["date"]} ')

        cc = couchCurl(ci.username, ci.password, jdata["name"], jdata["os"], jdata["ip"], jdata["date"], jdata["dateadded"], None)
        
        # see if we already have it.

        cc.checkEntry()
        if cc.already_exists == True:
            print(f'Couch Record EXISTS: ... ID: {cc.filename} ')
            continue

        # no zip on command line. - get cpcfiles and create a zip
        if jdata["zip"] is None:
            print(f"Couch Record ADD: Create ZIP")
 
            gdf  = GetDataFile(jdata["name"], jdata["os"], jdata["date"], ci.work_dir)
            status = gdf.GetDataDir()        # get zip
            if status == 1:
                status = gdf.GetCPCData()   
                if status == 1:
                    gdf.zip_it()

            if gdf.zip is None:
                print(f'Couch Record ADD:  ZIP file not found....')
                continue
            zip = gdf.zip
        else:
            zip = jdata['zip']

        # we we have a zip file
        
        if path.exists(zip) == False:
            print(f'Couch Record ADD:  Specified ZIP file not NOT FOUND, {zip}')
            continue

        # 
        #  2 step process.   Add Entry   (requests  library)
        #                    attach zip  (curl)
    
        cc.zip = zip

        print(f'Couch Record ADD: Add Entry {jdata["name"]}')
        cc.addEntry()

        if cc.entry_added == False:
            print('----------------------------------------')
            print(f'FAILED to add entry {jdata["name"]}, {zip}')
            print('----------------------------------------')
            print(f'DELETE: {zip}')

            try:    
                os.remove(zip)
            except OSError as error:
                print(error)

            continue

        #--------------------------------------------------------------------
        # attach zip
        #--------------------------------------------------------------------

        cc.attachZipCurl()

        # need to query couchdb and see if entry has an attachment.

        print(f'Couch Record ADD:  ATTACH ZIP for {jdata["name"]}, {zip}  To : {cc.rev}')
    
        # delete local zip file
        print(f'DELETE: {zip}')

        try:
            os.remove(zip)
        except OSError as error:
            print(error)

        print('CouchAddMain: done.')

#---------------------------------
# main
#---------------------------------

if __name__ == "__main__":    
    main()