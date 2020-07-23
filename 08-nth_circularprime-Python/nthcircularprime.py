# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def isprime(n):
	if n > 1:
		for i in range(2,n):
			if n%i == 0:
				return False
		return True
	return False

def rotatenumber(n):
	t = n
	cnt = 0
	while t != 0:
		t = t//10
		cnt += 1
	r = n%10
	q = n//10
	return r * (10**(cnt - 1)) +q

def isCircularPrime(n):
	if n == 0:
		return False
	t = n
	cnt = 0
	while t != 0:
		t = t//10
		cnt += 1
	for i in range(cnt):
		if not isprime(n):
			return False 
		n = rotatenumber(n)
	return True

def nthcircularprime(n):
	l = []
	for i in range(10000):
		if isCircularPrime(i):
			l.append(i)
	return l[n]
	# Your code goes here

	