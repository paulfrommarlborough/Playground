#!/usr/bin/bash

# customize for loading the cpc data file  

HOME="/home/douglas/couch/linux/AddFiles"
PERFCAP_ROOT="/data/perfcap"
COUCH_SERVER="192.168.1.167"

# add  YESTERDAY files in the datadirectory  to couchdb  for nodes (specified in input file)

python3 CouchAddMain.py --yesterday  --input $HOME/input.json  --os linux --ip 192.168.0.75  \
  --workdir $HOME --username admin --password pawz1 --server $COUCH_SERVER:5984 --rootdir $PERFCAP_ROOT

