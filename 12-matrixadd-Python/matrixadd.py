# matrixAdd(L, M)[10 pts]
# Background: we can think of a 2d list in Python as a matrix in math. To add two matrices, L and M, they must have 
# the same dimensions. 
# Then, we loop over each row and col, and the result[row][col] is just the sum of L[row][col] and M[row][col]. For example:
# L = [ [1,  2,  3],
#       [4,  5,  6] ]
# M = [ [21, 22, 23],
#       [24, 25, 26]]
# N = [ [1+21, 2+22, 3+23],
#       [4+24, 5+25, 6+26]]
# assert(matrixAdd(L, M) == N)
# With this in mind, write the function matrixAdd(L, M) that takes two rectangular 2d lists (that we will consider 
# to be matrices) that you 
# may assume only contain numbers, and returns a new 2d list that is the result of adding the two matrices. Return 
# None if the two matrices 
# cannot be added because they are of different dimensions.

def matrixadd(L, M):  #L=1 ; M=10
	# Your code goes here
	# print(len(L[0]), len(L[1]), len(M[0]))
	
	res = []
	if(len(L) == len(M) and len(L[0]) != len(M[0])):
		return None
	else:
		for i in range(len(L)):
			if i > 0  and len(L[i]) != len(M[i]):
				return None
			N = []
			for j in range(len(L[0])):
				N.append(L[i][j]+M[i][j])
			res.append(N)
		return res

# matrixadd([[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	# N = arr.array('k',)
	# for i in range(len(L)):
	# 	for j in range(len(L[0])):
	# 		N[i][j] = L[i][j] + M[i][j]
	# for k in N:
	# 	return k

	# 1 2 3              1 2 3      2 4 6        
	# 4 5 6              4 5 6      8 10 12
	# 7 8 9              7 8 9      14 16 18
	
	