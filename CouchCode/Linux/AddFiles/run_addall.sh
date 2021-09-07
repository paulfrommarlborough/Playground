#!/usr/bin/bash
#
# add all files in the datadirectory  to couchdb  for node (specified in input file)
# the --rootdir is the install directory of unix system.  ./data will have the data files.
#
HOME="/home/douglas/couch/linux/AddFiles"
PERFCAP_ROOT="/data/perfcap"
COUCH_SERVER="192.168.1.167"

python3 CouchAddMain.py --all --input $HOME/input.json --workdir $HOME --username admin --password pawz1 \
  --server $COUCH_SERVER:5984 --rootdir $PERFCAP_ROOT 

