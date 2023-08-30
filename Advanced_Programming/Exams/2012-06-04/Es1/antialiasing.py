import inspect
import re

def delete(self):
    prev_frame = inspect.currentframe().f_back
    try:
        assingment = inspect.getframeinfo(prev_frame).code_context[0]
    except AttributeError: return
    matches = re.search("([a-zA-Z][a-zA-Z0-9_]*)[ ]*=[ ]*(.*)$", assingment)
    prev_frame.f_locals[matches.group(1)] = deepcopy(eval(matches.group(2), prev_frame.f_locals))

def deepcopy(L):
    copy = list()
    for item in L:
        if type(item) == list:
            copy.append(deepcopy(item))
        else:
            copy.append(item)
    return copy

class antialiasing(type):
    def __new__(self, clsname, supers, clsdict):
        clsdict['__del__'] = delete
        return super().__new__(self, clsname, supers, clsdict)

original_list = list

list = antialiasing("list", (original_list,), dict(list.__dict__))