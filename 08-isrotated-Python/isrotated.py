# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.

# XYZ ZXY
def isrotated(str1, str2):
	#Your code goes here
	s = ""
	for i in str2: #Z
		s = i + s  #Z
	if(str1 == s):
		return True
	else:
		return False
	# str2=str2[::-1]
	# if(str1 == str2):
	# 	return True
	# else:
	# 	return False