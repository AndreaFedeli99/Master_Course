# Exam of Advanced Programming

###### 2013-07-22

## Exercise 1

Define a function `replace_synonyms` that takes a string (the text to simplify) and returns a copy of the same text with the complicated terms substituted with their more diffused synonym. To be more evident the new term should be capitalized in the result.

The table of synonym is contained inside the file `synomnyms-list.txt` and each line contains the term to be used separated by a colon `:` from a comma-separated list of terms it will substitute.

### Test example:

```py
if __name__ == "__main__":
    s0 = "The deadline is approximately midnight though it could vary."
    s1 = "She is a fascinating lady; she has an astonishing smile, an alluring voice and an entertaining sense of humor."
    s2 = "The topic is appealing nevertheless the speaker was too monotonous."
    print(replace_synonyms(s0))
    print(replace_synonyms(s1))
    print(replace_synonyms(s2))
```

### Expected output:

```code
The deadline is ABOUT midnight BUT it could CHANGE.
She is a INTERESTING lady; she has an AWESOME smile, an BEATIFUL voice and an FUNNY sense of humor.
The topic is INTERESTING BUT the speaker was SO BORING.
```

## Exercise 2

Implement your own version of some of strings' module without using such a module. In particular the only admitted operations on strings are: `+`, `[]`, `in`, `==`, `!=` and `:`. The solution must use a **recursive** approach.

The operations to implement are:

- `reverse(s)`: this returns the string `s` reversed;
- `strip(s, chars)`: this removes all the occurrences of the characters in `chars` from the string `s` and returns the resulting string;
- `split(s, seps)`: this splits the string `s` on the characters listed in `seps` (if two elements of `seps` are adjecent in the string no empty token is generated); the tokens are returned in a list in the order they have in the original string;
- `find(s, ch)`: this finds the character `ch` (positions starts from 0) or -1 when the character doesn't occur in the string; **note** that if function is called two or more times in a row with the same arguments it returns the position of the next occurence instead.

### Test example:

```py
from rstrings import *

if __name__ == "__main__":
    s0 = "The deadline is approximately midnight though it could vary."
    s1 = "She is a fascinating lady; she has an astonishing smile, an alluring voice and an entertaining sense of humor."
    s2 = "The topic is appealing nevertheless the speaker was too monotonous."
    s3 = "The topic ais appealing nevertheless the speaker was too monotonous."
    print(strip(s0, 'aeiou'))
    print(reverse(s0))
    print(strip(reverse(s0), 'aeiou'))
    print(split(s1, ' ;,.'))
    print(reverse(s2))
    print("test on find:")
    print(find(s2, 'a'))
    print(find(s2, 'a'))
    print(find(s2, 'a'))
    print(find(s3, 'a'))
    print(find(s3, 't'))
    print(find(s3, 't'))
    print(find(s3, 't'))
    print(find(s3, 't'))
    print(find(s3, 't'))
    print(find(s3, 't'))
    print(find(s3, 't'))
```

### Expected output:

```code
Th ddln s pprxmtly mdnght thgh t cld vry.
.yrav dluoc ti hguoht thgindim yletamixorppa si enildaed ehT
.yrv dlc t hght thgndm yltmxrpp s nldd hT
['She', 'is', 'a', 'fascinating', 'lady', 'she', 'has', 'an', 'astonishing', 'smile', 'an', 'alluring', 'voice', 'and', 'an', 'entertaining', 'sense', 'of', 'humor']
.suonotonom oot saw rekaeps eht sselehtreven gnilaeppa si cipot ehT
tests on find:
13
17
43
10
4
29
37
53
61
-1
4
```