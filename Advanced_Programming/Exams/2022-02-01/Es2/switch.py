import types

class Switch:
    def match(self, x):
        l = [Fun(self, x) for _, Fun in self.__class__.__dict__.items() \
            if type(Fun) == types.FunctionType and Fun.__name__ == 'wrapper']
        return [x for x in l if x is not None][0]


def case(c):
    def inner(F):
        def wrapper(self, x):
            l = [c]
            if ('__iter__' in c.__class__.__dict__):
                l = list(c)
            if (c == 'default' or x in l):
                return types.MethodType(F, self)
            return None
        return wrapper
    return inner