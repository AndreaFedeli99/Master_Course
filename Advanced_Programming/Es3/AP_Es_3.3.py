# Write a PolishCalculator class that implements a stack-based calculator that adopts polish notation for the expressions to be evaluated.

# Polish Notation is a prefix notation wherein every operator follows all of its operands; this notation has the big advantage of being unambiguous and permits to avoid the use of parenthesis. E.g., (3+4)*5 is equal to 3 4 + 5 *.

# An instance of the PolishCalculator class will understand the following API:
#   __init(self)__ with the obvious meaning
#   __str(self)__ which will format the expression in the corresponding infix notation
#   eval(str) which will evaluate the expression contained in the string str and written in the polish notation

# The recognized operators are +, - (both unary and binary), *, /, ** over integers and floats, or, and and not over booleans. At least a space ends each operands and operators, T and F respectively represent True and False.

# Hint. The evaluation/translation can be realized by pushing the recognized elements on a stack.

import operator
from collections import deque
from inspect import signature
from functools import reduce

class PolishCalculator:
    def __init__(self):
        self._add_unary = lambda val: val
        self._operator_map = {'+': lambda len: self._add_unary if len == 1 else operator.add,
                                '-': lambda len: operator.neg if len == 1 else operator.sub,
                                '*': lambda len: operator.mul,
                                '/': lambda len: operator.truediv,
                                '**': lambda len: operator.pow,
                                'and': lambda len: operator.and_,
                                'or': lambda len: operator.or_,
                                'not': lambda len: operator.not_
                            }
        self._boolean_parse = {'T': True, 'F': False}
        self._exp_stack = deque()
        self._exp_items = []

    def __str__(self):
        try:
            return reduce(lambda stack, c : 
                # not operator
                (c == "not") and (stack[:-1]+["{0} {1}".format(c, stack[-1])]) or
                # unary '-' and '+' operator
                (c == "-" or c == "+") and (len(stack[1:]) == 0) and (stack[:-1]+["({0}{1})".format(c, stack[-1])]) or
                # other operator
                (c in self._operator_map.keys()) and (stack[:-2]+["({0} {1} {2})".format(stack[-2],c, stack[-1])]) or
                # all operand
                stack+[c], 
            self._exp_items[1:], 
            [self._exp_items[0]])[0]
        except Exception as e:
            return f"Failed to evaluate the expression: {e}"

    def _get_operator_cardinality(self, op, stack):
        return len(signature(self._operator_map[op](len(stack))).parameters)

    def eval(self, str):
        self._exp_items = str.split(' ')
        eval_item = None
        result = None
        try:
            for item in self._exp_items:
                if item in self._operator_map:
                    # evaluate the current operator by popping the operands from the exporession's stack
                    # NOTE: the number of element to pop is established by the number of operator's arguments
                    operand_num = self._get_operator_cardinality(item, self._exp_stack)
                    eval_item = self._operator_map[item](operand_num)(*reversed([self._exp_stack.pop() for i in range(operand_num)]))
                elif item in self._boolean_parse:
                    eval_item = self._boolean_parse[item]
                else:
                    eval_item = float(item)
                self._exp_stack.append(eval_item)
            if len(self._exp_stack) == 1:
                result = self._exp_stack.pop()
            else:
                raise ValueError("wrong number of operand")
        except Exception as e:
            return f"Failed to evaluate the expression: {e}"
        finally:
            self._exp_stack.clear()
        return result

calculator = PolishCalculator()
print(calculator.eval("3 4 + 5 *"))
print("{0}{1}".format(calculator, "\n"))

print(calculator.eval("T F and T or not"))
print("{0}{1}".format(calculator, "\n"))

print(calculator.eval("4 -"))
print("{0}{1}".format(calculator, "\n"))

print(calculator.eval("T not"))
print(calculator)