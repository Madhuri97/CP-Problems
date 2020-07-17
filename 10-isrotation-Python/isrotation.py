# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	# Your code goes here
	if(len(str(x)) != len(str(y))):
		return False
	if str(y) in str(x)+str(x):
		return True
	return False
	# else:
	# 	while(x == y):  #3124 1234(T)
	# 		p = pow(10, len(str(x))-1)
	# 		for i in range(len(str(x))-1):
	# 			fd = x//p
	# 			left = (x*10+fd - (fd*p*10))
	# 		x = left 
	# 	return True
	# return False