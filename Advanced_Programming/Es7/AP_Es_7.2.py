# Goldbach's conjecture is one of the oldest unsolved problems in number theory and in all of mathematics. It states:
# Every even integer greater than 2 is a Goldbach number, i.e., a number that can be expressed as the sum of two primes.

# Expressing a given even number as a sum of two primes is called a Goldbach partition of the number. For example,

# 04 = 2 +  2           6 = 3 +  3           8 = 3 +  5

# 10 = 7 +  3          12 = 5 +  7          14 = 3 + 11

# 16 = 5 + 11          18 = 7 + 11          20 = 7 + 13

# Write the following Python functions:
# 1. goldbach(n) that returns a Goldbach partition for n
# 2. goldbach_list(n,m) that returns a dictionary indexed on the even numbers in the range (n,m) and whose values are their Goldbach partition