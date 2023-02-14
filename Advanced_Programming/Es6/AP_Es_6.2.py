# Let us consider a class MyMath with the following methods: fib, fact and taylor implementing the Fibonacci's series, the factorial and 
# the Taylor's series for a generic function and a level of approximation respectively. Then implement the following decorators:
# 1. @memorization applied to a method stores in the class previously calculated results and reuses them instead of recalculating
# 2. @logging applied to a method writes on a file the method name, its actual arguments when a method is called (also by recursion)
# 3. @stack_trace applied to a method prints its stack trace, i.e., the list of calls made to carry out the invocation.

from sympy import *
from functools import wraps

def memorization(method):
    @wraps(method)
    def inner(*args):
        if args in inner.cache.keys():
            return inner.cache[args]
        inner.cache[args] = method(*args)
        return inner.cache[args]
    inner.cache: dict = dict()
    return inner

def logging(method):
    @wraps(method)
    def inner(*args):
        with open('log.txt', mode = 'a+', encoding='utf-8') as f:
            f.write(f"logging::__call__ :- {method.__name__}{args[1:]}\n")
        return method(*args)
    return inner

def stack_trace(method):
    @wraps(method)
    def inner(*args):
        inner.stack = [f'{method.__name__}{args[1:]}'] + inner.stack
        print(inner.stack, sep='\n')
        res = method(*args)
        inner.stack = inner.stack[1:]
        return res
    inner.stack = list()
    return inner

class MyMath:

    x = Symbol('x')
    
    @memorization
    @logging
    @stack_trace
    def fib(self, n):
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
    
    @memorization
    @logging
    @stack_trace
    def fact(self, n):
        if n <= 1:
            return 1
        return n * self.fact(n - 1)

    @memorization
    @logging
    @stack_trace
    def taylor(self, f, n, x0):
        if n == 0:
            return f.subs(self.x, x0)
        return ((diff(f, self.x, n).subs(self.x, x0) * (self.x - x0)**n / self.fact(n))) + self.taylor(f, n - 1, x0)

m = MyMath()
x = Symbol('x')

print(m.fib(4))

print(m.fact(4))

pretty_print(m.taylor(exp(x), 4, 0))