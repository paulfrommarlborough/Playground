

from prime_func import compute_primes
from run_script_func import run_script

if __name__== "__main__":
	print("Main Run benchmark...")
        print("compute some primes...")
	compute_primes(100)

        print("run_unix benckmark...")
	run_script("./Run.sh", 10, 5)

