"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    # Your code goes here
    lw = 0
    hi = len(input_array) - 1
    while(lw <= hi):
        mid = (lw+hi)//2

        if(input_array[mid] == value):
            return mid
        elif(input_array[mid] < value):
            lw = mid + 1
        else:
            hi = mid - 1
    return -1
    # if hi > lw:
    #     mid = (hi + lw)//2
    #     if input_array[mid] == value:
    #         return mid
    #     elif input_array[mid] > value:
    #         return binary_search(input_array, value)
    #     else:
    #         return binary_search(input_array, value)
    # else:
    #     return -1
