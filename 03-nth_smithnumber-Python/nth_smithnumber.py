# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def isPrime(n):
    for i in range(2,n):
        if(n%1 == 0 and n%i == 0):
            return False
        return True

def sumOfDigits(n):
    s = 0
    while n > 0:
        r = n%10
        s = s + r
        n = n//10
    return s

def sumOfFactors(n):
    l = []
    for i in range(2,n+1):
        if n%i == 0:
            l.append(i)
    return sum(l)

def isSmith(n):
    if sumOfDigits(n) == sumOfFactors(n):
        return True
    else:
        return False

def fun_nth_smithnumber(n):
    l = []
    for i in range(1,1000):
        if isSmith(i) and not isPrime(i):
            l.append(i)
    return l[n]