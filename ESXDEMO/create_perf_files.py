import os
import time
import subprocess
import random
from datetime import datetime, timedelta
from  time import mktime
from run_script_func import run_exe

curday = ''

'''
**************************************************************
* create esx demo files.  - creates for yesterday
*  can be called by task scheduler for input into nightly load
*     duplicate  perf, merg,config
*     replace strings
*      for yesterday
**************************************************************
'''
#   appconfig:   paths and app settings
#

class  appconfig:
     def __init__(self, name):
        self.name=name
#        self.exe = 'C:\\tools\\duplicateperfandmerg\\bin\\DuplicatePerfAndMerg.exe' 
        self.exe = '.\\bin\\DuplicatePerfAndMerg.exe'
        self.outdir_perf='.\\output_perf'                 # intermediate output
#        self.outdir_config='.\\output_config'
#        self.outdir_merg='.\\output_merg'
#        self.finaldir_perf='.\\output_adjusted'

        self.indir_perf=".\\input_perf"
        self.indir_merg=".\\input_merg"
        self.indir_config=".\\input_config"

        self.finaldir_perf='C:\\TMP\\PERF'
        self.outdir_config='C:\\TMP\\PERF'
        self.outdir_merg='C:\\tmp\\merg'

'''
#   appduplicate class
#                build hostname list for output,  not very dynamic
'''

class  appduplicates:
     def __init__(self, name):
        self.name = name
        self.esxHosts = {
            'dc1_host1' : {
                'perf': 'rgesxi_2013Feb04_0000.perf',
                'merg': 'rgesxi_2021Apr16_1424.merg',
                'config': 'rgESXi_2020Mar27_1416_config.txt',
                'mhost': 'rgesxi',                    
            },
            'dc1_host2' : {
                'perf': 'rgesxi_2013Feb04_0000.perf',
                'merg': 'rgesxi_2021Apr16_1424.merg',
                'config': 'rgESXi_2020Mar27_1416_config.txt',
                'mhost': 'rgesxi',
            },
            'dc1_host3' : {
                'perf': 'vsphere01_2013Jan31_0000.perf',
                'merg': 'vsphere01_2021Apr14_0802.merg',
                'config': 'vsphere01_2020Feb19_0546_config.txt',
                'mhost': 'vsphere01',
            },
            'dc1_host4' : {
                'perf': 'esxi01_2013Jan29_0000.perf',
                'merg': 'esxi01_2021Apr16_1424.merg',
                'config': 'esxi01_2020Feb20_0546_config.txt',
                'mhost': 'esxi01',
            },
            'dc1_host5' : {
                'perf': 'rgesxi_2013Feb04_0000.perf',
                'merg': 'rgesxi_2021Apr16_1424.merg',
                'config': 'rgESXi_2020Mar27_1416_config.txt',
                'mhost': 'rgesxi',
            },
            'dc2_host1' : {
                'perf': 'rgesxi_2013Feb04_0000.perf',
                'merg': 'rgesxi_2021Apr16_1424.merg',
                'config': 'rgESXi_2020Mar27_1416_config.txt',
                'mhost': 'rgesxi',
            },
            'dc2_host2' : {
                'perf': 'rgesxi_2013Feb04_0000.perf',
                'merg': 'rgesxi_2021Apr16_1424.merg',
                'config': 'rgESXi_2020Mar27_1416_config.txt',
                'mhost': 'rgesxi',
            },
            'dc2_host3' : {
                'perf': 'rgesxi_2013Feb04_0000.perf',
                'merg': 'rgesxi_2021Apr16_1424.merg',
                'config': 'rgESXi_2020Mar27_1416_config.txt',
                'mhost': 'rgesxi',
            },
            'dc2_host4' : {
                'perf': 'rgesxi_2013Feb04_0000.perf',
                'merg': 'rgesxi_2021Apr16_1424.merg',
                'config': 'rgESXi_2020Mar27_1416_config.txt',
                'mhost': 'rgesxi',
            },
            'dc2_host5' : {
                'perf': 'vsphere01_2013Jan31_0000.perf',
                'merg': 'vsphere01_2021Apr14_0802.merg',
                'config': 'vsphere01_2020Feb19_0546_config.txt',
                'mhost': 'vsphere01',
            },
            'dc3_host1' : {
                'perf': 'esxi01_2013Jan29_0000.perf',
                'merg': 'esxi01_2021Apr16_1424.merg',
                'config': 'esxi01_2020Feb20_0546_config.txt',
                'mhost': 'esxi01',
            },
            'dc3_host2' : {
                'perf': 'rgesxi_2013Feb04_0000.perf',
                'merg': 'rgesxi_2021Apr16_1424.merg',
                'config': 'rgESXi_2020Mar27_1416_config.txt',
                'mhost': 'rgesxi',
            },
            'dc3_host3' : {
                'perf': 'vsphere01_2013Jan31_0000.perf',
                'merg': 'vsphere01_2021Apr14_0802.merg',
                'config': 'vsphere01_2020Feb19_0546_config.txt',
                'mhost': 'vsphere01',
            },
            'dc3_host4' : {
                'perf': 'vsphere01_2013Jan31_0000.perf',
                'merg': 'vsphere01_2021Apr14_0802.merg',
                'config': 'vsphere01_2020Feb19_0546_config.txt',
                'mhost': 'vsphere01',
            },
            'dc3_host5' : {
                'perf': 'rgesxi_2013Feb04_0000.perf',
                'merg': 'rgesxi_2021Apr16_1424.merg',
                'config': 'rgESXi_2020Mar27_1416_config.txt',
                'mhost': 'rgesxi',
            },
            'dc3_host6' : {
                'perf': 'vsphere01_2013Jan31_0000.perf',
                'merg': 'vsphere01_2021Apr14_0802.merg',
                'config': 'vsphere01_2020Feb19_0546_config.txt',
                'mhost': 'vsphere01',
            },
            'dc3_host7' : {
                'perf': 'rgesxi_2013Feb04_0000.perf',
                'merg': 'rgesxi_2021Apr16_1424.merg',
                'config': 'rgESXi_2020Mar27_1416_config.txt',
                'mhost': 'rgesxi',
            }
        }
        
    #    
    # Run_Duplicate_files:   duplicate the perf, merg and config
    #

def run_duplicate_files(app, curhost, host,time_start, time_end):

    in_perf = f"{app.indir_perf}\\{host['perf']}"
    in_merg = f"{app.indir_merg}\\{host['merg']}"
    in_config = f"{app.indir_config}\\{host['config']}"

    print("Run ", app.exe)
    print(" -host ", curhost)
    print(" -config ", in_config)
    print(" -merg ", in_merg)
    print(" -perf ", in_perf)
    run_exe(app.name, app.exe, app.outdir_perf, app.outdir_merg, app.outdir_config,time_start, time_end,\
            curhost, in_config, in_perf, in_merg, host['mhost'])
    pass

'''
  replace strings for the guests.
'''

def replace_guestnames(app, curhost, host, filedate):

    perf = f'{curhost}_{filedate}_0000.perf'
    mhost = host['mhost']

    final_perf = f"{app.finaldir_perf}\\{perf}"
    print (f'final perf: {final_perf}')
    intermediate_perf = f"{app.outdir_perf}\\{perf}"
    print (f'input perf: {intermediate_perf}')

    if mhost == 'esxi01':
        replace_esxi01(curhost, intermediate_perf, final_perf)   
    if mhost == 'rgesxi':
        replace_rgesx01(curhost, intermediate_perf, final_perf)   
    if mhost == 'vsphere01':
        replace_vsphere01(curhost, intermediate_perf, final_perf)  
    pass

'''
 replace_esxi01 : strings for esxi01 guest name replacement.
'''

def replace_esxi01(curhost, infile, outfile):
    exename = '.\\bin\\ReplaceString.exe'
    curhostdot = curhost.replace('_', '.') 
    command = []
    command.append("-infile")
    command.append(infile)
    command.append("-outfile")
    command.append(outfile)
    command.append('-replace')
    command.append(f'VMware vCenter Operations,{curhostdot}.g00')
    command.append('-replace')
    command.append(f'e01redhat6_x32,{curhostdot}.g01')
    command.append('-replace')
    command.append(f'e01redhat6_x64,{curhostdot}.g02')
    command.append('-replace')
    command.append(f'e01rhel55,{curhostdot}.g03')
    command.append('-replace')
    command.append(f'e01sles11,{curhostdot}.g04')
    command.append('-replace')
    command.append(f'e01sun10,{curhostdot}.g05')
    command.append('-replace')
    command.append(f'e01suse11,{curhostdot}.g06')
    command.append('-replace')
    command.append(f'e01sys01,{curhostdot}.g07')
    command.append('-replace')
    command.append(f'e01win2000,{curhostdot}.g08')
    command.append('-replace')
    command.append(f'sprsystem,{curhostdot}.g09')
    command.append('-replace')
    command.append(f'vCenter Mobile Access,{curhostdot}.g10')
    command.append('-replace')
    command.append(f'vkosystem,{curhostdot}.g11')
    command.append('-replace')
    command.append(f'C1-TaloranTemplate,{curhostdot}.g12')
    command.append('-replace')
    command.append(f'Thales Clone,{curhostdot}.g13')
    command.append('-replace')
    command.append(f'VMware Studio,{curhostdot}.g14')
    command.append('-replace')
    command.append(f'e01EVA,{curhostdot}.g15')
    command.append('-replace')
    command.append(f'e01fedora16,{curhostdot}.g16')
    command.append('-replace')
    command.append(f'e01.vm.eva.x64,{curhostdot}.g17')
    command.append('-replace')
    command.append(f'e01.vm.tm.x64,{curhostdot}.g18')
    command.append('-replace')
    command.append(f'e01solaris11,{curhostdot}.g19')
    command.append('-replace')
    command.append(f'e01ubuntu,{curhostdot}.g20')
    command.append('-replace')
    command.append(f'test_install_nojava,{curhostdot}.g21')
    command.append('-replace')
    command.append(f'e01ubuntu,{curhostdot}.g22')
    command.append('-replace')
    command.append(f'e01w2k8x64,{curhostdot}.g23')
    command.append('-replace')
    command.append(f'pawzdemo,{curhostdot}.g24')
    command.append('-replace')
    command.append(f'pawzv10test_esx,{curhostdot}.g25')
    command.append('-replace')
    command.append(f'pawzv10test_tm,{curhostdot}.g26')
    command.append('-replace')
    command.append(f'vSolaris11,{curhostdot}.g27')
    command.append('-replace')
    command.append(f'vTransactionMonitor,{curhostdot}.g27')   # 61

    subprocess.run([exename, f'{command[0]}', f'{command[1]}',\
        f'{command[2]}', f'{command[3]}', f'{command[4]}', f'{command[5]}',\
        f'{command[6]}', f'{command[7]}', f'{command[8]}', f'{command[9]}', \
        f'{command[10]}', f'{command[11]}', f'{command[12]}',f'{command[13]}',\
        f'{command[14]}', f'{command[15]}', f'{command[16]}',f'{command[17]}', \
        f'{command[18]}', f'{command[19]}', f'{command[20]}',f'{command[21]}',\
        f'{command[22]}', f'{command[23]}',f'{command[24]}',f'{command[25]}',\
        f'{command[26]}', f'{command[27]}',f'{command[28]}',f'{command[29]}',\
        f'{command[30]}', f'{command[31]}',f'{command[32]}', f'{command[33]}'\
        f'{command[34]}', f'{command[35]}', f'{command[36]}',f'{command[37]}',\
        f'{command[38]}', f'{command[39]}', f'{command[40]}',f'{command[41]}',\
        f'{command[42]}', f'{command[43]}',f'{command[44]}',f'{command[45]}',\
        f'{command[46]}', f'{command[47]}',f'{command[48]}',f'{command[49]}',\
        f'{command[50]}', f'{command[51]}',f'{command[52]}', f'{command[53]}'\
        f'{command[54]}', f'{command[55]}', f'{command[56]}',f'{command[57]}',\
        f'{command[58]}', f'{command[59]}', f'{command[60]}',f'{command[61]}'])
    pass

'''
 replace_rgesxi01 : strings for esxi01 guest name replacement.
'''

def replace_rgesx01(curhost, infile, outfile):
 
    exename = '.\\bin\\ReplaceString.exe'
    curhostdot = curhost.replace('_', '.') 
    command = []
    command.append("-infile")
    command.append(infile)
    command.append("-outfile")
    command.append(outfile)
    command.append('-replace')
    command.append(f'rgPAWZ,{curhostdot}.g00')
    command.append('-replace')
    command.append(f'vAgua,{curhostdot}.g01')
    command.append('-replace')
    command.append(f'vCoreAP1,{curhostdot}.g02')
    command.append('-replace')
    command.append(f'vCoreDB1,{curhostdot}.g03')
    command.append('-replace')
    command.append(f'vEuclid,{curhostdot}.g04')
    command.append('-replace')
    command.append(f'vMoto,{curhostdot}.g05')
    command.append('-replace')
    command.append(f'vNoir,{curhostdot}.g06')
    command.append('-replace')
    command.append(f'vSolaris10,{curhostdot}.g07')
    command.append('-replace')
    command.append(f'vThales,{curhostdot}.g08')
    command.append('-replace')
    command.append(f'vTmMonitor,{curhostdot}.g09')  # 23

    subprocess.run([exename, f'{command[0]}', f'{command[1]}',\
        f'{command[2]}', f'{command[3]}', f'{command[4]}', f'{command[5]}',\
        f'{command[6]}', f'{command[7]}', f'{command[8]}', f'{command[9]}', \
        f'{command[10]}', f'{command[11]}', f'{command[12]}',f'{command[13]}',\
        f'{command[14]}', f'{command[15]}', f'{command[16]}',f'{command[17]}', \
        f'{command[18]}', f'{command[19]}', f'{command[20]}',f'{command[21]}', \
        f'{command[22]}', f'{command[23]}'])
    pass

'''
 replace_vsphere01 : strings for vpshere01 guest name replacement.
'''

def replace_vsphere01(curhost, infile, outfile):
    exename = '.\\bin\\ReplaceString.exe'
    curhostdot = curhost.replace('_', '.') 
    command = []

    command.append("-infile")
    command.append(infile)
    command.append("-outfile")
    command.append(outfile)
    command.append('-replace')
    command.append(f'oracleLinux64,{curhostdot}.g00')
    command.append('-replace')
    command.append(f'pawzESX,{curhostdot}.g01')
    command.append('-replace')
    command.append(f'pawzV92,{curhostdot}.g02')
    command.append('-replace')
    command.append(f'testsql2012,{curhostdot}.g03')            
    command.append('-replace')
    command.append(f'testsql2012,{curhostdot}.g04')
    command.append('-replace')
    command.append(f'ubuntu64,{curhostdot}.g05')
    command.append('-replace')
    command.append(f'vs01w2k3r2x32us,{curhostdot}.g06')
    command.append('-replace')
    command.append(f'vs01w2k3x6401,{curhostdot}.g07')
    command.append('-replace')
    command.append(f'staging1,{curhostdot}.g09')
    command.append('-replace')
    command.append(f'staging2,{curhostdot}.g10')
    command.append('-replace')
    command.append(f'staging3,{curhostdot}.g11')
    command.append('-replace')
    command.append(f'staging,{curhostdot}.g12')
    command.append('-replace')
    command.append(f'vs01Win7,{curhostdot}.g13')
    command.append('-replace')
    command.append(f'vs01w2k3x6403_32,{curhostdot}.g08')  # 31

    subprocess.run([exename, f'{command[0]}', f'{command[1]}',\
        f'{command[2]}', f'{command[3]}', f'{command[4]}', f'{command[5]}',\
        f'{command[6]}', f'{command[7]}', f'{command[8]}', f'{command[9]}', \
        f'{command[10]}', f'{command[11]}', f'{command[12]}',f'{command[13]}',\
        f'{command[14]}', f'{command[15]}', f'{command[16]}',f'{command[17]}', \
        f'{command[18]}', f'{command[19]}', f'{command[20]}',f'{command[21]}', \
        f'{command[22]}', f'{command[23]}',f'{command[24]}',f'{command[25]}', \
        f'{command[26]}', f'{command[27]}',f'{command[28]}',f'{command[29]}', \
        f'{command[30]}', f'{command[31]}'])
    pass

'''
--------------------------------------------
main
--------------------------------------------
'''

if (__name__== '__main__'):
    print("main")
#    os.chdir("./esxdemo")
    app = appconfig('duplicateperf')
    dup = appduplicates('appdup')

    localtime = time.localtime()
    d = datetime.today() - timedelta(days=1)

    curday = datetime.strftime(d, "%d-%b-%Y")
    filedate = datetime.strftime(d, "%Y%b%d")

    starttime = f'{curday}'                     # just full day date
    endtime = f'{curday}'

    print (f'esx demo, create perf files... {curday}')

    for curhost, host in dup.esxHosts.items():
        print (f"{curhost} : {host['perf']}")

        run_duplicate_files(app, curhost, host, starttime, endtime)
        replace_guestnames(app, curhost, host, filedate)
        
    print('done')
