# mv1.py:   get a list of files from a directory
# rename with date of creation.
#----------------------------------------------------------
import os
import time
from os import listdir
from os.path import  isfile,join
from datetime import datetime

#now = datetime.now()
#current_dm = now.strftime("20%y%m%d")

mypath = 'C:\\paul\\tmp'
ofiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
filecount = 1

for cfile in ofiles:
    fp_cfile1 = f"{mypath}\\{cfile}"
    created = os.path.getmtime(fp_cfile1)
    current_dm = datetime.fromtimestamp(created).strftime("20%y%m%d")    
    fx = f'_xh_{0}.jpg'.format(current_dm)
    newfile = f"{filecount:05d}_xh_{current_dm}.jpg"
    print(f"File: {cfile}  Date created: {time.ctime(created)}")
    msg = f"Rename:({cfile},{newfile})"
    filecount = filecount + 1   
    fp_newfile = f"{mypath}\\{newfile}" 
    os.rename(fp_cfile1, fp_newfile)
    print(msg)

