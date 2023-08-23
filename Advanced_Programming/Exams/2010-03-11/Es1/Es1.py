def myfact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        if i%2 != 0: yield fact

def mysin(x, n):
    g=myfact(n)
    return sum([(x**i)/next(g) for i in range(1, n//2+1)])

def mysin_corrected(x, n):
    g=myfact(n)
    return sum(map(lambda item: item[1] if item[0] % 2 == 0 else -item[1], enumerate([(x**i)/next(g) for i in range(1, n//2+1)])))

print("Previous implementation:")
print("sin(1) = {0}".format(mysin(1, 6)))

print("Correct implementation:")
print("sin(1) = {0}".format(mysin_corrected(1, 6)))
