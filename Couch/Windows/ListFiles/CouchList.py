# listfiles.py
#
#    for the known couch servers,  list the data files for yesterday.
#--------------------------------------------------------------------


import requests, io, json
import time

from requests.exceptions import ConnectionError
from datetime import datetime, timedelta
from  time import mktime

#curl -X GET http://admin:pass@192.168.1.167:5984/ecapfiles/_all_docs

localtime = time.localtime()
d = datetime.today() - timedelta(days=1)
filedate = datetime.strftime(d, "%Y%b%d")
filedate = filedate.lower()

yesterdays_files = []

url_1 = { 'name':'ecapdev',  'url':'http://admin:stub@192.168.1.167:5984/ecapfiles/_all_docs' }
url_2 = { 'name':'vcoreap64', 'url':'http://admin:stub@192.168.0.192:5984/ecapfiles/_all_docs'}
url_3 = { 'name':'vcoredb64', 'url':'http://admin:stub@192.168.0.193:5984/ecapfiles/_all_docs' }

url_dict = {  
        0: url_1,
        1: url_2,
        2: url_3
}

for i in range(len(url_dict)):
    urlx = url_dict[i]['url']
    url_hostname = url_dict[i]['name']

    print('--------------------------------------------------------')
    try:
        r = requests.get(urlx, stream=True)
    except ConnectionError as e:
        #print(e)
        print(f'exception connectioning...{urlx}')
        r = None

    if r:
        print(f'Request: {urlx}')
        print(f'Request.status: {r.status_code}')


        contentJson= r.json()
        total_rows = int(contentJson["total_rows"])
        offset = contentJson["offset"]
        rows = contentJson["rows"]
        print(f'total rows:     {total_rows}   offset: {offset}')
        for i in range(total_rows):
            currentid = rows[i]['id']
#            print(f"id:  {rows[i]['id']}    key:   {rows[i]['key']} ")
#            print(f' filedate = {filedate}   currentid = {currentid}')
            if filedate in currentid:                
                x = f" {url_hostname}_{currentid}"
                yesterdays_files.append(x)
print('--------------------------------------------------')
print('--------------------------------------------------')
print('Done')
print(f'Yesterdays Files {yesterdays_files}')

#for i in range(len(url_dict)):
#    print(url_dict[i]['url'])
   
    
