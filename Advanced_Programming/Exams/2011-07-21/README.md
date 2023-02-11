# Exam of Advanced Programming

###### 2011-07-21

## Exercise 1

As everyone knows Europe is a collection of countries close to each other; each country has a pool of neighboring countries whose inhabitants have to cross to reach other countries.

Define a function `crossing` that given a country name and `n` (the disired number of steps) gives you the set of countries you can reach crossing n countries starting from the given country. Note that:

- In zero steps you can't exit from the starting country;
- In one step you get only in the border countries;
- The path must always be minimal, e.g., from Italy you can get in Belgium crossing Switzerland and Germany or only France, second path is the one to choose;
- You can't cross a country twice or more or get back, e.g., Italy → Switzerland → Italy is wrong

For semplicity, in the exercise exclude Kazakhstan, Georgia, Azerbaijan, Cyprus and Turkey from Europe.

**Hint**: define a generator `border`, used by `crossing` that given the starting country at each step provides the set of border countries of the border computed in the previous step.

### Test example:

```py
if __name__ == "__main__":
    print("*** From Italy in ")
    for steps in range(8):
        print("[{0}] = {1}".format(steps, crossing("italy", steps)))

    print("*** From Sweden in [5] steps, you get in", crossing('sweden', 5))
    print("*** From Germany in [2] steps, you get in", crossing('germany', 2))
    print("*** From Iceland in [3] steps, you get in," crossing('iceland', 3))
```

### Expected output:

```code
*** From Italy in
[0] = {'italy'}
[1] = {'san marino', 'france', 'slovenia', 'austria', 'switzerland', 'vatican city'}
[2] = {'czech republic', 'hungary', 'luxembourg', 'andorra', 'liechtenstein', 'croatia', 'monaco', 'belgium', 'slovakia', 'germany', 'spain'}
[3] = {'ukraine', 'romania', 'netherlands', 'portugal', 'denmark', 'poland', 'serbia', 'bosnia and herzegovina'}
[4] = {'belarus', 'montenegro', 'lithuania', 'macedonia', 'moldova', 'albania', 'russia', 'bulgaria'}
[5] = {'finland', 'norway', 'latvia', 'estonia', 'greece'}
[6] = {'sweden'}
[7] = set()
*** From Sweden in [5] steps, you get in {'netherlands', 'denmark', 'serbia', 'luxembourg', 'france', 'slovenia', 'austria', 'croatia', 'belgium', 'switzerland', 'bulgaria'}
*** From Germany in [2] steps, you get in {'ukraine', 'belarus', 'italy', 'lithuania', 'andorra', 'slovenia', 'liechtenstein', 'slovakia', 'monaco', 'hungary', 'russia', 'spain'}
*** From Iceland in [3] steps, you get in set()
```

## Exercise 2

Write a class to test the result on the previous exercise.

**Hint**: Some properties that should be valid in the previous exercise are:

- All countries listed as neighbors of another country must list such country as a neighbor;
- A path can be followed in the two directions, i.e., if you get in *c1*, *c2* and *c3* from a country *c* in n steps then in n steps from either *c1*, *c2* and *c3* you must get in *c*.

These are just a couple of **necessary** tests not the only possible but represents a good minimal pool of tests to consider your exercise correct.

## Exercise 3

Recently on the Internet is possible to see a novel approach to sorting named **sleep sort** that promises linear time complexity. Such an approach rely on the **sleep** system call to sort the numbers: each number is dealt as a thread which is suspended as many milliseconds as the number itself and when resumed it will just print its number. The scheduler will play the magic by resuming the threads in the correct order.

The exercise consists of coding the sleep sort algoritm as a python function that gets the numbers to be sorted and spawns the threads according to the presented algorithm.

**Hint**: take a look at the standard modules `threading`, `queue` and `time`.

### Test example:

```py
if __name__ == "__main__":
    sleepsort([7, 2 ,100, 1, 9, 45, 2, 33, 7, 77, 25])
    sleepsort([333, 222 ,112, 777, 901, 455, 256, 313, 125, 625, 825, 999, 316])
    sleepsort([1000, 10, 10.5, 100, 22, 77, 700, 3.145, 2000, 150, 35, 287, 4, 7, 777, 2525, 255, 256, 25])
```

### Expected output:

```code
1 2 2 7 7 9 25 33 45 77 100
112 125 222 256 313 316 333 455 625 777 825 901 999
3.145 4 7 10 10.5 22 25 35 77 100 150 255 256 287 700 777 1000 2000 2525
```