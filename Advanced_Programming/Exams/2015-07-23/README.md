# Exam of Advanced Programming

###### 2015-07-23

## Exercise 1

Write a function named `chain` that calculates and prints all the possible paths from a starting word to a target one.

To solve the exercise you must respect the following constraints:  
- The path must be composed of unique words.
- Each word must differ by one character with the precedent.
- The solution must use a recursive approach.
- All the used words must belong to a dictionary file called `dictionary.txt`
- The solution must respect the given interface.  

### Test example:

```py
if __name__ == '__main__':
    print("### witness → fatness")
    print(chain("witness", "fatness"))
    print("### warning → earring")
    print(chain("warning", "earring"))
    print("### sailing → writing")
    print(chain("sailing", "writing"))
```

### Expected output:

```code
witness → fatness
['witness', 'fitness', 'fatness']

warning → earring
['warning', 'warring', 'barring', 'earring']
['warning', 'warring', 'barring', 'jarring', 'earring']
['warning', 'warring', 'earring']
['warning', 'warring', 'jarring', 'barring', 'earring']
['warning', 'warring', 'jarring', 'earring']

sailing → writing
['sailing', 'failing', 'mailing', 'railing', 'wailing', 'waiting', 'whiting', 'writing']
['sailing', 'failing', 'mailing', 'railing', 'wailing', 'waiting', 'writing']
['sailing', 'failing', 'mailing', 'wailing', 'waiting', 'whiting', 'writing']
['sailing', 'failing', 'mailing', 'wailing', 'waiting', 'writing']
['sailing', 'failing', 'railing', 'mailing', 'wailing', 'waiting', 'whiting', 'writing']
['sailing', 'failing', 'railing', 'mailing', 'wailing', 'waiting', 'writing']
['sailing', 'failing', 'railing', 'wailing', 'waiting', 'whiting', 'writing']
['sailing', 'failing', 'railing', 'wailing', 'waiting', 'writing']
['sailing', 'failing', 'wailing', 'waiting', 'whiting', 'writing']
['sailing', 'failing', 'wailing', 'waiting', 'writing']
['sailing', 'mailing', 'failing', 'railing', 'wailing', 'waiting', 'whiting', 'writing']
['sailing', 'mailing', 'failing', 'railing', 'wailing', 'waiting', 'writing']
['sailing', 'mailing', 'failing', 'wailing', 'waiting', 'whiting', 'writing']
['sailing', 'mailing', 'failing', 'wailing', 'waiting', 'writing']
['sailing', 'mailing', 'railing', 'failing', 'wailing', 'waiting', 'whiting', 'writing']
['sailing', 'mailing', 'railing', 'failing', 'wailing', 'waiting', 'writing']
['sailing', 'mailing', 'railing', 'wailing', 'waiting', 'whiting', 'writing']
['sailing', 'mailing', 'railing', 'wailing', 'waiting', 'writing']
['sailing', 'mailing', 'wailing', 'waiting', 'whiting', 'writing']
['sailing', 'mailing', 'wailing', 'waiting', 'writing']
['sailing', 'railing', 'failing', 'mailing', 'wailing', 'waiting', 'whiting', 'writing']
['sailing', 'railing', 'failing', 'mailing', 'wailing', 'waiting', 'writing']
['sailing', 'railing', 'failing', 'wailing', 'waiting', 'whiting', 'writing']
['sailing', 'railing', 'failing', 'wailing', 'waiting', 'writing']
['sailing', 'railing', 'mailing', 'failing', 'wailing', 'waiting', 'whiting', 'writing']
['sailing', 'railing', 'mailing', 'failing', 'wailing', 'waiting', 'writing']
['sailing', 'railing', 'mailing', 'wailing', 'waiting', 'whiting', 'writing']
['sailing', 'railing', 'mailing', 'wailing', 'waiting', 'writing']
['sailing', 'railing', 'wailing', 'waiting', 'whiting', 'writing']
['sailing', 'railing', 'wailing', 'waiting', 'writing']
['sailing', 'wailing', 'waiting', 'whiting', 'writing']
['sailing', 'wailing', 'waiting', 'writing']
```

## Exercise 2

Implement an iterator called `UpDownFile` over files that permits to get a word at each call of the `next` operator.  

Moreover, it supports a `ungetw` method that permits to come back in the file's content a word at a time. 
That is that a call to `next` after a call to `ungetw` will extract the last extracted word.  

To solve the exercise you must respect the following constraints:  
- The only admitted methods on file are `open` and `read`.
- The solution must respect the given *--by the example below--* interface.  

### Test example:

```py
if __name__ == '__main__':
    fiter = UpDownFile("wikipedia-excerpt.txt")
    iter(fiter)
    print("### Let's go up and down for a while") 
    print(next(fiter))
    print(next(fiter))
    print(next(fiter))
    print(next(fiter))
    print(next(fiter))
    print(next(fiter))
    fiter.ungetw()
    fiter.ungetw()
    fiter.ungetw()
    print(next(fiter))
    print(next(fiter))
    fiter.ungetw()
    fiter.ungetw()
    print(next(fiter))
    fiter.ungetw()
    fiter.ungetw()
    fiter.ungetw()
    print(next(fiter))
    print(next(fiter))
    print(next(fiter))
    fiter.ungetw()
    print("### Let's finish the iteration") 
    try:
        while True:
            print(next(fiter))
    except StopIteration: pass
    print("### Let's restart the iteration") 
    iter(fiter)
    print(next(fiter))
    print(next(fiter))
    print(next(fiter))
    fiter.ungetw()
    print(next(fiter))
```

### Expected output:

```code
### Let's go up and down for a little
A
computer
file
is
a
resource
is
a
is
computer
file
is
### Let's finish the iteration
is
a
resource
for
storing
information
which
is
available
to
a
computer
program
and
is
usually
based
on
some
kind
of
durable
storage
A
file
is
durable
in
the
sense
that
it
remains
available
for
other
programs
to
use
after
the
program
that
created
it
has
finished
executing
Computer
files
can
be
considered
as
the
modern
counterpart
of
paper
documents
which
traditionally
are
kept
in
office
and
library
files
and
this
is
the
source
of
the
term
Etymology
The
word
file
was
used
publicly
in
the
context
of
computer
storage
as
early
as
February
1950
In
an
RCA
Radio
Corporation
of
America
advertisement
in
Popular
Science
Magazine
describing
a
new
memory
vacuum
tube
it
had
developed
RCA
stated
the
results
of
countless
computations
can
be
kept
on
file
and
taken
out
again
Such
a
file
now
exists
in
a
memory
tube
developed
at
RCA
Laboratories
Electronically
it
retains
figures
fed
into
calculating
machines
holds
them
in
storage
while
it
memorizes
new
ones
speeds
intelligent
solutions
through
mazes
of
mathematics
In
1952
file
was
used
in
referring
to
information
stored
on
punched
cards
In
early
usage
people
regarded
the
underlying
hardware
rather
than
the
contents
as
the
file
For
example
the
IBM
350
disk
drives
were
called
disk
files
3
In
about
1961
the
Burroughs
MCP
and
the
MIT
Compatible
Time-Sharing
System
introduced
the
concept
of
a
file
system
which
managed
several
virtual
files
on
one
storage
device
giving
the
term
its
present-day
meaning
Although
the
current
term
register
file
shows
the
early
concept
of
files
it
has
largely
disappeared
### Let's restart the iteration
A
computer
file
file
```