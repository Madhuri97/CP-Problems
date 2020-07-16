# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)

def ishappynumber(n):
	def sumOfSquares(n1):
		s = 0
		while n1 > 0:
			r = n1 % 10
			s = s + (r**2)
			n1 = n1 // 10
		return s
	l = []
	while sumOfSquares(n) not in l:
		res = sumOfSquares(n)
		if res == 1:
			return True
		else:
			l.append(res)
			n = res
	return False
	
def fun_nth_happy_number(n):
	li = []
	for i in range(50):
		if ishappynumber(i):
			li.append(i)
	return li[n]
