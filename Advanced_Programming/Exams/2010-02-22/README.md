# Exam of Advanced Programming

###### 2010-02-22

## Exercise 1

Let us consider a small language for expression with the binary operators `+, -, *, /` (with the obvious meaning) and the operands `0, 1, ..., 9` (note that an expression can only have figures from 0 to 9 but the intermediate and final results can be greater than this). To simplify the expressions are written in polish notation, i.e., all the operators come before of their operands (e.g., `(3+4)*5)` is equal to `*+345`).

An expression can be mathematical evaluated or converted in a stack-based assembler with the following statements: `store n`, `add`, `sub`, `mul`, `div` where `store n` will push on the stack the value of `n` and the other statements pop the two elements on the top and push the result on the top.

Write a `calculator` class with the methods:

- `__init__` that takes a string representing the expression in polish notion.
- `eval` with no args that mathematical evaluates the expression used in the constructor and returns the result.
- `code` with no args that generates the assembler corresponding to the expression and returns it as a string with a statement per row.

Of course the use of `eval` is forbidden and all the passed expressions are correct so no checks on inputs are necessary.

### Test example:

```py
from calculator import *

calc = calculator('+2*-53/63')
print(calc.eval())
print(calc.code(), end='')
```

Note that, closures, recursion and dictionaries can help a lot.

### Expected output:

```
6.0
(2+((5-3)*(6/3)))
```

## Exercise 2

Sometimes is necessary to delay the execution of a method until a condition is verified, e.g., in cryptography when two keys are necessary to decrypt a text we have to wait that the `decrypt` method is called with both keys.

A similar behavior can be achieved by really calling the method only after a given number of calls on a rearrangement of the **whole** set of passed arguments.

Implements such a behaviour through a **parametric** decorator `multi-triggered`. Such a decorator should have a couple of parameters: the first expresses how many times the method should be call before being really activated, the second is a function which applies on the values used in each call for each parameter. Of course we are speaking about decorators applicable on method not class definitions.

### Test example:

```py
from multi_triggered import *

class ToBeMultiTriggered:
    def m1(self): print("### m1 has been called!")
    @multi_triggered(2, lambda x, y: x*y)
    def m2(self, i): print("### m2({0}) has been called!".format(i))
    @multi_triggered(3, lambda x, y: x+y)
    def m3(self, x, y): print("### m3({0}, {1}) has been called!".format(x,y))

if __name__ == "__main__":
    to_be = ToBeMultiTriggered()
    to_be.m1()
    to_be.m2(5)
    to_be.m3('a', 3)
    to_be.m2(7)
    to_be.m3('b', 5)
    to_be.m2(3)
    to_be.m3('c', 7)
```

### Expected output:

```
### m1 has been called!
### m2(35) has been called!
### m3(abc, 15) has been called!
```

## Exercise 3

There are two kinds of positive numbers: prime numbers and composite numbers. A composite number is the product of a sequence of prime numbers. You can write a simple **generator**, named `prime_factors` to factor numbers and yield each prime factor of the number; the generators take as an input the number to factor and returns the prime factors from the smallest to the largest. 

Note that, a simple-looking for-loop shall not work; the prime factor of 128 is 2, repeated 7 times. Note also that 1 is not a factor or better is always a factor so can be excluded by the list.

### Test example:

```py
from prime_factors import *

def print_factors(n):
    print("The prime factors of {0} are:".format(n))
    for n in prime_factors(n):
        print(n, end=' ')
    print()

if __name__ == '__main__':
    print_factors(128)
    print_factors(9999)
    print_factors(123456789)
```

### Expected output:

```
The prime factors of 128 are:
2 2 2 2 2 2 2
The prime factors of 9999 are:
3 3 11 101
The prime factors of 123456789 are:
3 3 3607 3803
```