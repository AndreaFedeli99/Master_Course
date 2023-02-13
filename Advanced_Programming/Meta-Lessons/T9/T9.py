# Given a text file (text.txt) encoded in T9 and text file of a dictionary (dictionary.txt), write a function that translate each T9 sentence and print all the possible translations.
# Both files doesn't contain punctuations or accents and inside dictionary has only one word per row.
# Note: each number must be considered like it is pressed also more than one time.
# IMPORTANT: a brute force solution and using of itertools are forbidden.

letters_to_number = {'a': '2', 'b': '2', 'c': '2',
                     'd': '3', 'e': '3', 'f': '3',
                     'g': '4', 'h': '4', 'i': '4',
                     'j': '5', 'k': '5', 'l': '5',
                     'm': '6', 'n': '6', 'o': '6',
                     'p': '7', 'q': '7', 'r': '7', 's': '7',
                     't': '8', 'u': '8', 'v': '8',
                     'w': '9', 'x': '9', 'y': '9', 'z': '9'}

CHUNK_LENGTH = 6

def word_to_T9(w):
    return ''.join([letters_to_number[c] for c in w])

def init_word_dict(fn, chunk_l):
    translations = {}
    with open(fn, mode='r', encoding='utf-8') as f:
        for word in f:
            word = word.strip()
            if (len(word) >= chunk_l):
                T9 = word_to_T9(word[:chunk_l])
            else:
                T9 = word_to_T9(word)
            if T9 in translations.keys():
                translations[T9].append(word)
            else:
                translations.update({T9: [word]})
    return translations

def get_combinations(l1, l2):
    return [[phrase[len(phrase) - 1] + ' ' + word] for phrase in l1 for word in l2]

def print_translations(t):
    with open('result.txt', mode='a+', encoding='utf-8') as f:
        for phrases in t:
            for phrase in phrases:
                f.write(phrase + '\n')

def translate_phrases(fn, chuck_l, translations):
    res = []
    with open(fn, mode='r', encoding='utf-8') as f:
        for line in f:
            for T9 in line.split(' '):
                T9 = T9.strip()
                key = T9[:chuck_l] if len(T9) >= chuck_l else T9
                if key in translations.keys():
                    matches = [word for word in [match for match in translations[key] if len(match) == len(T9)] if len(word[chuck_l:]) == 0 or word_to_T9(word[chuck_l:]) == T9[chuck_l:]]
                    if len(res) == 0:
                        res = [[w] for w in matches]
                    else:
                        res = get_combinations(res, matches)
                else:
                    raise RuntimeError(f"The word {T9} doesn't have a translation")
            print_translations(res)
            res.clear()
                
if __name__ == '__main__':
    translations = init_word_dict('dictionary.txt', CHUNK_LENGTH)
    translate_phrases('text.txt', CHUNK_LENGTH, translations)
