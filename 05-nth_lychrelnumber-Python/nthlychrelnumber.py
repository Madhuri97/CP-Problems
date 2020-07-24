# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def reverse(n):
	q = 0
	while (n > 0):
		r = (n%10)
		q = (q*10)+r
		n = n // 10
	return q

def isPalindrome(n):
	if n == reverse(n):
		return True
	else:
		return False

def isLychrelNumber(n):
	for i in range(1,51):
		n = n + reverse(n)
		if (isPalindrome(n)):
			return False
	return True

def nthlychrelnumbers(n):
	# your code goes here
	l = []
	for i in range(5000):
		if isLychrelNumber(i):
			l.append(i)
	return l[n-1]