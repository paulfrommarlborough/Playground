set pwd=%1
python CouchGetMain.py --input-file input.json --workdir C:\tools\couch\nightly --username admin --password %pwd% --server 192.168.1.167:5984 --yesterday

rem python CouchGetMain.py  --host rgESXi1 --workdir C:\tools\couch\couchget --username admin --password %pwd% --server 192.168.1.167:5984 --date 2021sep01
rem python CouchGetMain.py  --host rgESXi --workdir C:\tools\couch\couchget --username admin --password %pwd% --server 192.168.1.167:5984 --date 2021sep01
