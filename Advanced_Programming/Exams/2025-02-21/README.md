# Exam of Advanced Programming

###### 2025-02-21

## Exercise 1

In mathematics, economics, and computer science, the **stable marriage problem** (also stable matching problem) is the problem of finding a stable matching between two equally sized sets of elements given an ordering of preferences for each element. A matching is a bijection from the elements of one set to the elements of the other set. A matching is not stable if:

1. There is an element A of the first matched set which prefers some given element B of the second matched set over the element to which A is already matched, and
2. B also prefers A over the element to which B is already matched.

In other words, a matching is stable when there does not exist any pair (A, B) which both prefer each other to their current partner under the matching.

The stable marriage problem has been stated as follows:

*Given n men and n women, where each person has ranked all members of the opposite sex in order of preference, marry the men and women together such that there are no two people of opposite sex who would both rather have each other than their current partners. When there are no such pairs of people, the set of marriages is deemed stable.*

**David Gale** and **Lloyd Shapley** proved that, for any equal number of men and women, it is always possible to solve the stable marriage problem and make all marriages stable. They presented an algorithm to do so.

The **Gale–Shapley algorithm** involves a number of "rounds" (or "iterations"):
- In the first round, first *a)* each unengaged man proposes to the woman he prefers most, and then *b)* each woman replies "maybe" to her suitor she most prefers and "no" to all other suitors. She is then provisionally "engaged" to the suitor she most prefers so far, and that suitor is likewise provisionally engaged to her.
- In each subsequent round, first *a)* each unengaged man proposes to the most-preferred woman to whom he has not yet proposed (regardless of whether the woman is already engaged), and then *b)* each woman replies "maybe" if she is currently not engaged or if she prefers this man over her current provisional partner (in this case, she rejects her current provisional partner who becomes unengaged). The provisional nature of engagements preserves the right of an already-engaged woman to "trade up" (and, in the process, to *"jilt"* her until-then partner).
- The previous step is repeated until everyone is engaged.

### Test example:

```py
from sm import sm

if __name__ == "__main__":
    guyprefers = {
        'abe': ['abi', 'eve', 'isa', 'ivy', 'jan', 'dee', 'fay', 'bea', 'lin', 'may'],
        'bob': ['isa', 'lin', 'abi', 'dee', 'eve', 'fay', 'bea', 'jan', 'ivy', 'may'],
        'col': ['lin', 'eve', 'abi', 'dee', 'bea', 'fay', 'ivy', 'may', 'isa', 'jan'],
        'dan': ['ivy', 'fay', 'dee', 'may', 'lin', 'eve', 'jan', 'bea', 'isa', 'abi'],
        'gav': ['may', 'eve', 'ivy', 'bea', 'isa', 'abi', 'dee', 'lin', 'jan', 'fay'],
        'hal': ['abi', 'eve', 'lin', 'fay', 'ivy', 'isa', 'jan', 'bea', 'may', 'dee'],
        'ian': ['lin', 'isa', 'dee', 'may', 'bea', 'abi', 'fay', 'ivy', 'lin', 'may'],
        'ike': ['jan', 'dee', 'bea', 'isa', 'fay', 'eve', 'abi', 'ivy', 'lin', 'may'],
        'jon': ['abi', 'fay', 'jan', 'may', 'eve', 'bea', 'dee', 'isa', 'ivy', 'lin'],
        'joy': ['bea', 'abi', 'dee', 'may', 'eve', 'ivy', 'isa', 'jan', 'lin', 'fay'],
    }

    galprefers = {
        'abi': ['bob', 'joy', 'jon', 'gav', 'ian', 'abe', 'dan', 'ike', 'col', 'hal'],
        'bea': ['bob', 'abe', 'col', 'joy', 'gav', 'dan', 'ian', 'ike', 'jon', 'hal'],
        'isa': ['joy', 'bob', 'ike', 'gav', 'hal', 'col', 'ian', 'abe', 'dan', 'jon'],
        'dee': ['joy', 'jon', 'col', 'abe', 'ian', 'hal', 'gav', 'dan', 'bob', 'ike'],
        'eve': ['jon', 'hal', 'joy', 'dan', 'abe', 'gav', 'col', 'ike', 'ian', 'bob'],
        'fay': ['bob', 'abe', 'ike', 'ian', 'jon', 'dan', 'joy', 'gav', 'col', 'hal'],
        'may': ['jon', 'gav', 'hal', 'joy', 'bob', 'abe', 'col', 'ike', 'dan', 'ian'],
        'lin': ['gav', 'jon', 'bob', 'abe', 'ian', 'dan', 'hal', 'ike', 'col', 'joy'],
        'ivy': ['ian', 'col', 'hal', 'gav', 'joy', 'bob', 'abe', 'ike', 'jon', 'dan'],
        'jan': ['ike', 'hal', 'gav', 'abe', 'bob', 'jon', 'col', 'ian', 'joy', 'dan'],
    }

    print("Engagements!")
    couples = sm(guyprefers, galprefers)
    print(f"{chr(10)}Final Couples")
    print(chr(10).join([f"  · {guy} 💑 {gal}" for gal, guy in sorted(couples, key = lambda e: e[1])]))
```

### Expected output:

```code
Engagements!
💑 jan engages with ike
💑 abi engages with jon
💑 bea engages with joy
💑 isa engages with bob
💑 lin engages with col
💑 ivy engages with dan
💑 may engages with gav
💔 lin breaks with col to 💑 engage with ian
💑 eve engages with abe
💔 eve breaks with abe to 💑 engage with hal
💔 ivy breaks with dan to 💑 engage with abe
💑 dee engages with col
💑 fay engages with dan

Final Couples
  · abe 💑 ivy
  · bob 💑 isa
  · col 💑 dee
  · dan 💑 fay
  · gav 💑 may
  · hal 💑 eve
  · ian 💑 lin
  · ike 💑 jan
  · jon 💑 abi
  · joy 💑 bea
```

## Exercise 2



### Test example:

```py

```

### Output:

```code

```

**Note** that your program must be general and not tailored on the examples.