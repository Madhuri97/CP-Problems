# Write the function getAverage(values) that takes a string of 
# comma-separated non-negative integer values, and returns their 
# average as a float (even though the values themselves are integers). 
# Note that some values may not be non-negative integers, and these 
# should be ignored. If there are no integer values, return 0 (do not crash here).
# For example, getAverage('13,excused,14,absent') ignores the two 
# strings and averages 13 and 14 to return 13.5. Also, getAverage('a,b,c') returns 0.
# [13,]

def fun_getaverage(s): 
	sum = 0 #0
	# cnt = 0
	sp = s.split(',')
	for i in sp: #13
		# print(type(int(i)))
		if(i.isdigit()): #T
			if(int(i) > 0): #T
				# cnt += 1
				sum = sum+int(i) #13
		avg = sum/2
	return float(avg)

# fun_getaverage("13,excused,14,absent")

