import math
import time

""" compute  pries """

def compute_primes( LIMIT):
	count = 3000000
	print("COMPUTE PRIMES.. ", LIMIT)
	while count < LIMIT:
		isprime = True
       		 
		for x in range(2, int(math.sqrt(count) + 1)):
            		if count % x == 0: 
                		isprime = False
		break
	print(count)        
	count += 1
