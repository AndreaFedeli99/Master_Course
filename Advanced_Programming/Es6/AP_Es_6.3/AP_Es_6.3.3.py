# Let us consider the class Person again and implement the following metaclasses:
# 3. The metaclass MultiTriggeredMethod that let activate a method only when called twice

from types import FunctionType
from datetime import date

def trigger(method):
    calls = 0
    def onCall(*args):
        nonlocal calls
        calls += 1
        if calls == 2:
            calls = 0
            return method(*args)
    return onCall

class MultiTriggeredMethod(type):
    def __new__(cls, clsname, bases, attrs):
        for attr, attrval in attrs.items():
            if type(attrval) is FunctionType and not attr.startswith('__'):
                attrs[attr] = trigger(attrval)
        return super().__new__(cls, clsname, bases, attrs)

class Person(metaclass=MultiTriggeredMethod):
    def __init__(self, name, lastname, birthday):
        self._name = name
        self._lastname = lastname
        self._birthday = birthday
    
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
    
    def get_lastname(self):
        return self._lastname
    
    def set_lastname(self, lastname):
        self._lastname = lastname
    
    def get_birthday(self):
        return self._birthday

    def set_birthday(self, birthday):
        self._birthday = birthday

    def __repr__(self):
        return self._name + ' ' + self._lastname + ', ' + str(self._birthday)

if __name__ == '__main__':
    p1 = Person('Andrea', 'Fedeli', date(1999, 6, 11))
    
    print("After 1st call of Person.get_name")
    print(f"{p1.get_name()}\n")

    print("After 1st call of Person.set_lastname")
    p1.set_lastname('X')
    print(f"{p1}\n")

    print("After 2nd call of Person.get_name")
    print(f"{p1.get_name()}\n")

    print("After 2nd call of Person.set_lastname")
    p1.set_lastname('X')
    print(p1)