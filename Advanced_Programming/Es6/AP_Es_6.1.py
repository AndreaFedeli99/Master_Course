# Let us consider a class Person with the following attributes: name, lastname, birthday with the obvious meaning and the corresponding setter and getters and the __repr__ to print it.

# 1. Extend the class Person in the class Student by adding a dictionary lectures with the lecture name as a key and the mark as a value, and the property grade_average to calculate the marks average
# 2. Extend the class Person in the class Worker by adding an attribute pay_per_hour and the properties day_salary, week_salary, month_salary, and year_salary
#    considering 8 working hours a day, 5 working days a week, 4 weeks a month, 12 months a year; note that to set one of the properties implies to recalculate the pay_per_hour value
# 3. Extend the class Person in the class Wizard by adding a property age that when used as a getter calculates the correct age in term of passed days from the 
#    birthday to the current day and when used as a setter it will change the birthday accordingly rejuvenating or getting old magically.

# Repeat the exercise by using the descriptors instead of the properties.

from datetime import date, timedelta
from functools import reduce

class Person:
    
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

class Student(Person):

    def __init__(self, name, lastname, birthday, lectures):
        super().__init__(name, lastname, birthday)
        self.__lectures = lectures

    def get_lectures(self):
        return self.__lectures

    def set_lectures(self, l):
        self.__lectures = l

    def calculate_average(self):
        return reduce(lambda m1, m2: m1 + m2, self.__lectures.values()) / len(self.__lectures.keys()) 

    def remove_lectures(self):
        self.__lectures = {}

    def __repr__(self):
        return super().__repr__() + ", subjects: " + str(self.get_lectures())

    grade_average = property(calculate_average, None, remove_lectures, "Manage the marks average")

class Worker(Person):

    wh_per_day = 8
    wd_per_week = 5
    ww_per_month = 4
    wm_per_year = 12

    def __init__(self, name, lastname, birthday, pay_per_hour):
        super().__init__(name, lastname, birthday)
        self.__pay_per_hour = pay_per_hour

    def get_pay_per_hour(self):
        return self.__pay_per_hour

    def set_pay_per_hour(self, pph):
        self.__pay_per_hour = pph

    def compute_total_pay(time):
        def compute(self):
            return self.__pay_per_hour * time
        return compute
    
    def update_pay_per_hour(time):
        def update(self, total):
            self.__pay_per_hour = total / time
        return update
    
    def zeroing_pay_per_hour(self):
        self.__pay_per_hour = 0

    def __repr__(self):
        return super().__repr__() + ", pph: " + str(self.get_pay_per_hour())

    day_salary = property(compute_total_pay(wh_per_day), update_pay_per_hour(wh_per_day), zeroing_pay_per_hour, "Manage the day salary")
    week_salary = property(compute_total_pay(wh_per_day * wd_per_week), 
                            update_pay_per_hour(wh_per_day * wd_per_week), 
                            zeroing_pay_per_hour, 
                            "Manage the week salary")
    month_salary = property(compute_total_pay(wh_per_day * wd_per_week * ww_per_month), 
                            update_pay_per_hour(wh_per_day * wd_per_week * ww_per_month), 
                            zeroing_pay_per_hour, 
                            "Manage the month salary")
    year_salary = property(compute_total_pay(wh_per_day * wd_per_week * ww_per_month * wm_per_year), 
                            update_pay_per_hour(wh_per_day * wd_per_week*ww_per_month * wm_per_year), 
                            zeroing_pay_per_hour, 
                            "Manage the year salary")

class Wizard(Person):

    def __init__(self, name, lastname, birthday):
        super().__init__(name, lastname, birthday)
    
    def get_age(self):
        return (date.today() - self._birthday).days

    def set_age(self, days):
        self.set_birthday(date.today() - timedelta(days))

    def __repr__(self):
        return super().__repr__() + ", age: " + str(self.age)
    
    age = property(get_age, set_age, None, "Manage the age")


if __name__ == '__main__':
    s = Student('James', 'Brown', date(1997, 5, 17), {'coding': 20, 'operative sistems': 25, 'alghoritms and complexity': 30})
    wor = Worker('Joe', 'Black', date(1978, 2, 21), 9.5)
    wiz = Wizard('David', 'Copperfield', date(1956, 9, 16))

    print(s)
    print(f"Marks average: {s.grade_average}")

    print()

    print(wor)
    print(f"Day salary: {wor.day_salary}")
    print(f"Week salary: {wor.week_salary}")
    print(f"Month salary: {wor.month_salary}")
    print(f"Year salary: {wor.year_salary}")

    print()

    wor.day_salary = 3
    print(wor)
    print(f"Day salary: {wor.day_salary}")
    print(f"Week salary: {wor.week_salary}")
    print(f"Month salary: {wor.month_salary}")
    print(f"Year salary: {wor.year_salary}")

    print()

    print(wiz)
    wiz.age = 1
    print(wiz)