# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def isPrime(n):
	for i in range(2,n):
		if(n%1 == 0 and n%i == 0):
			return False
		return True

def fun_isadditive(n):
	s = 0
	if(isPrime(n)):
		while(n > 0):
			r = n%10
			s = s + r
			n = n//10
		if(isPrime(s)):
			return True
		return False

def fun_nth_additive_prime(n):
	li = []
	for i in range(max(n)):
		if isPrime(i) and fun_isadditive(i):
			li.append(i)
	return li[n]