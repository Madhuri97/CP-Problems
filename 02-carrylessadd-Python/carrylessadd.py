# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.
# x = 785, y = 765
import math
def fun_carrylessadd(x, y):
	sum = 0  
	if(x == 0):
		return y
	if(y == 0):
		return x
	if(x > 0 and y > 0): #T
		m = 1			 
		each_sum = 0	
		while (x or y):  #
			each_sum = ((x%10)+(y%10))
			each_sum = each_sum%10
			sum = (each_sum*m) + sum
			x = math.floor(x/10)
			y = math.floor(y/10)
			m = m*10
		s = str(sum)
		s.strip("0")
		return int(s)
	return 0
