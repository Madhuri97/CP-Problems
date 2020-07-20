# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.
2,7,6,9,5,1,4,3,8
def hasduplicates(L):
	# Your code goes here
	count = 0
	temp = []
	TL = [j for sub in L for j in sub]
	for i in TL:
		if i in temp:
			count = count+1
		temp.append(i)

	if count >= 1:
		return True
	return False

	