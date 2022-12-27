# sin(x) can be approximate by the Taylor's series:
# sinx = x - (x^3/3!) + (x^5/5!) - (x^7/7!)
# Let's write a library to implement sin(x, n) by using the Taylor's series (where n is the level of approximation, i.e., 1 only one item, 2 two items, 3 three items and so on).
# Let's compare your function with the one implemented in the math module at the growing of the approximation level.

# Hint. Use a generator for the factorial and a comprehension for the series.

import math

def fact(n):
    res = 1
    index = 1
    while n > 0:
        yield res
        res *= index
        index += 1
        n -= 1

def sin(x, n):
    factorial = fact(2*n)
    return sum([[-x**((index*2)+1)/next(factorial) if index%2 != 0 else x**((index*2)+1)/next(factorial) for i in range(2)][1] for index in range(n)])

print(sin(math.pi, 5))