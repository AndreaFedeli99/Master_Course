import types

from FullStack import FullStack
from EmptyStack import EmptyStack
from Stack import Stack

from Smeagol import Smeagol
from Gollum import Gollum

def changeStack(f):
    def inner(*args):
        assert type(args[0]) is Stack or type(args[0]) is FullStack or type(args[0]) is EmptyStack, \
            f"{args[0]} MUST be a {Stack.__name__}, {FullStack.__name__} or {EmptyStack.__name__} instance"
        res = f(*args)
        if args[0].__top__ == args[0].__size__:
            args[0].__class__ = FullStack
        elif args[0].__top__ > 0:
            args[0].__class__ = Stack
        else:
            args[0].__class__ = EmptyStack
        return res
    return inner

def changeGollum(f):
    def inner(*args):
        assert type(args[0]) is Gollum or type(args[0]) is Smeagol, \
            f"{args[0]} MUST be a {Gollum.__name__} or {Smeagol.__name__} instance"
        res = f(*args)
        if args[0].hasTheOneRing:
            args[0].__class__ = Gollum
        else:
            args[0].__class__ = Smeagol
        return res
    return inner

type_decorator = {
    Stack.__name__: changeStack,
    EmptyStack.__name__: changeStack,
    FullStack.__name__: changeStack,
    Gollum.__name__: changeGollum,
    Smeagol.__name__: changeGollum
}

class ApplySpell(type):
    def __new__(self, clsname, supers, clsdict):
        new_dict = dict(clsdict)
        for attr, attrval in new_dict.items():
            if callable(attrval):
                new_dict[attr] = type_decorator[clsname](attrval)
                
        return type.__new__(self, clsname, supers, new_dict)

Stack = ApplySpell(Stack.__name__, Stack.__bases__, Stack.__dict__)
EmptyStack = ApplySpell(EmptyStack.__name__, EmptyStack.__bases__, EmptyStack.__dict__)
FullStack = ApplySpell(FullStack.__name__, FullStack.__bases__, FullStack.__dict__)

Gollum = ApplySpell(Gollum.__name__, Gollum.__bases__, Gollum.__dict__)
Smeagol = ApplySpell(Smeagol.__name__, Smeagol.__bases__, Smeagol.__dict__)