# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 


def fun_set_kth_digit(n, k, d):
	num = abs(n)
	s = str(num)
	if k < len(s):
		i = int(len(s)-k-1)
		s1 = s[0:i]+str(d)+s[i+1:len(s)]
		return int(s1)
	else:
		if n > 0:
			s1 = str(d)+s
			return int(s1)
		else :
			# s1 = abs(n)
			s1 = str(d)  + str(s1)
			s1 = int(s1) * -1
			return s1

