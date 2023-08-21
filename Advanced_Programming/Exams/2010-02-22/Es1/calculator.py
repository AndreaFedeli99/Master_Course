from collections import deque

operators = {
    '+': lambda x,y: x + y,
    '-': lambda x,y: x - y,
    '*': lambda x,y: x * y,
    '/': lambda x,y: x / y
}

class calculator:
    def __init__(self, exp):
        self.expr = exp
    
    def eval(self):
        def compute(str, stack):
            if len(str) == 0:
                return stack.pop()
            
            ch = str[-1]
            if ch in operators:
                op1 = stack.pop()
                op2 = stack.pop()

                stack.append(operators[ch](op1, op2))
                return compute(str[:-1], stack)
            else:
                stack.append(int(ch))
                return compute(str[:-1], stack)
        
        return compute(self.expr, deque())

    def code(self):
        def build(str, stack):
            if len(str) == 0:
                return stack.pop()
            
            ch = str[-1]
            if ch in operators:
                op1 = stack.pop()
                op2 = stack.pop()

                stack.append("(" + op1 + ch + op2 + ")")
                return build(str[:-1], stack)
            else:
                stack.append(ch)
                return build(str[:-1], stack)
        return build(self.expr, deque())