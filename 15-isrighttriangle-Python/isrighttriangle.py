# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math

def fun_distance(x1,y1,x2,y2):
	n1 = x2 - x1
	n2 = y2 - y1
	dist = math.sqrt((n1**2) + (n2**2))
	return dist

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	a = fun_distance(x1, y1, x2, y2)
	b = fun_distance(x1, y1, x3, y3)
	c = fun_distance(x2, y2, x3, y3)
	if(max(a,b,c) == a and math.isclose(a**2, b**2+c**2)):
		return True
	elif(max(a,b,c) == b and math.isclose(b**2, a**2+c**2)):
		return True
	elif(max(a,b,c) == c and math.isclose(c**2, a**2+b**2)):
		return True
	else:
		return False
		

