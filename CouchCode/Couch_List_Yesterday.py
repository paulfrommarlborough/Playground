import requests, io, json
import time

from requests.exceptions import ConnectionError
from datetime import datetime, timedelta
from  time import mktime


''' Take Known Couch Databases and see if we have the nightly download for yesterday
''  we need to have entry for NO DATA.
''  list the couch files at the end
'''

localtime = time.localtime()
d = datetime.today() - timedelta(days=1)
filedate = datetime.strftime(d, "%Y%b%d")

node_fail_list = []

yesterdays_files = []

url_1 = { 'name':'palladium', 'url':'http://admin:pawz1@192.168.5.158:5984/pawzfiles/_all_docs' }
url_2 = { 'name':'ecapdev',  'url':'http://admin:pawz1@192.168.1.167:5984/pawzfiles/_all_docs' }
url_3 = { 'name':'vcoreap64', 'url':'http://admin:pawz1@192.168.0.192:5984/pawzfiles/_all_docs'}
url_4 = { 'name':'vcoredb64', 'url':'http://admin:pawz1@192.168.0.193:5984/pawzfiles/_all_docs' }

node_fail_list.append('palladium')
node_fail_list.append('ecapdev')
node_fail_list.append('vcoreap64')
node_fail_list.append('vcoredb64')



url_dict = {  
        0: url_1,
        1: url_2,
        2: url_3,
        3: url_4        
}

# for each entry  query the files and see if we have the any for the last day

for i in range(len(url_dict)):
    urlx = url_dict[i]['url']
    url_hostname = url_dict[i]['name']

    
    try:
        r = requests.get(urlx, stream=True)
    except ConnectionError as e:
        print(f'--------------------------------------------------------')
        print(f' Request:  {url_hostname}, *** EXCEPTION ERROR. {urlx}')
        #print(e)
        print(f'--------------------------------------------------------')
        r = None

    if r:
        contentJson= r.json()
        total_rows = int(contentJson["total_rows"])
        offset = contentJson["offset"]
        rows = contentJson["rows"]
        
        print(f'--------------------------------------------------------')
        print(f' Request:  {url_hostname}, Status: {r.status_code},   Data Files: {total_rows}' ) 
        print(f'--------------------------------------------------------')
        
        for i in range(total_rows):
            currentid = rows[i]['id']
        #       print(f"id:  {rows[i]['id']}    key:   {rows[i]['key']} ")
            if filedate in currentid:                
                x = f" {url_hostname}_{currentid}"
                if url_hostname in node_fail_list:                    
                   node_fail_list.remove(url_hostname)
                yesterdays_files.append(x)
print('--------------------------------------------------')
#print(f'Yesterdays Files {yesterdays_files}')
print('Performance data files loaded into Couch for yesterday: ')
for item in yesterdays_files:
    print(f'  File:  {item}')

print('-------------------------------------------------')
print('Systems with missing Couch for yesterday: ')
for item1 in node_fail_list:
    print(f'  System:  {item1}')
   

print('--------------------------------------------------')
print('Done')

