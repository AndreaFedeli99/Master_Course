resource = 0

def manage_resource(f):
    def wrapper(*args, **kwargs):
        f.calls += 1
        if f.calls <= resource:
            return f(*args, **kwargs)
        else:
            print("resources run out")
            f.calls = 0
            raise SystemExit
    
    f.calls = 0
    return wrapper

@manage_resource
def fact(n):
    if n <= 1:
        return n
    return n * fact(n-1)

@manage_resource
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-2) + fibo(n-1)

if __name__ == "__main__":
    resource = 10
    print("{0}! :- {1}".format(10,fact(10)))
    resource = 9
    try:
        print("{0}! :- {1}".format(10,fact(10)))
    except SystemExit: pass
    resource = 160
    try:
        print("fibo({0}) :- {1}".format(10,fibo(10)))
    except SystemExit: pass
    resource = 180
    print("fibo({0}) :- {1}".format(10,fibo(10)))