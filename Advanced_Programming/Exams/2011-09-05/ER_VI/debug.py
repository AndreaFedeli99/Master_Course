def debug(cls):
    class wrapper:
        def __init__(self, *args, **kwargs):
            cls.__str__ = self.__str__
            self.wrapped = cls(*args, **kwargs)
            self.wrapped.last_call = "Λ"

        def __str__(self):
            return f"{self.wrapped.last_call : >2}{self.wrapped.idx : >5} :- {self.wrapped.txt}"
        
        def __getattr__(self, name):
            if name == "wrapped":
                return self.__dict__[name]
            else:
                self.wrapped.last_call = name
                return getattr(self.wrapped, name)
    
    return wrapper

if __name__ != '__main__':
    from ER_VI.editor import *

    editor = debug(editor)
    
    