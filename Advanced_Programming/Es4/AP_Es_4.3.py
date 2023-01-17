# Pascal's triangle is a geometric arrangement of the binomial coefficients in a triangle.

# The rows of Pascal's triangle are conventionally enumerated starting with row 0, and the numbers in each row are usually staggered relative to the numbers in the adjacent rows.
# A simple construction of the triangle proceeds in the following manner. On row 0, write only the number 1. 
# Then, to construct the elements of following rows, add the number directly above and to the left with the number directly above and to the right to find the new value. 
# If either the number to the right or left is not present, substitute a zero in its place.

# Implement an iterator for the Pascal's triangle that:
# 1. at each step will return another iterator containing all the elements in the corresponding stage sorted as in the triangle
# 2. the iterator can go forward and backward
# 3. (advanced) it is possible to define the working algebra for the triangle, e.g., it could be on Z7 or on the alphabet

class PascalTriangle:

    def __init__(self, stage):
        self._triangle = [[1], [1, 1]]
        self._stage = stage

    def __iter__(self):
        self.n = 0
        self.__calculate_triangle()
        return self
    
    def __next__(self):
        if self.n < self._stage:
            res = self._triangle[self.n]
            self.n += 1
            return res
        raise StopIteration

    def prev(self):
        if self.n > 0:
            res = self._triangle[self.n - 1]
            self.n -= 1
            return res
        raise StopIteration

    def __calculate_triangle(self):
        def inner(res):
            if len(self._triangle) == self._stage : return res
            res.append([1] + [res[-1][i] + res[-1][i + 1] for i in range(0, len(res[-1]) - 1)] + [1])
            return inner(res)
        return inner(self._triangle)

t = PascalTriangle(5)

print("Pascal triangle:")
for i in t:
    print(*t, sep='\n')

print("Reversed Pascal triangle:")
for i in range(t._stage):
    print(t.prev())