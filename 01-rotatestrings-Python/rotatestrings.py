# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')

def isNegative(n):
	if(n < 0):
		return True
	return False

def fun_rotatestrings(s, n):
	temp = ""
	if(not isNegative(n)):
		n = n%len(s)
		temp = s[n:]+s[:n]
		return temp

	if(isNegative(n)):
		n = abs(n)
		n = n%len(s)
		temp = s[len(s) - n :] + s[:len(s) - n]
		return temp
		
	return s

