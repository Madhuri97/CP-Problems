# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



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
        if n1+n2 == n:
            return True
            break
        cnt += 1
    return False 

def fun_nearestkaprekarnumber(n):
    l = n - math.floor(n)
    h = math.ceil(n) - n
    if isKaprekar(n):
        return n
    n1 = n - l
    n2 = n + h
    while True:
        if isKaprekar(n1):
            if isKaprekar(n2):
                if abs(n2 - n) < abs(n1 - n):
                    return n2
                    break
                else:
                    return n1
                    break
            else:
                return n1
                break
        if isKaprekar(n2):
            return n2
            break
        n2 += 1
        n1 -= 1
