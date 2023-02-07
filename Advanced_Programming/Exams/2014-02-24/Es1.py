operators = {'+': lambda sx, dx: sx + dx,
             '-': lambda sx, dx: sx - dx,
             '*': lambda sx, dx: sx * dx,
             '/': lambda sx, dx: sx // dx }

class leaf:
    def __init__(self, value):
        self.__value = value
    def eval(self):
        return int(self.__value)
    def combine(self):
        return self
    def __str__(self):
        return self.__value

def make_node(op, name):
    class node:
        def __init__(self, sx, dx):
            self.__sx = sx
            self.__dx = dx
        def eval(self):
            return op(self.__sx.eval(), self.__dx.eval())
        def combine(self):
            if isinstance(self.__sx, leaf) and isinstance(self.__dx, leaf):
                return leaf(str(self.eval()))
            else:
                self.__sx = self.__sx.combine()
                self.__dx = self.__dx.combine()
                return self
        def __str__(self):
            return "(" + self.__sx.__str__() + name + self.__dx.__str__() + ")"
    return node

translator = {op:make_node(fop, op) for op, fop in operators.items()}
translator.update({str(x): leaf(str(x)) for x in range(10)})

class calculator:
    def __init__(self, expr):
        self.__root, dropped = self.__convert(expr, 0)
    def is_value(self):
        return isinstance(self.__root, leaf)
    def __convert(self, expr, n):
        if n < len(expr):
            if expr[n] in {'+', '-', '*', '/'}:
                sx,n1 = self.__convert(expr, n+1)
                dx,n2 = self.__convert(expr, n1+1)
                return translator[expr[n]](sx,dx), n2
            else:
                return translator[expr[n]], n
    def combine(self):
        self.__root = self.__root.combine()
        return self
    def eval(self):
        return self.__root.eval()
    def __str__(self):
        return self.__root.__str__()

def print_reduction(calc):
    print(calc)
    if not calc.is_value(): print_reduction(calc.combine())

if __name__ == "__main__":
    expressions = ["+34", "+3-15", "*+34-23", "+7++34+23",
        "*+*34-34/6-35", "/+-81*45*/93/52", "*+/12/14-2/32", "+2*-53/63"]
    [print_reduction(calculator(expr)) for expr in expressions]