def gray_(n):
    if n == 0: return [""]
    else:
        lower = gray_(n-1)
        return ["0" + bits for bits in lower] + ["1" + bits for bits in lower[::-1]]

def gray(n):
    for g in gray_(n): yield g

def memorization(method):
    def inner(*args):
        if args not in inner.cache.keys():
            inner.cache[args] = method(*args)
        else:
            print(f"\n### cached value for {args} --> {inner.cache[args]}", end='\n')
        return inner.cache[args]
    inner.cache = dict()
    return inner

def mgray(n):
    global gray_
    gray_ = memorization(gray_)
    return gray(n)

if __name__ == '__main__':
    print( "GC(1) :-", end=' ')
    for gc in gray(1): print(gc, end=' ')
    print( "\nGC(2) :-", end=' ')
    for gc in gray(2): print(gc, end=' ')
    print( "\nGC(3) :-", end=' ')
    for gc in gray(3): print(gc, end=' ')
    print( "\nGC(4) :-", end=' ')
    for gc in gray(4): print(gc, end=' ')
    print()
    print( "GC_(1) :-", end=' ')
    for gc in mgray(1): print(gc, end=' ')
    print( "\nGC_(2) :-", end=' ')
    for gc in mgray(2): print(gc, end=' ')
    print( "\nGC_(3) :-", end=' ')
    for gc in mgray(3): print(gc, end=' ')
    print( "\nGC_(4) :-", end=' ')
    for gc in mgray(4): print(gc, end=' ')
    print()