# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.

# [[9,12]; [8]; [16,8]]
def fun_hasnoprimes(l):
	for i in l:  #[9,12]
		for j in i: #9
			if(j > 1): #T
				for k in range(2, len(i)):
					if(j%k == 0): 
						return False
	return True

