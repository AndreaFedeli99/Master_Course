from editor import *

class UndoRedo(type):
    pass

editor = UndoRedo(editor.__name__, editor.__bases__, editor.__dict__)