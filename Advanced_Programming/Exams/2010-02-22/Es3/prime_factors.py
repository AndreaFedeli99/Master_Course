def prime_factors(n):
    def gen_primes(n):
        sieve = [True] * (n+1)
        sieve[0] = sieve[1] = False
    
        for (i, isprime) in enumerate(sieve):
            if isprime:
                yield i
                for j in range(i*i, n, i):
                    sieve[j] = False

    while n != 1:
        for prime in gen_primes(n):
            if n % prime == 0:
                yield prime
                break
        n = n // prime