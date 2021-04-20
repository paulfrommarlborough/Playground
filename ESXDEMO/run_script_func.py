import time
import subprocess
import random

##cmdline = f'-start {starttime} -end {endtime} -host {curhost} -outdir {outdir} -perf {input_file}'

def run_exe(strName, exename, outdir_perf, outdir_merg, outdir_config, startime, endtime, curhost, inputfile_config, inputfile_perf, inputfile_merg, mhost_name):
		print("RunScript call... ", exename)

		subprocess.run([exename, '-start', startime,'-end',endtime,'-host', curhost,'-outdir_perf', outdir_perf, \
			'-merg', inputfile_merg, '-mhost', mhost_name, '-outdir_merg', outdir_merg, \
			'-perf', inputfile_perf, '-config', inputfile_config, '-outdir_config', outdir_config] )
		localtime = time.localtime()
		result = time.strftime("%I:%M:%S %p", localtime)
		print("***********************************************")
		print("***********************************************")
		print("    ", strName, result)
		print("***********************************************")
		print("***********************************************")
	