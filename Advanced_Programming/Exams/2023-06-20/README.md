# Exam of Advanced Programming

###### 2023-06-20

## Exercise 1

**Wordle** is a deceptively simple word puzzle. You're asked to guess the word of the day, which is a five-letter word id English. Wordle basic characteristics canbe summarized in:

- The word is exactly five letters long.
- It is in English and composed of letters, no punctuation, no numbers or other symbols.
- Only 6 guessing are possible for each hidden word.

A guess yields clues:

- A green letter if the character and position in the word is correct.
- A yellow letter if the character is present in the word, but we chose the wrong position.
- A white letter if the character in not in the word at all.

Both hidden and guessed words are/should be taken from a finite number of words, and what is a valid word is limited to the dictionary used by Wordle.

In this exercise, you are asked to write a module `wordle` to automatically play the puzzle. To this respect, we simplify some aspects:

- Only the first guess is given as a starting point all the other guessing are automatically chosen by your implementation.
- Any new guess should be the first one (alphabetically sorted) among those that could fit the hints provided by the oracle.
- The number of guessing is unlimited.

As a dictionary you have the file called `wordlist-worlde.txt`. **Note** that this is a full dictionary, e.i. it contains words of any length and with any character.

The `wordle.py` module must contain (at least) the functions:

- `read_words(fn)` that reads and organizes the dictionary.
- `wordle(guess, wordle, dictionary)` that is in charge of solving the puzzle. It takes the first guess, the hidden word and the dictionary read by the `read_words` funtion, respectively, and returns a list of colored words from the given guess (in position zero) to the hidden word (in the last spot) in the exact order you guessed them.

**Technical Note.** You can ouput colored letters by using ANSI escape codes. For your convenience the following are those that you need:

- White: `\u001b[37;1m`
- Green: `\u001b[32;1m`
- Yellow: `\u001b[33;1m`
- Reset: `\u001b[0m`

A piece of text is printed in a certain color when the corresponding escape code is encountered; the color is maintained until a reset escape code is encountered.

Note that the use of any module is **FORBIDDEN**. The solutions that use a module will be considered **WRONG**.

The following is a main program exercising the module and the expected result. **Note** that any solution whose behaviour differs from this one will be considered **WRONG**.

```py
from wordle import read_words, wordle

def print_wordlet(wordlet):
    for w in wordlet:
        print(w)
    print("\n")

if __name__ == '__main__':
    wl = read_words('wordlist-worlde.txt')
    print_wordlet(wordle('model', 'melon', wl))
    print_wordlet(wordle('slice', 'mount', wl))
    print_wordlet(wordle('crane', 'vowel', wl))
    print_wordlet(wordle('drive', 'sooty', wl))
    print_wordlet(wordle('yacht', 'sassy', wl))
    print_wordlet(wordle('happy', 'roots', wl))
    print_wordlet(wordle('lines', 'hatch', wl))
```

### Output:

```code
model
melon

slice
abaft
donut
mount

crane
bepop
domed
fogey
hotel
vowel

drive
aback
floss
shoot
sooty

yacht
badly
fairy
gamey
jazzy
nanny
pappy
sassy

happy
bedim
clock
front
roots

lines
aback
catch
hatch
```

## Exercise 2

Often objects during their life cycle evolves sometimes changing their interface. Stack clearly shows this point:

- Initially the stack is empty and the `pop()` operation is unacceptable and similarly when it is full it cannot accept `push()` operations. Another example is a `Smeagol` that finding the one ring becomes a `Gollum` enabled just swallow and chant "my precious" eveny once and then.

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
        return self.__container_[self.__top__]
    
    def push(self, e):
        self.__top__ += 1
        self.__container__[self.__top__-1] = e
    
    def __str__(self):
        return "type :- "+type(self).__name__+",\   "+str(self.__top__)+str(self.__size__)+\\
            ",\   container :- ["+', '.join(map(str, self.__container__[:self.__top__]))+']'

class EmptyStack:
    def __init__(self, size):
        self.__size__ = size
        self.__top__ = 0
        self.__container__ = [0]*size
    
    def push(self, e):
        self.__top__ += 1
        self.__container__[self.__top__-1] = e
    
    def __str__(self):
        return "type :- "+type(self).__name__+",\   "+str(self.__top__)+str(self.__size__)+\\
            ",\   container :- ["+', '.join(map(str, self.__container__[:self.__top__]))+']'

class FullStack:
    def __init__(self, size):
        self.__size__ = size
        self.__top__ = 0
        self.__container__ = [0]*size

    def pop(self):
        self.__top__ -= 1
        return self.__container_[self.__top__]
    
    def __str__(self):
        return "type :- "+type(self).__name__+",\   "+str(self.__top__)+str(self.__size__)+\\
            ",\   container :- ["+', '.join(map(str, self.__container__[:self.__top__]))+']'

class Smeagol:
    def __init__(self):
        self.hasTheRing = False
    
    def found(self, what):
        if what == 'the one ring':
            self.hasTheRing = True
    
    def __str__(self):
        return "type :- "+type(self).__name__+",\ Ring "+('🗸' if self.hasTheOneRing else 'x')

class Gollum:
    def __init__(self):
        self.hasTheRing = True
    
    def chant(self): print("My Precious!!!")

    def swallow(self): print("gollllummmm!")

    def lose_the_ring(self): self.hasTheOneRing = False
    
    def __str__(self):
        return "type :- "+type(self).__name__+",\ Ring "+('🗸' if self.hasTheOneRing else 'x')
```

The exercise consists of writing a metaclass `ApplySpell` that automatically changes an object class accordingly to some event, e.g., Smeagol gets the one ring, Gollum loses it or a Stack becomes empty/full. NOte that the meta-class should be independent of the event that forces the change.

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
    print("s1 should be a FullyStack!!!")
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