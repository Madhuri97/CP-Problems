# Write the function fun_distance(x1, y1, x2, y2) 
# that takes four int values x1, y1, x2, y2 
# that represent the two points (x1, y1) and (x2, y2), 
# and returns the distance between those points as a int.
import math

def fun_distance(x1, y1, x2, y2):
	# your code goes here
	n1 = x2-x1
	n2 = y2-y1
	distance = math.sqrt((n1**2) + (n2**2))
	return int(distance)