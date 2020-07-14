# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.
import math

def trianglearea(s1, s2, s3):
	# your code goes here
	s = (s1+s2+s3)/2
	area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
	return area
