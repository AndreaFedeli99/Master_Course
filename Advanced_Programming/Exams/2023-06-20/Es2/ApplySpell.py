from Stack import Stack
from FullStack import FullStack
from EmptyStack import EmptyStack

from Gollum import Gollum
from Smeagol import Smeagol

def changeType(clsname, f):
    def wrapper(instance, *args, **kwargs):
        res = f(instance, *args, **kwargs)
        changeTypeCall[clsname](instance)
        return res
    return wrapper

def changeStackType(instance):
    if instance.__top__ == 0:
        instance.__class__ = EmptyStack
    if instance.__top__ == instance.__size__:
        instance.__class__ = FullStack
    if 0 < instance.__top__ < instance.__size__:
        instance.__class__ = Stack

def changeGollum(instance):
    if instance.hasTheOneRing:
        instance.__class__ = Gollum
    else:
        instance.__class__ = Smeagol

changeTypeCall = {
    Stack.__name__: changeStackType,
    FullStack.__name__: changeStackType,
    EmptyStack.__name__: changeStackType,
    Gollum.__name__: changeGollum,
    Smeagol.__name__: changeGollum
}

class ApplySpell(type):
    def __new__(self, clsname, supers, clsdict):
        new_clsdict = {}
        for attrkey, attrval in clsdict.items():
            new_clsdict[attrkey] = changeType(clsname, attrval) if callable(attrval) else attrval
        return super().__new__(self, clsname, supers, new_clsdict)
    
Stack = ApplySpell(Stack.__name__, Stack.__bases__, Stack.__dict__)
FullStack = ApplySpell(FullStack.__name__, FullStack.__bases__, FullStack.__dict__)
EmptyStack = ApplySpell(EmptyStack.__name__, EmptyStack.__bases__, EmptyStack.__dict__)

Gollum = ApplySpell(Gollum.__name__, Gollum.__bases__, Gollum.__dict__)
Smeagol = ApplySpell(Smeagol.__name__, Smeagol.__bases__, Smeagol.__dict__)
