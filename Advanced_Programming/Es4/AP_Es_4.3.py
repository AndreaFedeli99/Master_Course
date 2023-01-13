# Pascal's triangle is a geometric arrangement of the binomial coefficients in a triangle.

# The rows of Pascal's triangle are conventionally enumerated starting with row 0, and the numbers in each row are usually staggered relative to the numbers in the adjacent rows.
# A simple construction of the triangle proceeds in the following manner. On row 0, write only the number 1. 
# Then, to construct the elements of following rows, add the number directly above and to the left with the number directly above and to the right to find the new value. 
# If either the number to the right or left is not present, substitute a zero in its place.

# Implement an iterator for the Pascal's triangle that:
# 1. at each step will return another iterator containing all the elements in the corresponding stage sorted as in the triangle
# 2. the iterator can go forward and backward
# 3. (advanced) it is possible to define the working algebra for the triangle, e.g., it could be on Z7 or on the alphabet