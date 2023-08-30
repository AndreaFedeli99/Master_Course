import inspect

from account import *

def account_log(f):
    def wrapper(*args, **kwargs):
        stack = inspect.getouterframes(inspect.currentframe())
        print("## At the ATM{0} Has been requested a «{1}» on the account {2} owned by {3} for {4}€."
            .format(stack[1].frame.f_locals['self'].idn, f.__name__, args[0].number, args[0].owner, args[1]))
        return f(*args, **kwargs)
    return wrapper

class meta_account(type):
    def __new__(self, clsname, supers, clsdict):
        new_dict = {}
        for attrname, attrval in clsdict.items():
            if attrname == 'deposit' or attrname == 'withdraw':
                new_dict[attrname] = account_log(attrval)
            else:
                new_dict[attrname] = attrval
        return super().__new__(self, clsname, supers, new_dict)

Account = meta_account(Account.__name__, Account.__bases__, Account.__dict__)