# Exam of Advanced Programming

###### 2023-07-18

## Exercise 1

You must define a module named `ireduction` this **MUST** define:

- A class `calculator` whose instances represent an expression parsed out from a string and permits all the basic operation on such an expression

- Such a class should be an iterator that at each iteration will reply with the next simplification of the expression used to instantiate the iterator.

The following is an example of usage and the expected behavior.

```py
from ireduction import calculator

if __name__ == "__main__":
    expression = [
        "+34", "+3-15", "*+34-23", "+7++34+23", "*^72", "-^2*32^5+23",
        "*+*34-34/6-35", "/+-81*45*/93/52", "*+/12/14-2/32", "+2*-53/63"]
    for expr in expression:
        c = calculator(expr)
        print('-----------------------------')
        print(c)
        while True:
            try:
                next(c)
            except StopIteration: break
            print(c)
        print('-----------------------------')
```

### Output:

```
-----------------------------
(3+4)
7
-----------------------------
(3+(1-5))
(3+-4)
-1
-----------------------------
((3+4)*(2-3))
(7*-1)
-7
-----------------------------
(7+((3+4)+(2+3)))
(7+(7+5))
(7+12)
19
-----------------------------
(7^2)
49
-----------------------------
((2^(3*2))-(5^(2+3)))
((2^6)-(5^5))
(64-3125)
-3061
-----------------------------
(((3*4)+(3-4))*(6/(3-5)))
((12+-1)*(6/-2))
(11*-3)
-33
-----------------------------
```

## Exercise 2

This is a variant of a game we had done in our childhood. Players take turns naming animals. Each animal chosen must begin with the same letter that ended the previous element (repetitions are not allowed). The game begins with any arbitrary animal chosen by a player 1 and ends when a player loses because he or she is unable to continue.

The exercise consists of writing a function `genchain` that calculates, given an animal name, the logest (or the shortest) possible path (measured in terms of number of words) yielded following the above rules. Note that when the longest (or the shortest) path is not unique the solution must be chosen as sorted in lexicographical order.

In the exercise take in conisderation only the animals in a given file called `animals.txt`.

The following is an example of the expected behavior.

```py
from genchain import genchain

if __name__ == "__main__":
    print("longest {0}  :- {1}".format('turtle', genchain('turtle')))
    print("shortest {0} :- {1}".format('turtle', genchain('turtle', min)))
    print("longest {0}  :- {1}".format('aardvark', genchain('aardvark')))
    print("shortest {0} :- {1}".format('aardvark', genchain('aardvark', min)))
    print("longest {0}  :- {1}".format('tiger', genchain('tiger')))
    print("shortest {0} :- {1}".format('tiger', genchain('tiger', min)))
    print("longest {0}  :- {1}".format('alligator', genchain('alligator')))
    print("shortest {0} :- {1}".format('alligator', genchain('alligator', min)))
    print("longest {0}  :- {1}".format('fish', genchain('fish')))
    print("shortest {0} :- {1}".format('fish', genchain('fish', min)))
    print("longest {0}  :- {1}".format('scorpion', genchain('scorpion')))
    print("shortest {0} :- {1}".format('scorpion', genchain('scorpion', min)))
    print("longest {0}  :- {1}".format('crocodile', genchain('crocodile')))
    print("shortest {0} :- {1}".format('crocodile', genchain('crocodile', min)))
```

### Output:

```
longest turtle :- ['turtle', 'eagle', 'elephant', 'tiger', 'rabbit']
shortest turtle :- ['turtle', 'elephant', 'tiger', 'rabbit']
longest aardvark :- ['aardvark', 'kangaroo', 'octopus', 'sheep', 'pig', 'goldfish', 'hippopotamus', ]
shortest aardvark :- ['aardvark', 'kitten']
longest tiger :- ['tiger', 'rabbit', 'turtle', 'eagle', 'elephant']
shortest tiger :- ['tiger', 'rabbit', 'turtle', 'elephant']
longest alligator :- ['alligator', 'rabbit', 'tiger', 'rat', 'turtle', 'eagle', 'elephant', ]
shortest alligator :- ['alligator', 'rabbit', 'tiger', 'rat', 'turtle', 'elephant']
longest fish :- ['fish', 'hippopotamus', 'shark', 'kangaroo', 'octopus', 'sheep', 'pig', ]
shortest fish :- ['fish', 'hippopotamus', 'scorpion']
longest scropion :- ['scorpion']
shortest scropion :- ['scorpion']
longest crocodile :- ['crocodile', 'eagle', 'elephant', 'tiger', 'rabbit', 'turtle']
shortest crocodile :- ['crocodile', 'eagle', 'elephant', 'turtle']
```