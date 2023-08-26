# Exam of Advanced Programming

###### 2011-09-05

## Exercise 1

As you probably know, ***VI*** is a *modal* text editor: it operates in either insert mode (where typed text becomes part of the document) or normal mode (where keystrokes are interpreted as commands that control the edit session). **Ex** is a line editor that serves as the foundation for the screen editor VI. Ex commands work on the current line or on a range of lines in a file.

**Syntax of Ex commands**

`:[address] command [option]`

In our exercise we are going to implement a simplified version of the line editor Ex used by VI.

In particular you have to implement a class `editor` representing a line of text with the following operations defined on it:

- `x` which deletes the character under the cursor (does nothing) if no characters are present) and move the cursor on the character on the right if present otherwise back of one;
- `dw` which deletes from the characters under the cursor (included) to the next space (excluded) or to the end of the line and moves the cursor on the character on the right if any or backwards otherwise;
- `i` which adds a character `c` after the character under the cursor and moves the cursor under `c`;
- `iw` which adds a word `w` followed by a blank space after the character under the cursor and moves the cursor under the blank space;
- `l` which moves the cursor `n` (1 as default, i.e., when nothing is specified) character on the right from the current position (it does nothing when at the end of the text or it moves less if it is close to the end);
- `h` which moves the cursor `n` (1 as default, i.e., when nothing is specified) character on the left from the current position (it does nothing when at the beginning of the text or it moves less if it is close to the beginning).

Clearly all the above operations are methods invokable on instances of the editor class. Each instance should have clear where the cursor is after each computation.

### Test example

```py
from editor import *

if __name__ == "__main__":
    ed = editor()
    print(ed)
    ed.x()
    print(ed)
    ed.dw()
    print(ed)
    ed.i(’a’)
    print(ed)
    ed.x()
    print(ed)
    ed.i(’a’)
    print(ed)
    ed.i(’b’)
    print(ed)
    ed.i(’c’)
    print(ed)
    ed.h()
    ed.dw()
    print(ed)
    ed.iw(" ...")
    print(ed)
    ed.i(’z’)
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
    ed.i(’X’)
    print(ed)
    ed.l(len("Supercalifragilistic")+1)
    print(ed)
    ed.dw()
    print(ed)
```

### Expected result

```


a

a
ab
abc
a
a ...
a ... z
a ... z
a... z
a.(Z) ... 1 2 3 .. z
a.(Z) ... 1 2 3 Supercalifragilisticexpialidocious .. z
a.(Z) ... 1 2 3 XSupercalifragilisticexpialidocious .. z
a.(Z) ... 1 2 3 XSupercalifragilisticexpialidocious .. z
a.(Z) ... 1 2 3 XSupercalifragilistic .. z
```

## Exercise 2

As you can imagine in the previous exercise, to debug the editor class is not easy. In particular is difficult to find out which operation has changed the text and where the cursor is in any moment.

To this respect write a decorator `debug` (to be applied to the `editor` class of the previous exercise) that, when you print the line of text prints also who has performed the operation and where the cursor is.

### Test example

```py
from debug import *

if __name__ == "__main__":
    ed = editor()
    print(ed)
    ed.x()
    print(ed)
    ed.dw()
    print(ed)
    ed.i(’a’)
    print(ed)
    ed.x()
    print(ed)
    ed.i(’a’)
    print(ed)
    ed.i(’b’)
    print(ed)
    ed.i(’c’)
    print(ed)
    ed.h()
    ed.dw()
    print(ed)
    ed.iw(" ...")
    print(ed)
    ed.i(’z’)
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
    ed.i(’X’)
    print(ed)
    ed.l(len("Supercalifragilistic")+1)
    print(ed)
    ed.dw()
    print(ed)
```

### Expected result

```
 Λ   -1 :- 
 x   -1 :-
dw   -1 :-
 i    0 :- a
 x   -1 :-
 i    0 :- a
 i    1 :- ab
 i    2 :- abc
dw    0 :- a
iw    5 :- a ...
 i    6 :- a ... z
 h    1 :- a ... z
 x    1 :- a... z
iw   15 :- a.(Z) ... 1 2 3 .. z
iw   50 :- a.(Z) ... 1 2 3 Supercalifragilisticexpialidocious .. z
 i   16 :- a.(Z) ... 1 2 3 XSupercalifragilisticexpialidocious .. z
 l   37 :- a.(Z) ... 1 2 3 XSupercalifragilisticexpialidocious .. z
dw   37 :- a.(Z) ... 1 2 3 XSupercalifragilistic.. z
```

## Exercise 3

Any (usable) editor should have a mechanism to undo and redo the actions carried out on the text and our line editor cannot do an exception to this rule.

On the other side undo/redo operations are normally orthogonal to the text editing actions and they are separately implemented. We are going to adopt the same approach to their implementation by defining a `UndoRedo` **metaclass**.

The `UndoRedo` metaclass will add to the `editor` class two operations:

- `u` which undoes the effects of the last executed command (`ctrlr` included) at every call (this means that two consecutive calls will undo the effects of the last two executed commands);
- `ctrlr` which redoes the effects of the last executed command at every call (consecutive calls have a behaviour similar to the undo case)

Note that every pair of calls `u` ⟶ `ctrlr` will leave the text unchanged. A call to `ctrlr` method after any other editing command (i.e., any method different from `u`) has no effect.

The undo/redo model to implement is linear, i.e., if you edit the text after an undo operation you lose the possibility to redo all the changes to it and a successive undo do not restore this possibility.

### Test example

```py
from undo import *

if __name__ == "__main__":
    ed = editor()
    print(ed)
    ed.i(’a’)
    print(ed)
    ed.u()
    print(ed)
    ed.ctrlr()
    print(ed)
    ed.i(’b’)
    print(ed)
    ed.i(’c’)
    print(ed)
    ed.h()
    ed.dw()
    print(ed)
    ed.u()
    print(ed)
    ed.u()
    ed.u()
    print(ed)
    ed.ctrlr()
    print(ed)
    ed.ctrlr()
    ed.ctrlr()
    print(ed)
    ed.iw(" ...")
    print(ed)
    ed.i(’z’)
    print(ed)
    ed.h(5)
    print(ed)
    ed.x()
    print(ed)
    ed.iw("(Z) ... 1 2 3")
    print(ed)
    ed.iw("Supercalifragilisticexpialidocious")
    print(ed)
    ed.u()
    print(ed)
    ed.ctrlr()
    print(ed)
    ed.u()
    print(ed)
    ed.h()
    ed.i(’X’)
    print(ed)
    ed.dw()
    print(ed)
```

### Expected result

```

a

a
ab
abc
a
abc
ab
abc
a
a ...
a ... z
a ... z
a... z
a.(Z) ... 1 2 3 .. z
a.(Z) ... 1 2 3 Supercalifragilisticexpialidocious .. z
a.(Z) ... 1 2 3 .. z
a.(Z) ... 1 2 3 Supercalifragilisticexpialidocious .. z
a.(Z) ... 1 2 3 .. z
a.(Z) ... 1 2 3 X.. z
a.(Z) ... 1 2 3 z
```