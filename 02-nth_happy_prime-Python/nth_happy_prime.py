# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def sumOfSquares(n1):
	s = 0
	while n1 > 0:
		r = n1%10
		s = s + (r**2)
		n1 = n1//10
	return s

def ishappynumber(n):
	l = []
	while sumOfSquares(n) not in l:
		res = sumOfSquares(n)
		if res == 1:
			return True
		else:
			l.append(res)
			n = res
	return False

def isPrime(n):
	for i in range(2,n):
		if(n%1 == 0 and n%i == 0):
			return False
		return True
		

def fun_nth_happy_prime(n):
	li = []
	for i in range(50):
		if ishappynumber(i) and isPrime(i):
			li.append(i)
	return li[n]