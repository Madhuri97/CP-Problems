# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def isKaprekar(n):
    if n <= 0:
        return False
    k = n**2
    if k < 10:
        if k == n:
            return True
    numk = math.ceil(math.log(k,10))
    cnt = 1
    while cnt < numk:
        n1 = k%10**cnt
        n2 = k//10**cnt
        if n1 == 0:
            cnt += 1
            continue
        if n1 + n2 == n:
            return True
            break
        cnt += 1
    return False

def fun_nth_kaprekarnumber(n):
    l = []
    for i in range(78000):
        if isKaprekar(i):
            l.append(i)
    return l[n]