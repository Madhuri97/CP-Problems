# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46
def isTidyNumber(n):
    p = 10
    while (n): 
        r = n%10 #2
        n = n//10
        if r > p:
            return False
        p = r
    return True
        

def fun_nth_tidynumber(n):
    l = []
    for i in range(1000):
        if isTidyNumber(i):
            l.append(i)
    return l[n+1]
