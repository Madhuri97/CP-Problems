# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.

# [[12,4,6]; [8,12,14]; [6,18]]
def isprime(n):
	for i in range(2,n):
		if(n%1 == 0 and n%i == 0):
			return False
		return True
def fun_hasnoprimes(l):
	# if(len(l) > 1): #3>1
		# for i in l:  #[9,12]
		# 	for j in i: #9
		# 		if(j > 1): #T
		# 			for k in range(2, len(i)):
		# 				if(j%k == 0): 
							# return False
	if(len(l) > 1):
		t = [j for sub in l for j in sub]
		for i in t:
			if(isprime(i)):
				return False
	return False

