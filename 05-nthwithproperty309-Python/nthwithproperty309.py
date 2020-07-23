# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
	# Your code goes here
	def isWithProperty309(n):
		i = 0
		cnt = 0
		n = n**5
		t = n
		while n > 0:
			if i != n%10:
				n = n//10
			elif i == n%10:
				cnt += 1
				n = t
				i += 1
				if cnt > 9:
					return True
		return False

	i = -1
	gus = 0
	while i < n:
		gus += 1
		if isWithProperty309(gus):
			i += 1
	return gus
