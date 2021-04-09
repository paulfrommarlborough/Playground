# mv1.py:   get a list of files from a directory
# rename with date of creation. 
#----------------------------------------------------------
import os
import time
from os import listdir
from os.path import  isfile,join
from datetime import datetime

mypath = 'C:\\paul\\temp'
ofiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
filecount = 10

for cfile in ofiles:
    fp_cfile1 = f"{mypath}\\{cfile}"
    created = os.path.getmtime(fp_cfile1)
    current_dm = datetime.fromtimestamp(created).strftime("20%y%m%d") 
    newfile = f"xh_{filecount:05d}_{current_dm}.jpg"
    print(f"File: {cfile}  Date created: {time.ctime(created)}")
    filecount = filecount + 1   
    fp_newfile = f"{mypath}\\{newfile}" 
    msg = f"Rename:({cfile},{newfile})"
    print(msg)
    os.rename(fp_cfile1, fp_newfile)

