# Consider the number 6. The divisors of 6 are: 1, 2, 3 and 6.

# Every number from 1 up to and including 6 can be written as a sum of distinct divisors of 6: 1=1, 2=2, 3=1+2, 4=1+3, 5=2+3, 6=6.

# A number n is called a practical number if every number from 1 up to and including n can be expressed as a sum of distinct divisors of n.

# A pair of consecutive prime numbers with a difference of six is called a sexy pair (since "sex" is the Latin word for "six"). The first sexy pair is (23, 29).

# We may occasionally find a triple-pair, which means three consecutive sexy prime pairs, such that the second member of each pair is the first member of the next pair.

# We shall call a number n such that: (n-9, n-3), (n-3,n+3), (n+3, n+9) form a triple-pair, and the numbers n-8, n-4, n, n+4 and n+8 are all practical, an engineers' paradise.

# Find the sum of the first four engineers' paradises.

def isPractical(n):
    2 * n <= sum([i for i in range(1, n) if n % i == 0], 1)

def generatePrimes(n):
    sieve = [True for i in range(2, n+3)]
    for i in range(int(n**0.5) + 1):
        if sieve[i]:
            x = 2
            j = (i + 2) * x
            while j < n+3:
                sieve[j - 2] = False
                x += 1
                j = (i + 2) * x
    return [i for i in range(2, len(sieve)) if sieve[i - 2]]

def isSexyPair(n1, n2):
    primes = generatePrimes(n2)
    return (primes[len(primes) - 1] == n2) and (primes[len(primes) - 2] == n1)

def isTriplePair(p1, p2, p3):
    return p1[1] == p2[0] and p2[1] == p3[0] and isSexyPair(*p1) and isSexyPair(*p2) and isSexyPair(*p3)

def getNextEngineerParadise():
    n = 10
    while True:
        print(f"Checking if {n} is an engineers' paradise") if n % 10000 == 0 else None
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

if __name__ == '__main__':
    print(sumOfFirstNEngineersParadise(4))