import requests, io, json
import subprocess

#  CouchAddCurl:  
#     class to handle curl operations.
#  

from requests.exceptions import ConnectionError

# add with json: need to write json, and then run curl
#  curl to add entry 
#     curl -X PUT http://admin:pawz1@127.0.0.1:5984/ecapfiles/palladium_2021apr01 -d @example.json -H "Content-type: application/json"
#  curl to attach file
#     curl -vX PUT http://admin:pawz1@127.0.0.1:5984/ecapfiles/palladium_2021apr01/ecp_Palladium_2021Apr01.zip?rev=11-49c188b2f6b009288046e4e80c305b55 --data-binary @ecp_Palladium_2021Apr01.zip -H "Content-Type: application/zip"

class couchCurl:
    def __init__(self, host, os, ip, date, dateadded, zip):
        self.host = host        
        self.os = os
        self.ip = ip
        self.date = date
        self.date_added = dateadded
        self.zip = zip
        self.filename = f'{host}_{date}'
        self.entry_added = False
        self.rev = None
        return

    def buildJson(self):
        data_set = {"name": self.host, "ip": self.ip, "os": self.os, "date": self.date,"dateadded":self.date_added}
        self.json_data = json.dumps(data_set)
        print(f'Input Json: {self.json_data}')


    # needs the zip file name for data. ?
    def buildJson_attach(self):
        data_set = {'rev': self.rev}
        self.json_data_attach = json.dumps(data_set)
        print(f'Input Json: {self.json_data_attach}')


    #-------------------------------------------------------
    # addentry:
    #   request works with straight requsts PUT - uses json with inputs
    #   saves the rev value , so we can attach the file.
    #------------------------------------------------------------------
    
    def addEntry(self):

        self.buildJson()

        print(f'couchCurl.addEntry {self.host}')
        
        # need more info
        urlx = f'http://admin:pawz1@127.0.0.1:5984/ecapfiles/{self.filename}'
        try:           
           r = requests.put(urlx, data =self.json_data)
        except ConnectionError as e:
            print(f'--------------------------------------------------------')
            print(f' EXCEPTION ERROR, PUT initial record:  {urlx}')           
            print(f'--------------------------------------------------------')
            r = None
            return

        if r.ok  == False:
            print(f'Error {r.status_code} :  {r.reason}')
            return


        contentJson= r.json()                                    
        self.rev = contentJson["rev"]
        status = contentJson["ok"]
        self.entry_added = True
        
        print(f'AddEntry: Status {status},  Rev {self.rev}')
        return


    #----------------------------------------------------------------------------------
    #  attachZipCurl
    #
    # Since i Cant really get the  requests.post to work,  just bypass it and call curl..
    # maybe thats how its all ment to be done.
    #----------------------------------------------------------------------------------

    def attachZipCurl(self):
        zip_with_path = f'@{self.zip}'
        zip_no_path= f'{self.filename}.zip'

        urlx = f'http://admin:pawz1@127.0.0.1:5984/ecapfiles/{self.filename}/{zip_no_path}?rev={self.rev}'
        subprocess.run(['curl', '-vX', 'PUT', urlx, '--data-binary', zip_with_path, '-H', 'Content-Type: application/zip' ] )
        return

    #--------------------------------------------------------------------------
    # attachZip:   requests.post
    #  upload a multipart-encoded mime file  -   cant get to work.
    #--------------------------------------------------------------------------
    
    def attachZip(self):
        print(f'attach zip')
        self.buildJson_attach()
        headers = { "content-type":"application/zip" }
       # files = {'file': (self.zip, open(self.zip, 'rb').read(), 'application/zip', {'Expires': '0'})}
        files = {'file': (self.zip, open(self.zip, 'rb').read(), 'application/zip' )}
        #files={"archive": ("test.zip", fileobj)}
        urlx = f'http://admin:pawz1@127.0.0.1:5984/ecapfiles/{self.filename}'
        try:        
           r = requests.post(urlx, headers=headers,files=files,params=self.json_data_attach)

        except ConnectionError as e:
            print(f'--------------------------------------------------------')
            print(f'  *** ATTACH EXCEPTION ERROR. ATTACH {urlx}')           
            print(f'--------------------------------------------------------')
            r = None
            return

        if r.ok  == False:
            print(f'Error {r.status_code} :  {r.reason}')
            return
