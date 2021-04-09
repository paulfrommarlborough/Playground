
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
current_dm = now.strftime("20%y%d%m")
print("Current Time =", current_dm)

fx = '_xh_{0}.jpg'.format(current_dm)
#newfile = f"_xh_{0}.jpg" % current_dm
print (fx) 

cfile = '1'
ofiles = [ '1','2','3','4']
filecount = 1
for cfile in ofiles:
     #  fx = f'_xh_{0}.jpg'.format(current_dm)

    newfile = f"{filecount:05d}_xh_{current_dm}_.jpg"
    print(newfile)
    filecount = filecount + 1
