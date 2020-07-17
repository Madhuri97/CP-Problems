# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2
# 7, 41
def isPrime(n):
	if n > 1:
		for i in range(2,n):
			if(n%1 == 0 and n%i == 0):
				return False
		return True
	return False

def fun_isadditive(n):
	s = 0
	if(isPrime(n)):
		while(n > 0): #T T T 
			r = n%10  #0 0 0
			s = s + r #0 0 0
			n = n//10 #0 5 2
		if(isPrime(s)): #
			return True
		return False

def fun_nth_additive_prime(n):
	li = []
	for i in range(10000):
		if fun_isadditive(i):
			return li[n]