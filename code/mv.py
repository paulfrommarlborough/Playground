# get a list of files from a directory
import os
from os import listdir
from os.path import  isfile,join
from datetime import datetime

now = datetime.now()

current_dm = now.strftime("20%y%m%d")

mypath = 'C:\\paul\\temp'
ofiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
filecount = 73
for cfile in ofiles:
    fx = f'_xh_{0}.jpg'.format(current_dm)
    newfile = f"{filecount:05d}_xh_{current_dm}_.jpg"
    msg = f"os.rename({cfile},{newfile})"
    filecount = filecount + 1
    fp_cfile = f"{mypath}\\{cfile}"
    fp_newfile = f"{mypath}\\{newfile}" 
    os.rename(fp_cfile, fp_newfile)
    print(msg)

#for filecount=0; filecount < ofiles.count; filecount++:
#    fname = f"000_{ofiles[filecount]}"
 #   print(fname)