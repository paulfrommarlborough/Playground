set root="C:\tools\CouchCode\Windows\AddFiles"
set passwd="%1"
python CouchAddMain.py --yesterday --host PALLADIUM   --os WINDOWS --ip 192.168.5.158 --workdir %root% --username admin --password %passwd% --server 192.168.5.158:5984