from prime_factors import *

def print_factors(n):
    print("The prime factors of {0} are:".format(n))
    for n in prime_factors(n):
        print(n, end=' ')
    print()

if __name__ == '__main__':
    print_factors(128)
    print_factors(9999)
    print_factors(123456789)