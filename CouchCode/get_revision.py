import requests, io, json
import time

#  1:  Inputs   hostname, ip, os, date, filename.zip
# 
#  2:  Add Record:  hostname, ip, op, os, date
#
#  3:  get _rev
#
#  4:  attach file to _rev
#

from requests.exceptions import ConnectionError
from datetime import datetime, timedelta
from  time import mktime

#curl -X GET http://admin:pawz1@127.0.0.1:5984/ecapfiles/palladium_2021apr01?revs_info=true


input_array = []


url_list = []

url_1 = { 'name':'palladium', 'url':'http://admin:pawz1@192.168.5.158:5984/ecapfiles/palladium_2021apr01?revs_info=true' }

url_dict = {  
        0: url_1
}


urlx = url_dict[0]['url']
url_hostname = url_dict[0]['name']

print(f'URL: {urlx}')
try:
    r = requests.get(urlx, stream=True)
except ConnectionError as e:
    print(f'--------------------------------------------------------')
    print(f' Request:  {url_hostname}, *** EXCEPTION ERROR. {urlx}')
    print(e)
    print(f'--------------------------------------------------------')
    r = None  

if r:
    contentJson= r.json()
    record_rev = contentJson["_rev"]
    record_id = contentJson["_id"]
    record_date = contentJson["date"]
    record_name = contentJson["name"]
    record_ip = contentJson["ip"]
    record_os = contentJson["os"]

    print(f'---------------------------------------------------------------------')
    print(f' Request:  {url_hostname}, _id: {record_id},   Data _Rev: {record_rev},  Date {record_date}' ) 
    print(f'---------------------------------------------------------------------')
  
