import time
import subprocess

def run_script(exename, loop_count, sleep_sec):
	count=0
	while count < loop_count:
		print("UnixBenchmark Loop... ", loop_count)
		subprocess.call("./Run.sh")
		localtime = time.localtime()
		result = time.strftime("%I:%M:%S %p", localtime)
        	print("***********************************************")
        	print("***********************************************")
		print("    ", result)
        	print("***********************************************")
        	print("***********************************************")
		count=count+1
		time.sleep(sleep_sec)
