# Exam of Advanced Programming

###### 2014-02-24

## Exercise 1

- Define a class `calculator` whose instances represent an expression parsed out from a string and permits all the basic operations on such an expression.
- Define a function `print_reduction` that given an instance of `calculator` can evaluate the expression step by step (printing all the intermediate results).

The solution must respect the following constraints:  
- The only admitted operations are `+, -, *` and `/` with the traditional meaning.
- The only available type is `int`.
- To simplify the parsing, the expressions must be written in polish notation and numbers in the initial expression are only 1-figure positive integers.

##### Note: Polish notation is a form of notation for expressions that places operators to the left of their operands without the use of brackets.

### Test example:

```py
if __name__ == "__main__":
    expressions = ["+34", "+3-15", "*+34-23", "+7++34+23",
        "*+*34-34/6-35", "/+-81*45*/93/52", "*+/12/14-2/32", "+2*-53/63"]
    [print_reduction(calculator(expr)) for expr in expressions]
```

### Expected output:

```code
(3+4)
7
(3+(1-5))
(3+-4)
-1
((3+4)*(2-3))
(7*-1)
-7
(7+((3+4)+(2+3)))
(7+(7+5))
(7+12)
19
(((3*4)+(3-4))*(6/(3-5)))
((12+-1)*(6/-2))
(11*-3)
-33
(((8-1)+(4*5))/((9/3)*(5/2)))
((7+20)/(3*2))
(27/6)
4
(((1/2)+(1/4))*(2-(3/2)))
((0+0)*(2-1))
(0*1)
0
(2+((5-3)*(6/3)))
(2+(2*2))
(2+4)
6
```

## Exercise 2

The reflected binary code, also known as **Gray code**, is a binary numeral system where two successive values differ in only one bit. More formally, a Gray code is a code assigning to each of a a contiguous set of integers, or to each member of a circular list, a word of symbols such that each two adjacent code words differ by one symbol.

There can be more than one Gray code for a given word length, but the term was first applied to a particular binary code for the non-negative integers, the *binary-reflected Gray code*, or **BRGC**.

Here is shown the three-bit version:
<table>
  <tr>
    <th>Decimal</th>
    <th>Gray</th>
    <th>Binary</th>
  </tr>
  <tr>
    <td>0</td>
    <td>000</td>
    <td>000</td>
  </tr>
  <tr>
    <td>1</td>
    <td>001</td>
    <td>010</td>
  </tr>
  <tr>
    <td>2</td>
    <td>011</td>
    <td>010</td>
  </tr>
  <tr>
    <td>3</td>
    <td>010</td>
    <td>011</td>
  </tr>
  <tr>
    <td>4</td>
    <td>110</td>
    <td>100</td>
  </tr>
  <tr>
    <td>5</td>
    <td>111</td>
    <td>101</td>
  </tr>
  <tr>
    <td>6</td>
    <td>101</td>
    <td>110</td>
  </tr>
  <tr>
    <td>7</td>
    <td>100</td>
    <td>111</td>
  </tr>
</table>

Implement two functions `gray` and `mgray` that took an integer `n` and return a generator with complete Gray code of lenght `n`. The difference beetween the two versions is that the second one stores and reuses previously calculated sequences.

The solution must respect the following constraints:
- Both implementations should be **recursive**.
- Storing and reusing of previously calculated sequences should be introduced via a decorator or a meta-class.

### Test example:

```py
if __name__ == "__main__":
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
```

### Expected output:

```code
GC(1) :- 0 1
GC(2) :- 00 01 11 10
GC(3) :- 000 001 011 010 110 111 101 100
GC(4) :- 0000 0001 0011 0010 0110 0111 0101 0100 1100 1101 1111 1110 1010 1011 1001 1000
GC_(1) :- 0 1
GC_(2) :-
### cached value for (1,) --> ['0', '1']
00 01 11 10
GC_(3) :-
### cached value for (2,) --> ['00', '01', '11', '10']
000 001 011 010 110 111 101 100
GC_(4) :-
### cached value for (3,) --> ['000', '001', '011', '010', '110', '111', '101', '100']
0000 0001 0011 0010 0110 0111 0101 0100 1100 1101 1111 1110 1010 1011 1001 1000
```