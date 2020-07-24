# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.

def isUglyNumber(n):
    if n == 1:
        return 1
    if n <= 0:
        return 0

    if n%2 == 0:
        return isUglyNumber(n//2)
    if n%3 == 0:
        return isUglyNumber(n//3)
    if n%5 == 0:
        return isUglyNumber(n//5)
    return 0


def fun_nth_uglynumber(n):
    l = []
    for i in range(2000):
        if isUglyNumber(i):
            l.append(i)
    return l[n]
