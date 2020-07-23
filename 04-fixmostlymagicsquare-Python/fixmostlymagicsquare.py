# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):
	l = []
	for i in L:
		n = 0
		n += sum(i)
		l.append(n)
	if(len(l) != len(set(l))):
		k = max(l) - min(l)
		maxi = max(l)
		for i in l:
			if i == maxi:
				idx = l.index(max(l))
		d = L[idx]
		idx1 = d.index(max(d))
		d[idx1] = max(d) - k
		L[idx1] = d
		return L
	# Your code goes here