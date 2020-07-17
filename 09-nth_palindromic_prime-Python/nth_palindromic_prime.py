# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2


def Fun_isPalindrome(n):
	tmp = n
	rev = 0
	while(n > 0):
		r = n%10
		rev = rev*10+r
		n = n//10
	if(tmp == rev):
		return True
	else:
		return False

def fun_isPrime(n):
	if(n > 1 and Fun_isPalindrome(n)):
		for i in range(2,n):
			if(n%i == 0):
				return False
		return True
	return False

def fun_nth_palindromic_prime(n):
	li = []
	for i in range(100000):
		if fun_isPrime(i):
			li.append(i)
	return li[n]