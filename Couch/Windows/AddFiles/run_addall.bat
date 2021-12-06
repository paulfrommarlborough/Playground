set root="C:\tools\CouchCode\Windows\AddFiles"
set password=%1
python CouchAddMain.py --all --input %root%\\input.json --workdir %root% --username admin --password %password% --server 192.168.5.158:5984