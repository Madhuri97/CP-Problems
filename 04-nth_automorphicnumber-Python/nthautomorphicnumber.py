# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.


def isAutomorphicNumber(n):
	s = n**2
	r = len(str(n))
	lst = s%pow(10,r)
	if lst == n:
		return True
	return False

def nthautomorphicnumbers(n):
	# Your code goes here
	l = []
	for i in range(500000):
		if isAutomorphicNumber(i):
			l.append(i)
	return l[n-1]

	