from Person import Person

class salary_descriptor:

    def __init__(self, time, priv_name):
        self._time = time
        self.private_name = priv_name

    def __get__(self, obj, objType = None):
        value = getattr(obj, self.private_name)
        return value
    
    def __set__(self, obj, value = None):
        setattr(obj, self.private_name, value)
        obj.set_pay_per_hour(value / self._time)
    
    def __delete__(self, obj):
        setattr(obj, self.private_name, 0)
        obj.set_pay_per_hour(0)

class Worker(Person):

    wh_per_day = 8
    wd_per_week = 5
    ww_per_month = 4
    wm_per_year = 12

    def __init__(self, name, lastname, birthday, pay_per_hour):
        super().__init__(name, lastname, birthday)
        self._pay_per_hour = pay_per_hour
        self.ds = self._pay_per_hour * self.wh_per_day
        self.ws = self._pay_per_hour * self.wh_per_day * self.wd_per_week
        self.ms = self._pay_per_hour * self.wh_per_day * self.wd_per_week * self.ww_per_month
        self.ys = self._pay_per_hour * self.wh_per_day * self.wd_per_week * self.ww_per_month * self.wm_per_year

    def get_pay_per_hour(self):
        return self._pay_per_hour

    def set_pay_per_hour(self, pph):
        self._pay_per_hour = pph

    def compute_total_pay(time):
        def compute(self):
            return self._pay_per_hour * time
        return compute
    
    def update_pay_per_hour(time):
        def update(self, total):
            self._pay_per_hour = total / time
        return update
    
    def zeroing_pay_per_hour(self):
        self._pay_per_hour = 0

    def __repr__(self):
        return self._name + ' ' + self._lastname + ', ' + str(self._birthday) + ", pph: " + str(self.get_pay_per_hour())

    day_salary = property(compute_total_pay(wh_per_day), update_pay_per_hour(wh_per_day), zeroing_pay_per_hour, "Manage the day salary")
    day_salary_desc = salary_descriptor(wh_per_day, 'ds')
    week_salary = property(compute_total_pay(wh_per_day * wd_per_week), 
                            update_pay_per_hour(wh_per_day * wd_per_week), 
                            zeroing_pay_per_hour, 
                            "Manage the week salary")
    week_salary_desc = salary_descriptor(wh_per_day * wd_per_week, 'ws')
    month_salary = property(compute_total_pay(wh_per_day * wd_per_week * ww_per_month), 
                            update_pay_per_hour(wh_per_day * wd_per_week * ww_per_month), 
                            zeroing_pay_per_hour, 
                            "Manage the month salary")
    month_salary_desc = salary_descriptor(wh_per_day * wd_per_week * ww_per_month,'ms')
    year_salary = property(compute_total_pay(wh_per_day * wd_per_week * ww_per_month * wm_per_year), 
                            update_pay_per_hour(wh_per_day * wd_per_week*ww_per_month * wm_per_year), 
                            zeroing_pay_per_hour, 
                            "Manage the year salary")
    year_salary_desc = salary_descriptor(wh_per_day * wd_per_week*ww_per_month * wm_per_year, 'ys')