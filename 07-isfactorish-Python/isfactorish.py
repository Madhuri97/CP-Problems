# Write the function fun_isfactorish(n) that takes a value int n, 
# and returns True if n is a (possibly-negative) integer with exactly 3 unique digits 
# (so no two digits are the same), where each of the digits is a factor of the number 
# n itself. In all other cases, the function returns False (without crashing).
# For example:
#  assert(fun_isfactorish(412) == True) # 4, 1, and 2 are all factors of 412
#  assert(fun_isfactorish(-412) == True) # Must work for negative numbers!
#  assert(fun_isfactorish(4128) == False) # 4128 has more than 3 digits
#  assert(fun_isfactorish(112) == False) # 112 has duplicate digits (two 1's)
#  assert(fun_isfactorish(420) == False) # 420 has a 0 (0 is not a factor)
#  assert(fun_isfactorish(42) == False) # 42 has a leading 0 (only 2 unique digits)


def fun_isfactorish(n):
	num = str(abs(n))
	if(len(num) != 3 or (num[0] == num[1] or num[1] == num[2] or num[2] == num[0]) or num.count("0") > 0):
		return False
	return True
	# if(len(str(num)) == 2):
	# 	r = num%10 
	# 	while(r != 0):
	# 		if(num%r == 0):
	# 			num = num//10
	# 		r = num%10
	# 	return True
	# return False
