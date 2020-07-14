# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.



def fun_nearestodd(n):
	temp = n
	rem = temp%2 
	if(rem != 0):
		return int(temp)
	elif(rem == 0):
		return temp-1
	return 2*int((temp%2.0))+1


