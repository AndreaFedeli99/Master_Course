# Exam of Advanced Programming

###### 2024-07-01

## Exercise 1

To verify that a number is prime is considered a trivial task for a computer scientist. This is true when the number to check is pretty small (let's say if it is below or equal to 10000) but when the number to check grows larger the naive approach (namely trial division) tends to become slower and slower up to be intractable.

Fortunately in the years, several mathematicians proposed different alforithms to check the primality of big numbers. Just to cite a few *Lucas-Lehmer* and *Fermat's Little Theorem*.

The **Lucas-Lehmer** test works as follows. Let $M^p = 2^p-1$ be the *Mersenne number* to test with *p* an odd prime. The primality of *p* can be efficiently checked with a simple algorithm like trial division since *p* is exponentially smaller than $M^p$. Define a sequence { s_i } for all $i \geq 0$ by
```math
s_i = \begin{cases}
    4 & \text{if } i = 0\\
    s^2_{i-1} - 2 & \text{otherwise}
\end{cases}
```
Then $M^p$ is prime if and only if $s_{p-2} \equiv 0 \pmod{M^p}$. The number $s_{p-2} \pmod{M^p}$ is called the Lucas_Lehmer residue of *p*.

**Fermat's little theorem** states that if *p* is prime and $0 < a < p$, then $a^{p-1} \equiv 1 \pmod{p}$. If we want to test wheter *p* is prime, then we can pick random *a*'s in the interval and see whether the equality holds. If the equality does not hold for a value of *a*, then *p* is not prime. If the equality does hold for many values of *a*, then we can say that *p* is **probably** prime.

As you can notice, neither the Lucas-Lehmer's primality test nor the Fermat's Little Theorem provide a certain for all numbers. But in a case we cna use them to define the number as *probably* prime or *surely* not prime.

The exercise consists of implementing a module `primality` with (at least) 4 funtions: `trialdivision`, `lucaslehmer`, `littlefermat` and `is_prime`. Each of them is a predicate over an integer number (the one that should be tested as prime). The first three functions should implement the described algorithms. The last one is testing the primality of the input by applying one of the other algorithms according to the following rules:

- If the input is smaller or equal to 10001 it will use the trial division algorithm.
- If the input is between 10001 and 524280 (extremes included) it will us e the Lucas-Lehmer's algorithm (no check if the input is a Marsenne number).
- It will use the Fermat's little theorem otherwise (please use a reasonable set of values for *a* both in size and values).

**Note** that the given interfaces must be respected and your module should be compliant with the following main and its execution

### Test example:

```py
from primality import is_prime

def test_primes(vl):
    if len(vl) > 0:
        print(f"{vl[0]:14d} :- {is_prime(vl[0])}")
        test_primes(vl[1:])

if __name__ == "__main__":
    test_primes([25, 127, 8191, 131071, 524286, 524287, 524288, 2147483647])
```

### Expected output:

```
Trials-Division's Primality Test            25 :- False
Trials-Division's Primality Test           127 :- True
Trials-Division's Primality Test          8191 :- True
Lucas-Lehemer's Primality Test          131071 :- True
Little Fermat's Primality Test          524286 :- False
Little Fermat's Primality Test          524287 :- True
Little Fermat's Primality Test          524288 :- False
Little Fermat's Primality Test      2147483647 :- True
```

## Exercise 2

Often objects during their life cycle evolves sometimes changing their interface. Stack clearly shows this point:

- Initially the stack is empty and the `pop()` operation is unacceptable and similarly when it is full it cannot accept `push()` operations. Another example is a `Smeagol` that finding the one ring becomes a `Gollum` enabled just swallow and chant "my precious" every once and then.

Normally an object begins with a type and cannot change it without a complete re-installation. Python being a dynamic language is a little bit more flexible and permits to move one instance from a class to another without re-instantiating it. Of course, the messages an object can accept will change when its class changes.

These are the classes that should manifest such a behavior. This code has to be used verbatim and can't be edited:

```py
class Stack:
    def __init__(self, size):
        self.__size__ = size
        self.__top__ = 0
        self.__container__ = [0]*size

    def pop(self):
        self.__top__ -= 1
        return self.__container__[self.__top__]
    
    def push(self, e):
        self.__top__ += 1
        self.__container__[self.__top__-1] = e
    
    def __str__(self):
        return "type :- "+type(self).__name__+",\t\t"+str(self.__top__)+"/"+str(self.__size__)+\
            ",\tcontainer :- ["+', '.join(map(str, self.__container__[:self.__top__]))+']'
```

```py
class EmptyStack:
    def __init__(self, size):
        self.__size__ = size
        self.__top__ = 0
        self.__container__ = [0]*size
    
    def push(self, e):
        self.__top__ += 1
        self.__container__[self.__top__-1] = e
    
    def __str__(self):
        return "type :- "+type(self).__name__+",\t"+str(self.__top__)+"/"+str(self.__size__)+\
            ",\tcontainer :- ["+', '.join(map(str, self.__container__[:self.__top__]))+']'
```

```py
class FullStack:
    def __init__(self, size):
        self.__size__ = size
        self.__top__ = 0
        self.__container__ = [0]*size

    def pop(self):
        self.__top__ -= 1
        return self.__container__[self.__top__]
    
    def __str__(self):
        return "type :- "+type(self).__name__+",\t"+str(self.__top__)+"/"+str(self.__size__)+\
            ",\tcontainer :- ["+', '.join(map(str, self.__container__[:self.__top__]))+']'
```

```py
class Smeagol:
    def __init__(self):
        self.hasTheOneRing = False
    
    def found(self, what):
        if what == 'the one ring':
            self.hasTheOneRing = True
    
    def __str__(self):
        return "type :- " + type(self).__name__ + \
            ",\tRing " + ('🗸' if self.hasTheOneRing else 'x')
```

```py
class Gollum:
    def __init__(self):
        self.hasTheOneRing = True
    
    def chant(self): print("My Precious!!!")

    def swallow(self): print("gollllummmm!")

    def lose_the_ring(self): self.hasTheOneRing = False
    
    def __str__(self):
        return "type :- " + type(self).__name__ + \
            ",\t\tRing " + ('🗸' if self.hasTheOneRing else 'x')
```

The exercise consists of writing a metaclass `ApplySpell` that automatically changes an object class accordingly to some event, e.g., Smeagol gets the one ring, Gollum loses it or a Stack becomes empty/full. **NOTE** that the meta-class should be independent of the event that forces the change.

**Note, the use of any module is FORBIDDEN. The solution that use a module will be considered WRONG**.

```py
from FullStack import FullStack
from EmptyStack import EmptyStack
from Stack import Stack

from Smeagol import Smeagol
from Gollum import Gollum

from ApplySpell import *

if __name__ = "__main__":
    print("s should be a Stack!!!")
    s = Stack(5)
    print(s)
    for elem in [25, 5, 7, 16, 100]:
        s.push(elem)
        print(s)
    for _ in range(s.__size__):
        s.pop()
        print(s)
    print("s1 should be a FullStack!!!")
    s1 = FullStack(10)
    print(s1)
    try:
        s1.pop()
    except AttributeError as e:
        print(e)
    for elem in range(s1.__size__):
        s1.push(elem)
        print(s1)
    try:
        s1.push(-1)
    except AttributeError as e:
        print(e)
    
    print("Into the Middle-Earth")
    smeagol = Smeagol()
    try:
        for item in [ 'a key', 'a sword', 'the one ring', 'a loved one' ]:
            smeagol.found(item)
            print(smeagol)
    except AttributeError as e:
        print(e)
    smeagol.chant()
    smeagol.swallow()
    smeagol.swallow()
    smeagol.lose_the_ring()
    try:
        smeagol.chant()
    except AttributeError as e:
        print(e)
    print(smeagol)
```

### Output:

```code
s should be a Stack!!!
type :- EmptyStack,     0/5,    container :- []
type :- Stack,          1/5,    container :- [25]
type :- Stack,          2/5,    container :- [25, 5]
type :- Stack,          3/5,    container :- [25, 5, 7]
type :- Stack,          4/5,    container :- [25, 5, 7, 16]
type :- FullStack,      5/5,    container :- [25, 5, 7, 16, 100]
type :- Stack,          4/5,    container :- [25, 5, 7, 16]
type :- Stack,          3/5,    container :- [25, 5, 7]
type :- Stack,          2/5,    container :- [25, 5]
type :- Stack,          1/5,    container :- [25]
type :- EmptyStack,     0/5,    container :- []
s1 should be a FullStack!!!
type :- EmptyStack,     0/10,    container :- []
'EmptyStack' object has no attribute 'pop'
type :- Stack,          1/10,   container :- [0]
type :- Stack,          2/10,   container :- [0, 1]
type :- Stack,          3/10,   container :- [0, 1, 2]
type :- Stack,          4/10,   container :- [0, 1, 2, 3]
type :- Stack,          5/10,   container :- [0, 1, 2, 3, 4]
type :- Stack,          6/10,   container :- [0, 1, 2, 3, 4, 5]
type :- Stack,          7/10,   container :- [0, 1, 2, 3, 4, 5, 6]
type :- Stack,          8/10,   container :- [0, 1, 2, 3, 4, 5, 6, 7]
type :- Stack,          9/10,   container :- [0, 1, 2, 3, 4, 5, 6, 7, 8]
type :- Stack,          10/10,  container :- [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'FullStack' object has no attribute 'push'
Into the Middle-Earth
type :- Smeagol,        Ring x
type :- Smeagol,        Ring x
type :- Gollum,         Ring 🗸
'Gollum' object has no attribute 'found'
My Precious!!!
gollllummmm!
gollllummmm!
'Smeagol' object has no attribute 'chant'
type :- Smeagol,        Ring x
```

**Note** that your program must be general and not tailored on the examples.