set pwd=%1
python CouchGetMain.py  --host rgESXi1 --workdir C:\tools\couch\couchget --username admin --password %pwd% --server 192.168.1.167:5984 --yesterday
python CouchGetMain.py  --host rgESXi --workdir C:\tools\couch\couchget --username admin --password %pwd% --server 192.168.1.167:5984 --yesterday
python CouchGetMain.py  --host esxi01 --workdir C:\tools\couch\couchget --username admin --password %pwd% --server 192.168.1.167:5984 --yesterday
python CouchGetMain.py  --host esxi02 --workdir C:\tools\couch\couchget --username admin --password %pwd% --server 192.168.1.167:5984 --yesterday
python CouchGetMain.py  --host vsphere01 --workdir C:\tools\couch\couchget --username admin --password %pwd% --server 192.168.1.167:5984 --yesterday


rem python CouchGetMain.py  --host rgESXi1 --workdir C:\tools\couch\couchget --username admin --password %pwd% --date 2021aug27 --server 192.168.1.167:5984
rem python CouchGetMain.py  --host rgESXi --workdir C:\tools\couch\couchget --username admin --password %pwd% --date 2021aug27 --server 192.168.1.167:5984
