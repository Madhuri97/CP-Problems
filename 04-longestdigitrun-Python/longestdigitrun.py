# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	n = str(n)
	l = [str(i) for i in str(n)]
	p = l[0]
	count = 1
	best = p
	bestcnt = count
	while len(l) != 0:
		for j in len(l):
			c = l[j+1]
			if c == p:
				count += 1
			else:
				p = c
				count = 1
			
			if count > bestcnt:
				bestcnt = count
				best = c
				return best
			

# 	print(l)
# longestdigitrun(117773732)