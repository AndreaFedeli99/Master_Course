from primality import is_prime

def test_primes(vl):
    if len(vl) > 0:
        print(f"{vl[0]:14d} :- {is_prime(vl[0])}")
        test_primes(vl[1:])

if __name__ == '__main__':
    test_primes([25, 127, 8191, 131071, 524286, 524287, 524288, 2147483647])