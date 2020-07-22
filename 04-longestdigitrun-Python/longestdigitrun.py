# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	if n < 0:
		n = -n
	l = list(map(int,str(n)))
	di = {}
	count = 1
	for i in range(len(l) - 1):
		if l[i] == l[i+1]:
			count = 0
			if l[i] in di:
				di[l[i]] = di[l[i]] + 1
			else:
				di[l[i]] = 1
	if count == 1:
		l.sort()
		return l[0]
	newdi = {}
	h = sorted(di.keys())
	for i in h:
		newdi[i] = di[i]
	newdi = sorted(newdi.items(), key = lambda item:item[1], reverse = True)
	return newdi[0][0]

	# while len(l) != 0:
	# 	for j in len(l):
	# 		c = l[j+1]
	# 		if c == p:
	# 			count += 1
	# 		else:
	# 			p = c
	# 			count = 1
			
	# 		if count > bestcnt:
	# 			bestcnt = count
	# 			best = c
	# 			return best
			

# 	print(l)
# longestdigitrun(117773732)