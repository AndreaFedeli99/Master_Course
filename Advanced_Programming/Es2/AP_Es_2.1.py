# Write the solutions for the following quizzes by using functional programming:

# 1. Sum all the natural numbers below one thousand that are multiples of 3 or 5.
# 2. Calculate the smallest number divisible by each of the numbers 1 to 20.
# 3. Calculate the sum of the figures of 2^1000
# 4. Calculate the first term in the Fibonacci sequence to contain 1000 digits.

import functools

# 1.
print(sum(list((filter(lambda num:num % 3 == 0 or num % 5 == 0, range(1, 1001))))))

# 2.
def smallestDivisibleNumber():
    starting_list = list(range(1, 21))
    temp_list = starting_list
    for i in range(len(starting_list)):
        for j in range(i+1, len(starting_list)):
            if temp_list[j]%starting_list[i] == 0:
                temp_list[j] = temp_list[j] // starting_list[i]
    return functools.reduce(lambda val1, val2: val1 * val2, temp_list)

print(smallestDivisibleNumber())

# 3.    
print(functools.reduce(lambda x,y: x+y, [int(figure) for figure in str(2**1000)]))

# 4.
def fibMaxFigures(max_fig):
    a, b = 0, 1
    founded = False
    while not founded and len(str(a)) <= max_fig:
        yield a
        founded = len(str(a)) == 1000
        a, b = b, a + b
print(list(filter(lambda num:len(str(num)) == 1000, [n for n in fibMaxFigures(1000)])))