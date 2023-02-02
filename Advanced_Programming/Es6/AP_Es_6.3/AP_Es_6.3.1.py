# Let us consider the class Person again and implement the following metaclasses:
# 1. The metaclass Counter which counts how many times Person has been instantiated

from datetime import date

class Counter(type):
    _instances_count = 0

    def __call__(cls, *args):
        Counter._instances_count += 1
        return super().__call__(*args)
    
    def get_instance_count(cls):
        return cls._instances_count
    
class Person(metaclass=Counter):
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

if __name__ == "__main__":
    print(Person.get_instance_count())

    p1 = Person('Andrea', 'Fedeli', date(1999, 6, 11))
    print(Person.get_instance_count())

    p2 = Person('Paolo', 'Rossi', date(1800, 1, 1))
    p3 = Person('Mario', 'Mario', date(1985, 7, 13))
    print(Person.get_instance_count())