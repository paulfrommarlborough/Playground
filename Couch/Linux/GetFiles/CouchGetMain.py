import sys
import os
import zipfile
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
#
# notes :  in progress.    get fetch functions working. - see about combining with couchAdd
#--------------------------------------------------------------------------------

def main():
    ci = couchinputs()
    status = ci.parse()
    if status == False:
        print('too many options missing, cant continue')
        return

    # special case we have a HOSTname - no dates - get all

    if ci.host is not None and ci.date is None:
        print('get all for host {ci.host}')
        cc = couchCurl(ci.server, ci.username, ci.password, ci.host, ci.os, ci.ip, None, None, ci.work_dir, None)
        cc.getAllDocuments()
        return


    for jdata in  ci.operations_list:           
#       print(jdata)    
        print(f'Couch Record Get: GetZip, {jdata["name"]}, {jdata["os"]}, {jdata["ip"]}, {jdata["date"]} ')
        cc = couchCurl(ci.server, ci.username, ci.password, jdata["name"], jdata["os"], jdata["ip"], jdata["date"], None, ci.work_dir, None)

        cc.checkEntry()
        if cc.already_exists == False:
            print(f'Couch Record DOESNT EXIST: ... ID: {cc.filename} ')
            continue

        status =  cc.getAttachment() # requests
        if status == True:
            print(f'Copied:  {cc.zip}')
            ## make sure cc.zip has path.
            with zipfile.ZipFile(cc.zip, 'r') as zip_ref:                
                zip_ref.extractall(cc.work_dir)
            os.remove(cc.zip)

        else:
            print(f'Failed:  {cc.filename}')
            
    #    cc.getAttachmentCurl()   # curl has more screen output.

        print('CouchGetMain: done.')

#---------------------------------
# main
#---------------------------------

if __name__ == "__main__":    
    main()
