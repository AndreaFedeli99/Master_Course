# Implement tail-recursion on recursive methods

import inspect

class RecursiveException(Exception):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

def tail_recursion(method):
    def wrapper(*args, **kwargs):
        stack = inspect.stack()
        if len(stack) > 3 and stack[0][0].f_code == stack[2][0].f_code:
            raise RecursiveException(args, kwargs)
        else:
            while True:
                try:
                    return method(*args, **kwargs)
                except RecursiveException as e:
                    args = e.args
                    kwargs = e.kwargs
    return wrapper

@tail_recursion
def fact(n, acc):
    if n == 1:
        return acc
    return fact(n - 1, n* acc)

if __name__ == '__main__':
    print(fact(1001, 1))