# First, you can read about look-and-say numbers here. Then, write the function lookAndSay(a) that takes a list of 
# numbers and returns a list of numbers that results from "reading off" the initial list using the look-and-say 
# method, using tuples for each (count, value) pair. For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookandsay(a):
	# Your code goes here
	if len(a) <= 0:
		return []
	fnl = []
	idx = 0
	n = a[0]
	for i in range(len(a)):
		if a[i] != n:
			l = len(a[idx:i])
			fnl = fnl + [(l,n)]
			n = a[i]
			idx = i
		if i == len(a)-1:
			l = len(a[idx:])
			fnl = fnl + [(l,n)]
	return fnl
	