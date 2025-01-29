# Exam of Advanced Programming

###### 2025-01-29

## Exercise 1

Ruzzle is a grid (4×4) based game where each element of the grid is a letter and the aim of the game consists in determining all the possible English words out of all possible paths in the grid (where a path is a sequence of adjacent grid elements).

The exercise consists of writing a function ruzzles that calculates all the English words hidden in a given grid with the following simplifications/constraints:
- the minimum number length for a word is 3 characters;
- an entry is considered adjacent to another if it is immediately at left, at right, above or below it (no diagonals are considered); note that a word can also be hidden in the grid in its reversed form (i.e. it can be read from right to left);
- no entry can be considered twice in the same word;
- the words should be checked againts the ones contained in the `dictionary.txt` file;
- the list of resulting words must be alphabetically sorted.

The input is a list of 4-character strings where each string represents a row in the grid and their position in the list mimic the position in the grid.

### Test example:

```py
from ruzzle import *

if __name__ == '__main__':
    print(ruzzles(["walk", "moon", "hate", "rope"]))
    print(ruzzles(["abbr", "evia", "tion", "alba"]))
    print(ruzzles(["abse", "imtn", "nded", "ssen"]))
    print(ruzzles(["reca", "rwar", "aazp", "syon"]))
    print(ruzzles(["abst", "oine", "uesl", "snsp"]))
    print(ruzzles(["essx", "ndet", "sigh", "raen"]))
```

### Expected output:

```code
['alone', 'ate', 'atone', 'eta', 'hat', 'hate', 'knee', 'knot', 'law', 'lone', 'loom', 'lot', 'moat', 'moo', 'moon', 'moot', 'nee', 'net', 'not', 'note', 'oat', 'oaten', 'one', 'opt', 'pee', 'peen', 'rope', 'tee', 'ten', 'ton', 'tone', 'too', 'walk']
['ablate', 'ablation', 'ablative', 'alb', 'alit', 'alive', 'ate', 'ban', 'bio', 'boil', 'bra', 'bran', 'eta', 'evil', 'ion', 'late', 'lion', 'lit', 'lite', 'live', 'nab', 'naive', 'oblate', 'oil', 'ran', 'tali', 'tea', 'vet', 'via', 'vita', 'vital']
['abs', 'absent', 'absentee', 'absentminded', 'absentmindedness', 'aim', 'end', 'mind', 'minded', 'nee', 'need', 'needs', 'nest', 'see', 'seed', 'send', 'sent', 'tee', 'teen']
['ace', 'away', 'awe', 'car', 'caraway', 'carp', 'caw', 'err', 'race', 'racer', 'raceway', 'raw', 'rec', 'war', 'warp', 'way', 'ways', 'yaw', 'yon']
['abs', 'bin', 'bio', 'else', 'lens', 'let', 'net', 'nib', 'nibs', 'seine', 'sue', 'ten', 'tense']
['aegis', 'aid', 'aide', 'dig', 'dis', 'ear', 'end', 'gear', 'get', 'ides', 'near', 'nearsighted', 'nearsightedness', 'raid', 'send', 'set', 'side', 'sigh', 'sight', 'sighted']
```

## Exercise 2

In the *Peano Arithmetic* is possible to write any natural number with a costant symbol `0` and a unary function symbol `succ`, such that for every natural number *n* it can be represented by the composition of the `succ` function *n* times with parameter the costant symbol `0`, e.g. the number 2 will be represented as `succ(succ(0))`

The exercise consists of writing a Python module called `peano` containing the functions `add`, `sub`, `mult` and `div` implementing addition, subtraction, multiplication and integer division operations between two number in *Peano Arithmetic* respectively and two functions called `convert` and `evaluate`, where the former takes a natural number and return its representation in *Peano Arithmetic* and the latter the viceversa. The module must respect the following constraints:

- All the functions developed must be written using **functional programming**;
- It's forbidden to use any arithmetic operation and data representation related to integers or any numerical data type;
- It's forbidden to include any standard Python module;
- The functions must throw `NegativeNumber` and `DivisionByZero` exceptions when a negative number is obtained or when a division by 0 is executed;
- The `div` operation must truncate the decimal part of the result;

Probably you will need to implement some utility functions. The only arithmetic operation allowed is the `+1` inside the `evaluate` method.

All the solutions that use any Python module, that use any numerical data representation or operation or that don't use functional programming will be considered wrong.

### Test example:

```py
from peano import zero, succ, add, sub, mult, div, convert, evaluate

if __name__ == "__main__":
    z = zero()
    one = succ(zero())
    two = succ(succ(zero()))
    three = succ(succ(succ(zero())))
    print(f"Zero :- {z}\nOne :- {one}\nTwo :- {two}\nThree :- {three}\n")
    print(f"Zero :- {evaluate(z)}\nOne :- {evaluate(one)}\nTwo :- {evaluate(two)}\nThree :- {evaluate(three)}\n")

    print(f"15 + 8 = 23 :- {evaluate(add(convert(15), convert(8)))}")
    print(f"25 - 7 = 18 :- {evaluate(sub(convert(25), convert(7)))}")
    try:
        print(f"5 - 23 = -18 {evaluate(sub(convert(5), convert(23)))}")
    except NegativeNumber:
        print("Subtraction must return a positive number!")

    print(f"7 * 6 = 42 :- {evaluate(mult(convert(7), convert(8)))}")
    print(f"28 / 7 = 4 :- {evaluate(div(convert(28), convert(7)))}")
    print(f"25 / 2 = 12 :- {evaluate(div(convert(25), convert(2)))}")
```

### Output:

```code
Zero :- 0
One :- succ(0)
Two :- succ(succ(0))
Three :- succ(succ(succ(0)))

Zero :- 0
One :- 1
Two :- 2
Three :- 3

15 + 8 = 23 :- 23
27 - 5 = 18 :- 18
    raise NegativeNumber
NegativeNumber: Subtraction must return a positive number!
7 * 6 = 42 :- 42
28 / 7 = 4 := 4
25 / 2 = 12 := 12
```

**Note** that your program must be general and not tailored on the examples.