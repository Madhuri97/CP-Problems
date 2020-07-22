# shortenLongRuns(L, k) [15 pts]
# Write the non-destructive function shortenLongRuns(L, k) that takes a list L and a positive integer k, and 
# non-destructively returns a similar list, only without any run of k consecutive equal values in L. This means that 
# any values that would otherwise produce a consecutive run of k elements are not present. 
# For example: 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 2) == [2, 3, 5, 3]) 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 3) == [2, 3, 5, 5, 3]) 
# Note: your function may not just create a copy of L and call the destructive version of this function (below) on 
# that copy and return it. Instead, you must directly construct the result here.

def shortenlongruns(L, k):
	# Your code goes here
	n = 0
	l = []
	for i in range(len(L)): #5
		if L[i] not in l:   #2-T
			l.append(L[i])  #l = [2,3,5]
			n = 1
		elif L[i] == L[i-1]: #5=5-T T
			n +=1             #2
			if n >= k:		  #2>=2T T
				continue
			else:
				l.append(L[i])
		elif L[i] != L[i - 1]: #T
			l.append(L[i])	   #[2,3,5,3]
			n = 1
	return l