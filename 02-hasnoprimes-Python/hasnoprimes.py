# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.

# [[12,4,6]; [8,12,14]; [6,18]]
def isprime(n):
	for i in range(2,n):
		if(n%1 == 0 and n%i == 0):
			return False
		return True

def fun_hasnoprimes(l):
	
	t = [j for sub in l for j in sub]
	for i in t:
		if(isprime(i)):
			return False
		return True
	

