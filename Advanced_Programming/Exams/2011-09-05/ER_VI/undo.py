from collections import deque

if __name__ == "__main__":
    from editor import *
else:
    from ER_VI.editor import *

def u(self):
    try:
        prec_status = self.op_stack.pop()
        self.redo.append((self.idx, self.txt))
        self.idx = prec_status[0]
        self.txt = prec_status[1]
    except IndexError:
        pass

def ctrlr(self):
    try:
        prec_status = self.redo.pop()
        self.op_stack.append((self.idx, self.txt))
        self.idx = prec_status[0]
        self.txt = prec_status[1]
    except IndexError:
        pass

def manageUndoRedo(f):
    def wrapper(instance, *args, **kwargs):
        instance.op_stack.append((instance.idx, instance.txt))
        instance.redo.clear()
        return f(instance, *args, **kwargs)
    return wrapper

class UndoRedo(type):
    def __new__(self, clsname, supers, clsdict):
        new_dict = {}
        for attrname, attrval in clsdict.items():
            if callable(attrval) and not attrname.startswith("__") and not attrname.endswith("__"):
                new_dict[attrname] = manageUndoRedo(attrval)
            else:
                new_dict[attrname] = attrval
        new_dict["op_stack"] = deque()
        new_dict["redo"] = deque()
        new_dict["u"] = u
        new_dict["ctrlr"] = ctrlr
        return super().__new__(self, clsname, supers, new_dict)

editor = UndoRedo(editor.__name__, editor.__bases__, editor.__dict__)