# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.
# [[1,3],   [[1,3,2,2],
# [2,4],      [2,4,5,1]]
# [2,5]], 

def fun_matrixmultiply(m1, m2):
    if len(m1[0]) != len(m2):
        print(len(m1[0]), len(m2))
        return None
    res = []
    for i in range(len(m1)):
        s = []
        for j in range(len(m2[0])):
            s.append(0)
        res.append(s)
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                res[i][j] += m1[i][k]*m2[k][j]
    return res

# fun_matrixmultiply([[1,3],[2,4],[2,5]], [[1,3,2,2], [2,4,5,1]])
fun_matrixmultiply([[1],[2,4],[2,5]], [[1,3,2,2], [2,4,5,1]])
# fun_matrixmultiply([[1,3,5],[2,4,6],[2,5,7]], [[1,3,2,2], [2,4,5,1]])
# fun_matrixmultiply([[1,3],[2,4]], [[1,3,2,2], [2,4,5,1]])
   




