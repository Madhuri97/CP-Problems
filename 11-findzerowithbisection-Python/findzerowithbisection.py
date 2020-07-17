# Bisection Algorithm comes into play!
# We know that the square root of x lies between 1 and x, from mathematics
# Rather than exhaustively trying things starting at 1, suppose instead we pick a number in the middle of this range
# Bisection search works when value of function varies monotonically with input
# If g, the users input/guess, is less than/greater than the midpoint of the range, then that number becomes the new high point of said range and is then factored into the new search.

def method(x):
	return x**3 - x**2 + 2
def findzerowithbisection(x, epsilon):
	if(method(x)*method(epsilon) >= 0):
		return
	c = x
	while((epsilon-x) >= 0.01):
		c = (x+epsilon)/2
		if(method(c) == 0.0):
			break
		if(method(c)*method(x) < 0):
			epsilon = c
		else:
			x = c
	return c

	# epsilon and step are initialized
	# don't change these values
	# epsilon
	# your code starts here