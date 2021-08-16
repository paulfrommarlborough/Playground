import sys
import argparse

from CouchAddInput import couchinputs
from CouchAddCurl import couchCurl

#------------------------------------------------------------
# Main routine to handle Couch load of   ecapfiles database
#   save zip of cpc files for systems.  adding extra identifying 
#   columns in the database.  host, os, ip, date + attached zip
#----------------------------------------------------------------

def main():
    ci = couchinputs()
    ci.parse()
    print(f'Couch Add Record for {ci.host}, {ci.os}, {ci.ip}, {ci.date} ')
    cc = couchCurl(ci.host, ci.os, ci.ip, ci.date, ci.date_added, ci.zip)
    cc.addEntry()

    if cc.entry_added == False:
        print('----------------------------------------')
        print(f'FAILED to add entry {ci.host}, {ci.zip}')
        print('----------------------------------------')
        return

    #----------------------------------------------------------------------------------
    # Since i Cant really get the  requests.post to work,  just bypass it and call curl..
    #  maybe thats how its all ment to be done.
    #----------------------------------------------------------------------------------
    cc.attachZipCurl()
    print(f'Couch Attach Zip for {ci.host}, {ci.zip}  To : {cc.rev}')
    print('done.')

if __name__ == "__main__":    
    main()