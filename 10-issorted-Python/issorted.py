# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):    #[1, 2, 3, 4, 5.5, 5.1, 7, 8, 9, 10]
	# i = 0           #i=0=>1=>2=>3=>4=>5.5
	# cnt = 1         #1
	# while i < len(a): #T T T T
	# 	if(a[i] < a[i -1]): #2 < 1(F), 3 < 2(F), (F), (F),
	# 		cnt = 1
	# 	i += 1
	# if cnt == 1:
	# 	return True
	# else:
	# 	return False
	s = sorted(a)
	if(a == s):
		return True
	else:
		return False
	# your code goes here