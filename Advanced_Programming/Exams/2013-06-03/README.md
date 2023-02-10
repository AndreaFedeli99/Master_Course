# Exam of Advanced Programming

###### 2013-06-03

## Exercise 1

A palindrom string is a string that can be read in the same way from left to right and from right to left. Some word are not palindrome but can be transformed into palindrome word by adding a minimum number of characters depending on the string.

The exercise consists on defining a function `palin` that given a string returns how many charachters are necessary to render it palindrome and which are those characters. Please note that the correct answer minimizes the number of introduced characters and list them in temporal order of introduction (characters can be introduced everywhere).

### Test example:

```py
if __name__ == "__main__":
    print(palin("casa"))
    print(palin("otto"))
    print(palin("palindromo"))
    print(palin("posero"))
    print(palin("coccinella"))
```

### Expected output:

```code
The word <<casa>> needs 1 insertions to become palindrome: ['c']
The word <<otto>> needs 0 insertions to become palindrome
The word <<palindromo>> needs 7 insertions to become palindrome: ['p', 'a', 'l', 'i', 'n', 'd', 'r']
The word <<posero>> needs 3 insertions to become palindrome: ['p', 'r', 'e']
The word <<coccinella>> needs 7 insertions to become palindrome: ['a', 'l', 'l', 'e', 'n', 'i', 'c']
```