import math

def compute_primes( LIMIT):
	count = 3
	while count < LIMIT:
		isprime = True
        
        	for x in range(2, int(math.sqrt(count) + 1)):
            		if count % x == 0: 
                		isprime = False
                	break
        
        	if isprime:
            		print count
		count += 1
