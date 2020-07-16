# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):    
	i = 1           
	cnt = 0         
	while i < len(a): 
		if(a[i] < a[i -1]): 
			cnt = 1
		cnt = 0
		i += 1
	if  not cnt:
		return True
	else:
		return False
	# s = sorted(a)
	# s1 = sorted(a, reverse = True)
	# if(a == s or a == s1):
	# 	return True
	# else:
	# 	return False
	# your code goes here