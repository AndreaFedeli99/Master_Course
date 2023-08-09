from itertools import groupby

FILE_NAME = "Advanced_Programming\Exams\\2022-02-15\Es1\wordlist-text.txt"

def anagram_key(word):
    return ''.join(sorted(word))

words = [w.strip().lower() for w in open(FILE_NAME).readlines()]
words_dict = {k: list(v) for k,v in groupby(sorted(words, key=lambda x: anagram_key(x)), key=lambda x: anagram_key(x))}


def anagram(word):
    key = ''.join(sorted(word))
    return ', '.join([v for v in words_dict[key] if v != word])
    
def anagrams():
    return '\n'.join([f"{k} :- {', '.join(v)}" for k,v in sorted({v[0]: v[1:] for k,v in words_dict.items()}.items(), key = lambda x: x[0])])