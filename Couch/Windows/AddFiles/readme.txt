CouchAdd Project:                                               24-aug-2021
     
     Add CPC data files from WINDOWS, ESX, MSSQL into CouchDB after zipping

     Run nightly in task scheduler on windows to add yesterdays data.

     Database entries have keys for   date, name, os, ipaddress

     Run using an input json   file

     Note: need to add --user   --password options...

#----------------------------------------------
# Launch Options...
#----------------------------------------------

"args": ["--host", "palladium", "--os", "WINDOWS", "--ip", "192.168.5.158", "--workdir", "C:\\tools\\TMP","--input", "C:\\tools\\TMP\\input.json"  ] 

# specific date
"args": ["--host", "palladium", "--os", "WINDOWS", "--ip", "192.168.5.158", "--workdir", "C:\\tools\\TMP", "--date", "2021Aug20", "--input", "C:\\tools\\TMP\\input.json"  ] 

# specific date
"args": ["--host", "palladium", "--os", "WINDOWS", "--ip", "192.168.5.158", "--workdir", "C:\\tools\\TMP", "--date", "2021Aug20" ]

# ALL FILES
"args": ["--all", "-username", "admin", "--password", "pawz1", "--workdir", "C:\\tools\\Couch\\Nightly","--input", "C:\\tools\\Couch\\NiGHTLY\\input.json"  ] 

# nightly
"args": [ "--workdir", "C:\\tools\\Couch\\Nightly","--input", "C:\\tools\\Couch\\Nightly\\input.json"  ] 

#----------------------------------------------
# Curl Notes
# add with json: need to write json, and then run curl
#  curl to add entry 
#     curl -X PUT http://admin:pawz1@127.0.0.1:5984/ecapfiles/palladium_2021apr01 -d @example.json -H "Content-type: application/json"
#  curl to attach file
#     curl -vX PUT http://admin:pawz1@127.0.0.1:5984/ecapfiles/palladium_2021apr01/ecp_Palladium_2021Apr01.zip?rev=11-49c188b2f6b009288046e4e80c305b55 --data-binary @ecp_Palladium_2021Apr01.zip -H "Content-Type: application/zip"

