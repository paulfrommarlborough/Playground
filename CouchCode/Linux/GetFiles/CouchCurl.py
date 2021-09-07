import requests, io, json
import subprocess, os
import zipfile
from datetime import datetime

#  CouchAddCurl:  
#     class to handle curl operations.
#  

from requests.exceptions import ConnectionError


class couchCurl:
    def __init__(self, server, username, password, host, os, ip, date, dateadded, workdir, zip):
        self.zip_with_path = None
        self.host = host        
        self.os = os
        self.ip = ip
        self.date = date
        self.server = server
        self.work_dir = workdir
        self.username = username
        self.password = password
        self.zip = zip
        self.filename = f'{host}_{date}'
        self.entry_added = False
        self.rev = None
        self.already_exists = False
        return

    def buildJson(self):
        self.date_added = datetime.now().strftime("%d-%b-20%y %H:%M")    # make current.
        data_set = {"name": self.host, "ip": self.ip, "os": self.os, "date": self.date}
        self.json_data = json.dumps(data_set)
        print(f'Input Json: {self.json_data}')


    # needs the zip file name for data. ?

    def buildJson_attach(self):
        data_set = {'rev': self.rev}
        self.json_data_attach = json.dumps(data_set)
        print(f'Attach Input Json: {self.json_data_attach}')

    #-------------------------------------------------------
    # addentry:
    #   request works with straight requsts PUT - uses json with inputs
    #   saves the rev value , so we can attach the file.
    #------------------------------------------------------------------
    
    def checkEntry(self):
        self.already_exists = False
        urlx = f'http://{self.username}:{self.password}@{self.server}/ecapfiles/{self.filename}'
        try:           
           r = requests.get(urlx)
        except ConnectionError as e:
            print(f'--------------------------------------------------------')
            print(f' EXCEPTION ERROR, GET initial record:  {urlx}')           
            print(f'--------------------------------------------------------')
            return False

        if r.status_code == 200:
            self.already_exists=True

        return self.already_exists

    #-------------------------------------------
    # addEntry:  add entry into couchdb
    #
    #      sets member variable entry_added
    #-------------------------------------------

    def addEntry(self):

        self.buildJson()

        print(f'couchCurl.addEntry {self.host}')
        
        # need more info
        urlx = f'http://{self.username}:{self.password}@{self.server}/ecapfiles/{self.filename}'
        try:           
           r = requests.put(urlx, data =self.json_data)
        except ConnectionError as e:
            print(f'--------------------------------------------------------')
            print(f' EXCEPTION ERROR, PUT initial record:  {urlx}')           
            print(f'--------------------------------------------------------')
            r = None
            return  self.entry_added

        if r.ok  == False:
            print(f'Error {r.status_code} :  {r.reason}')
            return self.entry_added


        contentJson= r.json()                                    
        self.rev = contentJson["rev"]
        status = contentJson["ok"]
        self.entry_added = True
        
        print(f'AddEntry: Status {status},  Rev {self.rev}')
        return  self.entry_added


    #----------------------------------------------------------------------------------
    #  attachZipCurl
    #
    # Since i Cant really get the  requests.post to work,  just bypass it and call curl..
    # maybe thats how its all ment to be done. (investigate pycurl)
    #----------------------------------------------------------------------------------

    def attachZipCurl(self):
        self.zip_with_path = f'@{self.zip}'
        zip_no_path= f'{self.filename}.zip'
        os.chdir(self.work_dir)  

        urlx = f'http://{self.username}:{self.password}@{self.server}/ecapfiles/{self.filename}/{zip_no_path}?rev={self.rev}'
        subprocess.run(['curl', '-vX', 'PUT', urlx, '--data-binary', self.zip_with_path, '-H', 'Content-Type: application/zip' ] )
        return True

    #--------------------------------------------------------------------------
    # attachZip:   requests.post
    #  upload a multipart-encoded mime file  -   cant get to work.
    #--------------------------------------------------------------------------
    
    def attachZip(self):
        print(f'attach zip')
        self.buildJson_attach()
        headers = { "content-type":"application/zip" }       
        files = {'file': (self.zip, open(self.zip, 'rb').read(), 'application/zip' )}
        urlx = f'http://{self.username}:{self.password}@{self.server}/ecapfiles/{self.filename}'
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

#  curl -vX GET http://admin:pawz1@192.168.1.167:5984/pawzfiles/ecapdev_2021Mar18/ecp_ecapdev_2021Mar18.zip -O -J

#-----------------------------------------------------------
# getAttachmentCurl
#----------------------------------------------------------
    def getAttachmentCurl(self):
        print(f'get attachment...')
        zip_no_path= f'{self.filename}.zip'

        os.chdir(self.work_dir)
        # command line order seems to matter
        urlx = f'http://{self.username}:{self.password}@{self.server}/ecapfiles/{self.filename}/{zip_no_path}'
        subprocess.run(['curl', '-vX', 'GET', urlx, '-O', '-J' ] )

        return

#-----------------------------------------------------------
# getAttachment
#----------------------------------------------------------
    def getAttachment(self):
        zip_no_path= f'{self.filename}.zip'
        self.zip_with_path = f'{self.work_dir}/{zip_no_path}'
        
        print(f'get attachment...')

        urlx = f'http://{self.username}:{self.password}@{self.server}/ecapfiles/{self.filename}/{zip_no_path}'
        print(f'{urlx}')
        try:           
           r = requests.get(urlx,stream=True)
        except ConnectionError as e:
            print(f'--------------------------------------------------------')
            print(f' EXCEPTION ERROR, PUT initial record:  {urlx}')           
            print(f'--------------------------------------------------------')
            return False

        chunk_size = 1024

        with open(self.zip_with_path, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=chunk_size):
                fd.write(chunk)
        
        
        if os.path.isfile(self.zip_with_path):
            self.zip = self.zip_with_path
            return True

        return False

#---------------------------------------------
# getAllDocuments
#--------------------------------------------

    def getAllDocuments(self):
        data_set = {"name": self.host }
        self.json_data = json.dumps(data_set)

        urlx = f'http://{self.username}:{self.password}@{self.server}/ecapfiles/_all_docs?include_docs=true'
        print(f'{urlx}')
        try:           
           r = requests.get(urlx,data =self.json_data)
        except ConnectionError as e:
            print(f'--------------------------------------------------------')
            print(f' EXCEPTION ERROR, GET initial record:  {urlx}')           
            print(f'--------------------------------------------------------')
            return False

        data = r.json() 
        rows = data['rows']        
        for row in rows:
            doc = row['doc']
            nameFile = row['key']
            host = doc['name']
            if host == self.host:
                print(f'Get name = {nameFile},  hostname {host}')
                self.filename = nameFile
                status = self.getAttachment()
                if status == True:
                    print(f'unzip {self.zip_with_path}')
                    with zipfile.ZipFile(self.zip_with_path, 'r') as zip_ref:                
                        zip_ref.extractall(self.work_dir)
                    os.remove(self.zip_with_path)

                else:
                    print(f'couldnt get file')


    #    print(data)
    
        # parse data and return document list to fetch attachments.
        return True
