"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def partition(array,fst,lst):
	pivot = array[fst]
	left = fst+1
	right = lst

	done = False
	while not done:
		while left <= right and array[left] <= pivot:
			left = left + 1
		while array[right] >= pivot and right >= left:
			right = right - 1
		if right < left:
			done = True
		else:
			tmp = array[left]
			array[left] = array[right]
			array[right] = tmp

	tmp = array[fst]
	array[fst] = array[right]
	array[right] = tmp

	return right

def quicksortpartition(array, fst, lst):
	if fst < lst:
		p = partition(array, fst, lst)
		quicksortpartition(array, fst, p - 1)
		quicksortpartition(array, p + 1, lst)

def quicksort(array):
	quicksortpartition(array,0,len(array)-1)
	return array
	