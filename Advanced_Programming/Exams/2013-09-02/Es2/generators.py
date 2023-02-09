
def even(s):
    for n in s:
        if n%2 == 0:
            yield n

def stopAt(s, n):
    for num in s:
        if num > n: break
        yield num

def buffer(s, n):
    res = list()
    has_next = True
    while has_next:
        for i in range(n):
            try:
                res.append(next(s))
            except StopIteration as ex:
                has_next = False
        yield res
        res.clear()

def conditional(seq, p):
    def bufnext(seq):
        bufnext.store = [bufnext.store[1], next(seq)]
        return bufnext.store
    
    bufnext.store = [0, next(seq)]
    
    while True:
        res = bufnext(seq)
        if p(res[1]): yield res[0]
