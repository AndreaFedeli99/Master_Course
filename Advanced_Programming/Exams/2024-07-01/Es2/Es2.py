from FullStack import FullStack
from EmptyStack import EmptyStack
from Stack import Stack

from Smeagol import Smeagol
from Gollum import Gollum

from ApplySpell import *

if __name__ == "__main__":
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
