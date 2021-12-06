#!/usr/bin/bash

HOME="/home/douglas/couch/linux/AddFiles"
PERFCAP_ROOT="/data/perfcap"
COUCH_SERVER="192.168.1.167"
PASSWORD="$1"
# add  YESTERDAY files in the datadirectory  to couchdb  for nodes (specified in input file)
#
python3 CouchAddMain.py --yesterday --input $HOME/input.json --workdir $HOME --username admin --password $1 \
--server $COUCH_SERVER:5984 --rootdir $PERFCAP_ROOT 

