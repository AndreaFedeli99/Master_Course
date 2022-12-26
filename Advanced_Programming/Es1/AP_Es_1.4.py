# A matrix can be represented as a list of lists (rows and columns).

# 1. Use the comprehensions to define a function (identity) that returns the identity matrix (the one with all 0s but the 1s on the diagonal) of given size.
# 2. Use the comprehensions to define a function (square) that returns a square matrix filled with the first n*n integers with n given as an argument.
# 3. Write the function transpose to transpose a generic matrix independently of the size and content.
# 4. Write the function multiply to multiply two matrices non necessarily square matrices.

def identity(dim):
    return [[1 if j==i else 0 for j in range(dim)] for i in range(dim)]

print(identity(4))

def square(dim):
    return [[j+i*dim for j in range(1, dim + 1)] for i in range(dim)]

print(square(5))

def transpose(matrix):
    return [[matrix[y][i] for y in range(len(matrix))] for i in range(len(matrix[0]))]

print(transpose(square(5)))

A=[[1,2],[3,4],[5,6]]
print(transpose(A))

def multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return None
    else:
        elem = lambda A,B,i,j : sum([A[i][k]*B[k][j] for k in range(len(A[0]))])
        return [[ elem(matrix1, matrix2, i, j) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]

M1=[[1,2,3],[4,5,6]]
M2=[[7,8],[9,10],[11,12]]

print(multiply(M1, M2))
print(multiply(M2, M1))

M3=[[3,4,2]]
M4=[[13,9,7,5],[8,7,4,6],[6,4,0,3]]

print(multiply(M3, M4))