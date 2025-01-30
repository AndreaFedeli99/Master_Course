class NegativeNumber(Exception): pass
class DivisionByZero(Exception): pass

def zero(): return "0"

def succ(p): return f"succ({p})"

def evaluate(p):
    def inner(n, curr):
        if curr == zero():
            return n
        return inner(n+1, curr[5:-1])
    return inner(0, p)

def convert(n):
    def inner(p):
        if evaluate(p) == n:
            return p
        return inner(succ(p))
    return inner(zero())

def add(p1, p2):
    def inner(p, op2):
        if p == zero():
            return op2
        if op2 == zero():
            return p
        return inner(succ(p), op2[5:-1])
    return inner(p1, p2)

def sub(p1, p2):
    def inner(p, op2):
        if op2 == zero():
            return p
        if p == zero() and op2 != zero():
            raise NegativeNumber
        return inner(p[5:-1], op2[5:-1])
    return inner(p1, p2)

def mult(p1, p2):
    def inner(p, op2):
        if op2 == succ(zero()):
            return p
        return inner(p.replace("0", p1), op2[5:-1])
    if p1 == zero() or p2 == zero(): 
        return zero()
    return inner(p1, p2)

def div(p1, p2):
    def inner(p, op1, op2):
        if op1 == zero():
            return p
        try:
            op1 = sub(op1, op2)
        except:
            return p
        return inner(succ(p), op1, op2)
    if p2 == zero():
        raise DivisionByZero
    return inner(zero(), p1, p2)