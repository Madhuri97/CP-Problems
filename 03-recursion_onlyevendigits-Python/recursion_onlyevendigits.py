# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.
# [43, 23265, 17, 58344]

def fun_recursion_onlyevendigits(l): 
	def iseven(n): #43, 4
		if n == 0: #F
			return 0
		else:
			n1 = n%10  #3 0
			if n%2 == 0:  #T
				return iseven(n//10)*10+n1 
			return iseven(n//10) #4
	if(len(l) != 0):
		return[iseven(l[0])]+fun_recursion_onlyevendigits(l[1:]) 
	return []
	
