rem  get cpc data files for ESX systems on the in-accessable 192.168.0.n network.
rem  data files are loaded to couch on a system in the 192.168.1.n network.
rem
rem  Assumes the VPN link is Up.
rem     must be scheduled after the schedule to load couch on 1.167
rem

pwd=%1

python CouchGetMain.py  --host rgESXi1 --workdir C:\tools\couch\couchget --username admin --password %pwd% --server 192.168.1.167:5984 --yesterday
python CouchGetMain.py  --host rgESXi --workdir C:\tools\couch\couchget --username admin --password %pwd% --server 192.168.1.167:5984 --yesterday

copy/Y *.cpc-* C:\"Program Files"\Perfcap\ecap\monitor\data_vmware\

del/Q *.cpc-*