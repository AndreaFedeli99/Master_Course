# Let us consider the class Person again and implement the following metaclasses:
# 2. The metaclass Spell that transforms the instances of Person in a Worker with the properties/descriptors of the previous exercise as real methods/attributes

from Worker import Worker
from datetime import date

class Spell(type):
    def __new__(cls, clsname, bases, attrs):
        def new_init(self, name, lastname, birthday, pph):
            self._name = name
            self._lastname = lastname
            self._birthday = birthday
            self._pay_per_hour = pph
            self.ds = self._pay_per_hour * self.wh_per_day
            self.ws = self._pay_per_hour * self.wh_per_day * self.wd_per_week
            self.ms = self._pay_per_hour * self.wh_per_day * self.wd_per_week * self.ww_per_month
            self.ys = self._pay_per_hour * self.wh_per_day * self.wd_per_week * self.ww_per_month * self.wm_per_year
        
        new_dict = Worker.__dict__.copy()
        new_dict['__init__'] = new_init
        return super().__new__(cls, Worker.__name__, Worker.__bases__, new_dict)

class Person(metaclass=Spell):
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
    p1 = Person('Andrea', 'Fedeli', date(1999, 6, 11), 10)
    
    print(p1.__class__.__bases__)
    print(p1)
    print(p1.day_salary_desc)