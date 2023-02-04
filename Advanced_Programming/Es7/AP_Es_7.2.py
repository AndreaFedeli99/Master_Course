# Goldbach's conjecture is one of the oldest unsolved problems in number theory and in all of mathematics. It states:
# Every even integer greater than 2 is a Goldbach number, i.e., a number that can be expressed as the sum of two primes.

# Expressing a given even number as a sum of two primes is called a Goldbach partition of the number. For example,

# 04 = 2 +  2           6 = 3 +  3           8 = 3 +  5

# 10 = 7 +  3          12 = 5 +  7          14 = 3 + 11

# 16 = 5 + 11          18 = 7 + 11          20 = 7 + 13

# Write the following Python functions:
# 1. goldbach(n) that returns a Goldbach partition for n
# 2. goldbach_list(n,m) that returns a dictionary indexed on the even numbers in the range (n,m) and whose values are their Goldbach partition

from itertools import combinations_with_replacement

def goldbach(n):
    if n <= 2 or n % 2 != 0: return
    def generate_primes(n):
        sieve = [True for i in range(2, n+1)]
        for i in range(int(n**0.5) + 1):
            if sieve[i]:
                x = 2
                j = (i + 2) * x
                while j < n + 1:
                    sieve[j - 2] = False
                    x += 1
                    j = (i + 2) * x
        return [i for i in range(2, len(sieve)) if sieve[i - 2]]
    return [i for i in combinations_with_replacement(generate_primes(n), 2) if sum(i) == n]

def goldbach_list(n, m):
    return {k: goldbach(k) for k in range(n, m + 1) if k % 2 == 0}

if __name__ == '__main__':
    print(goldbach(3))
    print(goldbach(20))
    print(goldbach_list(4, 20))