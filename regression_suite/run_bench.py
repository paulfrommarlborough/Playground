import os
import time
import random

from prime_func import compute_primes
from run_script_func import run_script

def run_primes(strCurDir):
	os.chdir(strCurDir)

	MAX_PRIME_CHECK = 1000000
#	MAX_PRIME_CHECK = random.randint(1000, 1000000000)
	NTIME = random.randrange(1)
	NLOOPS = random.randrange(20)
	if NTIME == 0:
		NTIME = 1
	if NLOOPS == 0:
		NLOOPS = 1


	localtime = time.localtime()
	starttime = time.time()
	result = time.strftime("%I:%M:%S %p", localtime)

	print("PRIMES.LOOPS MAX.. ", NLOOPS)
	for i in range(NLOOPS):
		print("PRIMES... ", i)
		compute_primes(MAX_PRIME_CHECK)
		if NTIME > 0:
			nsec = random.randrange(NTIME)
			time.sleep(nsec)
	
	endtime = time.time()
	localtimef = time.localtime()
	resultf = time.strftime("%I:%M:%S %p", localtimef)
	run_secs = endtime - starttime 
	print("PRIMES FINISHED ", resultf, "  Secs ", run_secs)

def run_matrix(strCurDir):
	os.chdir(strCurDir)
	NTIME=random.randrange(1)
	NLOOPS=random.randrange(10)
	if NTIME == 0:
		NTIME = 1
	if NLOOPS == 0:
		NLOOPS = 1


	localtime = time.localtime()
	starttime = time.time()
	result = time.strftime("%I:%M:%S %p", localtime)

	os.chdir("./matrix_windows")
	print("MATRIX...", result)
	run_script("MATRIX", "Run.Bat", NLOOPS, NTIME)

def run_unixbench(strCurDir):
	os.chdir(strCurDir)
	NTIME=random.randrange(1)
	NLOOPS=random.randrange(1)
	if NTIME == 0:
		NTIME = 1
	if NLOOPS == 0:
		NLOOPS = 1

	localtime = time.localtime()
	starttime = time.time()
	result = time.strftime("%I:%M:%S %p", localtime)
	print("UNIXBENCH...", result)
	os.chdir("./unixbench-4.0.1")
	run_script("UNIXBENCH", "Run.Bat", NLOOPS, NTIME )


def run_rijndael(strCurDir):
	os.chdir(strCurDir)
	NTIME=random.randrange(1)
	NLOOPS=random.randrange(10)
	if NTIME == 0:
		NTIME = 1
	if NLOOPS == 0:
		NLOOPS = 1

	localtime = time.localtime()
	starttime = time.time()
	result = time.strftime("%I:%M:%S %p", localtime)
	print("RIJNDAEL...", result)

	os.chdir("./rijn_Windows")
	run_script("RIJNDAEL", "Run.bat", NLOOPS, NTIME )

def run_bonnie(strCurDir):
	os.chdir(strCurDir)
	NTIME=random.randrange(1)
	NLOOPS=random.randrange(10)
	if NTIME == 0:
		NTIME = 1
	if NLOOPS == 0:
		NLOOPS = 1

	localtime = time.localtime()
	starttime = time.time()
	result = time.strftime("%I:%M:%S %p", localtime)
	print("BONNIE...", result)
	os.chdir("./bonnie_windows")
	run_script("BONNIE", "Run.bat", NLOOPS, NTIME )

def run_takeabreak(strCurDir):
	os.chdir(strCurDir)
	NTIME=random.randrange(3000)
	print("TAKE_A_BREAK: ", NTIME)
	time.sleep(NTIME)

if __name__== "__main__":
	print("Main Run benchmark...")

	strCurDir = os.getcwd()
	print("CurrentDir = " , strCurDir)
	random.seed(time.time())	

	""" you are guarenteed all tests.  - """

	while True:
# 		run_suite = [0,0,2,2,3,3,3,4]
		run_suite = [0,0,0,2,3,3,3,4]


		random.shuffle(run_suite)

		while run_suite:
			nfunc = run_suite.pop()

			print ("Function: ", nfunc)
			if nfunc == 0:
				run_primes(strCurDir)
			elif nfunc == 1:
				run_unixbench(strCurDir)
			elif nfunc == 2:
				run_matrix(strCurDir)
			elif nfunc == 3:
				run_rijndael(strCurDir);
			elif nfunc == 4:
				run_takeabreak(strCurDir);
			elif nfunc == 5:
				run_bonnie(strCurDir);
			else:
				print("UNKNOWN: ", nfunc)

