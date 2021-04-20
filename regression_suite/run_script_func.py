import time
import subprocess
import random

def run_script(strName, exename, loop_count, max_sleep_sec):
	count=0
	while count < loop_count:
		print("RunScript Loop... ", count)
		print("RunScript LoopMAX... ", loop_count)
		print("RunScript call... ", exename)
		subprocess.call(exename)
		localtime = time.localtime()
		result = time.strftime("%I:%M:%S %p", localtime)
		print("***********************************************")
		print("***********************************************")
		print("    ", strName, result)
		print("***********************************************")
		print("***********************************************")
		count=count+1
		sleep_sec = random.randrange(max_sleep_sec)
		print("RunScript: sleep... ", strName, sleep_sec)
		time.sleep(sleep_sec)
