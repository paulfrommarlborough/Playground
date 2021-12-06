#!/usr/bin/bash
#
# Customize Entries to fetch data from couchdb for a node / nodes  for a date/dates
WORKDIR="`pwd`"
COUCH_SERVER="192.168.1.167"
PASSWORD="$1"
python3 CouchGetMain.py --host rgESXi1 --workdir $WORKDIR --username admin --password $PASSWORD --server $COUCH_SERVER:5984 --yesterday
