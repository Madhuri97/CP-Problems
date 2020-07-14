# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):

	n = abs(digit) 
	n1 = n%10**(k+1) 
	n2 = n%10**(k)   
	num = (n1 + n2)/(10**k)  
	return abs(num)
