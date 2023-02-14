# You are to write a class Matrix for representing and manipulating integer matrices. 
# An instance of this class stores the elements of a matrix as a list of lists of integers, and provides methods for the operations of matrix equivalence, 
# matrix copy, matrix addition, scalar-matrix multiplication, matrix-matrix multiplication, matrix transposition, and matrix norm -- the "size" of a matrix. 
# Override the appropriate operators and raise the appropriate exceptions.

# We first define these operations, and then give a skeleton of the Matrix class showing the signatures for all methods and constructors you must implement.

# The operations

# Let aij denote the i,j-th element of matrix A, located at row i, column j. Using this notation, the matrix operations listed above may be defined precisely as follows:
# - matrix equivalence A ≃ B where A in Zm×n, B in Zp×q when m = p and n = q and bij = aij for i = 1,...,m j = 1,...,n;
# - matrix copy B = A where A, B in Zm×n (bij = aij for i = 1,...,m j = 1,...,n);
# - matrix addition C = A + B where A, B, C in Zm×n (cij = aij + bij for i = 1,...,m j = 1,...,n);
# - scalar-matrix multiplication B = aA where A, B in Zm×n, a in Z (bij = a·aij for i = 1,...,m j = 1,...,n);
# - matrix-matrix multiplication C = A·B where A in Zm×p, B in Zp×n, C in Zm×n (cij = Σk=1, ..., p aik·bkj for i = 1,...,m j = 1,...,n);
# - matrix transposition B = AT where A in Zm×n, B in Zn×m (bji = aij for i = 1,...,m j = 1,...,n);
# - matrix norm (matrix 1-norm) a = ‖A‖ where a in Z, A in Zm×n (a = maxj Σi | aij | for i = 1,...,m j = 1,...,n).

# Note that in each case we state the proper matrix dimensions for the operation to be valid. For example, when multiplying two matrices A and B, the number of columns of A must match the number of rows of B.

import copy
from functools import reduce

class Matrix:
    def __init__(self, m):
        self.matrix = m
    
    def can_perform_add(self, other):
        return len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0])

    def can_perform_mul(self, other):
        return len(self.matrix[0]) == len(other.matrix) and len(self.matrix) == len(other.matrix[0])

    def __str__(self):
        return '\n'.join([str(row) for row in self.matrix])

    def __repr__(self):
        return "Matrix({0})".format(self.matrix)

    def __eq__(self, other):
        try:
            return all([v == other.matrix[i][j] for i, col in enumerate(self.matrix) for j,v in enumerate(col)])
        except (IndexError, AttributeError):
            return False
    
    def __deepcopy__(self, memo):
        return Matrix(copy.deepcopy(self.matrix, memo))
    
    def __add__(self, other):
        try:
            assert self.can_perform_add(other), "Matrix should have the same dimensions"
            return Matrix([[v + other.matrix[i][j] for j,v in enumerate(col)] for i, col in enumerate(self.matrix)])
        except AttributeError:
            raise TypeError("Method argument must be a Matrix instance")
    
    def __mul__(self, other):
        try:
            assert self.can_perform_mul(other), "First matrix's columns dimension must be equal to second matrix's rows dimension"
            return Matrix([[reduce(lambda x, y: x + y, map(lambda x, y: x * y[i], self.matrix[n], other.matrix)) for i in range(len(self.matrix))] for n in range(len(self.matrix))])
        except AttributeError:
            return Matrix([[v * other for v in row] for row in self.matrix])
    
    __rmul__ = __mul__

    def T(self):
        return Matrix([[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))])
    
    def one_norm(self):
        return max([reduce(lambda x,y: abs(x) + abs(y), [self.matrix[i][n] for i in range(len(self.matrix))]) for n in range(len(self.matrix[0]))])


if __name__ == "__main__":
    m1 = Matrix([[1, 2, 3], [4, 5, 6]])
    m2 = Matrix([[1, 2], [3, 4], [5, 6]])

    print("m1=")
    print(m1)
    print()
    print("m2=")
    print(m2)

    print()

    print("m1 == m2:", m1 == m2)

    print()

    print("Let's copy m1 into m3")
    m3 = copy.deepcopy(m1)
    print("m3=")
    print(m3)

    print()

    print("m3 == m1:", m3 == m1)
    print("m3 is m1:", m3 is m1)

    print()

    print("m1 + m3 =")
    print(m1 + m3)

    print()

    print("m1 * 2 =")
    print(m1 * 2)

    print()

    print("m1 * m2 =")
    print(m1 * m2)

    print()

    print("m1 transposition is:")
    print(m1.T())

    print()

    print("m3 1-norm is:")
    print(m3.one_norm())