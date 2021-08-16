import requests, zipfile, io

# urlx = 'http://admin:pawz1@localhost:5984/pawzfiles/Palladium_2021Mar14/ecp_Palladium_2021Mar14.zip'
urlx = 'http://admin:pawz1@192.168.1.167:5984/pawzfiles/ecapdev_2021Apr07/ecp_ecapdev_2021Apr07.zip'

r = requests.get(urlx, stream=True)
print('zipfile...')
z= zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()
