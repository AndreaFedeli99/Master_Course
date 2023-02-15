from itertools import groupby

FILE_NAME = "wordlist-text.txt"

words = [w.strip().lower() for w in open(FILE_NAME).readlines()]

def anagram_key(word):
    return ''.join(sorted(word))

def anagram(word):
    return ', '.join([w for w in words if anagram_key(word) == anagram_key(w) and w != word])
    
def anagrams():
    groups = {k: list(v) for k,v in groupby(sorted(words, key=lambda x: anagram_key(x)), key=lambda x: anagram_key(x))}
    return '\n'.join([f"{k} :- {', '.join(v)}" for k,v in sorted({v[0]: v[1:] for k,v in groups.items()}.items(), key = lambda x: x[0])])