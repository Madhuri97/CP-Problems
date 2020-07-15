# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.
import statistics
def median(a):

	if(len(a) != 0):
		return statistics.median(a)
	else:
		return None
	# your code goes here