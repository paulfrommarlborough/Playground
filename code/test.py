import pycurl

from io import StringIO


print ('test pycurl')

buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.USERPWD, 'admin:pawz1')
c.setopt(c.PORT, 5984)
c.setopt(c.HTTPGET, 1)
c.setopt(c.URL, 'http://192.168.5.158//pawzfiles/Palladium_2021Mar15/ecp_Palladium_2021Mar15.zip')
c.setopt(c.CUSTOMREQUEST, 'GET')

c.perform()
c.close()

body = buffer.getvalue()
print ('body: ')
print (body)

hostname='192.168.5.158'
username='admin'
pwd='pawz1'
port='5984'
date='2021mar10'


