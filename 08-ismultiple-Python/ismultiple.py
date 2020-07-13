# Write the function isMultiple that takes two int values m and n 
# and returns True if m is a multiple of n and False otherwise. 
# Note that 0 is a multiple of every integer including itself. 
# Also, you should make constructive use of the isFactor function you just wrote above.

def fun_isFactor(f,n):
	if(n == 0 and f == 0):
		return True
	elif(f == 0):
		return False
	if n%f == 0:
		return True
	else:
		return False

def fun_ismultiple(m, n):
	if(fun_isFactor == True or m%n == 0):
		return True
	elif(n == 0 and m == 0):
		return True
	return False # replace with your solution
