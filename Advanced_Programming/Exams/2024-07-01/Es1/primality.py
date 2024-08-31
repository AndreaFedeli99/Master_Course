from math import isqrt, log2
from random import randint

def is_prime(n):
    if n > 524_280:
        res = littlefermat(n)
    elif n > 10_000:
        res = lucaslehmer(n)
    else:
        res = trialdivision(n)
    return res

def littlefermat(n, k=10_000):
    for _ in range(0, k):
        if pow(randint(1, n - 1), n - 1, n) != 1:
            return False
    return True

def lucaslehmer(n):
    s = 4
    p = int(log2(1 + n))
    for i in range(p-2):
        s = pow(s, 2, n) - 2
    return s == 0

def trialdivision(n):
    for div in range(2, isqrt(n)+1):
        if n % div == 0:
            return False
    return True