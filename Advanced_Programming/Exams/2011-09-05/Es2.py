from ER_VI.debug import *

if __name__ == "__main__":
    ed = editor()
    print(ed)
    ed.x()
    print(ed)
    ed.dw()
    print(ed)
    ed.i('a')
    print(ed)
    ed.x()
    print(ed)
    ed.i('a')
    print(ed)
    ed.i('b')
    print(ed)
    ed.i('c')
    print(ed)
    ed.h()
    ed.dw()
    print(ed)
    ed.iw(" ...")
    print(ed)
    ed.i('z')
    print(ed)
    ed.h(5)
    print(ed)
    ed.x()
    print(ed)
    ed.iw("(Z) ... 1 2 3")
    print(ed)
    ed.iw("Supercalifragilisticexpialidocious")
    print(ed)
    ed.h(len("Supercalifragilisticexpialidocious")+1)
    ed.i('X')
    print(ed)
    ed.l(len("Supercalifragilistic")+1)
    print(ed)
    ed.dw()
    print(ed)
