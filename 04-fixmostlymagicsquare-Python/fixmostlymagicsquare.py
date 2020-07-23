# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.
# [[2, 7, 9], [9, 5, 1], [4, 3, 8]] => [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

def fixmostlymagicsquare(L):  #[[2, 7, 9], [9, 5, 1], [4, 3, 8]]
	l = []
	for i in L: #i = [2, 7, 9]  i = [9, 5, 1]    i = [4, 3, 8]
		n = 0
		n += sum(i) #18             #15             15
		l.append(n) #l=[18]        l=[18,15]       l=[18,15,15]
	if(len(l) != len(set(l))): #T
		k = max(l) - min(l)    #18-15 = 3
		maxi = max(l)          #18         
		for i in l:			   
			if i == maxi:      #i==18
				idx = l.index(max(l))      #idx = 1
		d = L[idx]                         #a = 2,7,9
		idx1 = d.index(max(d))             #a[3] = 6
		d[idx1] = max(d) - k
		L[idx] = d
		return L
		
	# Your code goes here