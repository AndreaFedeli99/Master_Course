# To extend the class for the strings to support the following operations:
# 1. To check if the string is palindrome, a string is palindrome when the represented sentence can be read the same way in either directions in spite of spaces, 
#    punctual and letter cases, e.g., detartrated, "Do geese see God?", "Rise to vote, sir.", ...
# 2. To subtract the letters in a string from the letters in another string, e.g., "Walter Cazzola"-"abcwxyz" will give "Wlter Col" 
#    note that the operator - is case sensitive and that the target should be a name containing an instance of the child class
# 3. Given a dictionary of strings, to check if the string is an anagram of one or more of the strings in the dictionary

import itertools as it
import string

class CustomString(str):

    def isPalindrome(self):
        s = self.translate(str.maketrans('', '', string.punctuation)).replace(' ', '').lower()
        return s == s[::-1]

    def __sub__(self, other):
        return CustomString(''.join([s for s in self if s not in other]))

    def isAnagram(self, words):
        permutations = [''.join(x) for x in it.permutations(self, len(self))]
        return any(list(it.filterfalse(lambda x: words[x] not in permutations, words)))

palindrome = CustomString("Red roses run no risk, sir, on Nurse's order.")
print(palindrome.isPalindrome())

s = palindrome - "abcersk"
print(s)
print(s.isPalindrome())

anagram = CustomString("abc")
print(anagram.isAnagram({'1': "ghf", '2': "yturua"}))
print(anagram.isAnagram({'1': "bca", '2': "123"}))