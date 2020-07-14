# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
	# your code goes here
	i = 12
	if(eggs == 0):
		return 0
	if(eggs%i == 0):
		return  eggs//i
	if(eggs%i == 1):
		return eggs//i + 1
	else:
		return 1

	
