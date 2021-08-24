# python to get all databases from couch.

# curl -X GET http://admin:pawz1@192.168.5.158:5984/_all_dbs
# curl -X GET http://admin:pawz1@192.168.5.158:5984/pawzfiles/_all_docs

import couchdb
import os
import pandas as pd
import io
import zipfile

couch = couchdb.Server('http://localhost:5984')
couch.resource.credentials = ('admin', 'pawz1')
db = couch['pawzfiles']
rows = db.view('_all_docs', include_docs=True)
print('rows---')
print (rows)

#for row in rows:
#    nameFile = row['_attachments'].keys()[0]
#    print(f'attachment {nameFile}')
print ('rows done---')

data_doc = [row['doc'] for row in rows]

for dd in data_doc:    
    nameFile = dd['_attachments'].keys()
    n = list(nameFile)
    attachname = n[0]
    if 'Palladium' in attachname:
        continue
    if 'ecpm' in attachname:
        continue
    if 'esxi01.zip' in attachname:
        continue
    if 'esxi02.zip' in attachname:
        continue
    

    print(f'attachment {n[0]}')
    attachment = db.get_attachment(dd, n[0]).read()
    current_folder = os.getcwd()
    tempfile = os.path.join(current_folder, n[0])

    z = zipfile.ZipFile(io.BytesIO(attachment))
    z.extractall()                                 # extracts here


print('data---')
print(data_doc)

print('---------------------------------------')
data1 = [row['id'] for row in rows]
print(data1)

x = len(data1)
print(x)

for i  in range(x):
    print(f" {i}:  {data1[i]}")

print('-----')



#doc = db[doc_id]
#nameFile = doc['_attachments'].keys()[0]
#attachment = db.get_attachment(doc, nameFile).read()
#current_folder = os.getcwd()
#tempfile = os.path.join(current_folder, nameFile)
#f= open(tempfile, 'w')
#f.write(attachment)
#f.close()    