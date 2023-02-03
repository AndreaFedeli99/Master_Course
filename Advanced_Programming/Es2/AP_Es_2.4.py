# Consider the number 6. The divisors of 6 are: 1, 2, 3 and 6.

# Every number from 1 up to and including 6 can be written as a sum of distinct divisors of 6: 1=1, 2=2, 3=1+2, 4=1+3, 5=2+3, 6=6.

# A number n is called a practical number if every number from 1 up to and including n can be expressed as a sum of distinct divisors of n.

# A pair of consecutive prime numbers with a difference of six is called a sexy pair (since "sex" is the Latin word for "six"). The first sexy pair is (23, 29).

# We may occasionally find a triple-pair, which means three consecutive sexy prime pairs, such that the second member of each pair is the first member of the next pair.

# We shall call a number n such that: (n-9, n-3), (n-3,n+3), (n+3, n+9) form a triple-pair, and the numbers n-8, n-4, n, n+4 and n+8 are all practical, an engineers' paradise.

# Find the sum of the first four engineers' paradises.

from itertools import chain, cycle, accumulate, combinations

def factors(n):
    def prime_powers(n):
        for c in accumulate(chain([2, 1, 2], cycle([2,4]))):
            if c*c > n: break
            if n%c: continue
            d,p = (), c
            while not n%c:
                n,p,d = n//c, p*c, d + (p,)
            yield(d)
        if n > 1: yield((n,))

    r = [1]
    for e in prime_powers(n):
        r += [a*b for a in r for b in e]
    return r[:-1]

def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

def isPractical(x: int) -> bool:
    if x == 1:
        return True
    if x % 2:
        return False
    mult_4_or_6 = (x % 4 == 0) or (x % 6 == 0)
    if x > 2 and not mult_4_or_6:
        return False

    f = sorted(factors(x), reverse=True)
    if sum(f) < x - 1:
        return False
    ps = powerset(f)

    found = set()
    for nps in ps:
        if len(found) < x - 1:
            y = sum(nps)
            if 1 <= y < x:
                found.add(y)
        else:
            break
    return len(found) == x - 1

def isPrime(n):
    return [i for i in range(2, int(n**0.5) + 1) if n%i==0] == []

def generatePrimes(n):
    sieve = [True for i in range(2, n+3)]
    for i in range(0, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i+2, len(sieve)):
                if (j+2) % (i+2) == 0:
                    sieve[j] = False
    return [i for i in range(2, len(sieve)) if sieve[i - 2]]

def isSexyPair(n1, n2):
    if n2 - n1 != 6:
        return False
    elif not isPrime(n1) or not isPrime(n2):
        return False
    primes = generatePrimes(n2)
    return (primes[len(primes) - 1] == n2) and (primes[len(primes) - 2] == n1)

def isTriplePair(p1, p2, p3):
    return p1[1] == p2[0] and p2[1] == p3[0] and isSexyPair(*p1) and isSexyPair(*p2) and isSexyPair(*p3)

def getNextEngineerParadise():
    n = 10
    while True:
        print(f"Checking if {n} is an engineers' paradise") if n % 1000 == 0 else None
        if isPractical(n-8) and isPractical(n-4) and isPractical(n) and isPractical(n+4) and isPractical(n+8) and isTriplePair((n-9, n-3), (n-3, n+3), (n+3, n+9)):
            print(f"{n} is an engineers' paradise")
            yield n
        n += 1

def sumOfFirstNEngineersParadise(n):
    eng_paradise_founded = 0
    getParadise = getNextEngineerParadise()
    res = 0
    while (eng_paradise_founded != n):
        res += next(getParadise)
        eng_paradise_founded += 1
    return res

print(sumOfFirstNEngineersParadise(4))