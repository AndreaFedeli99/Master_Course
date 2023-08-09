from wordle import read_words, wordle

def print_wordlet(wordlet):
    for w in wordlet:
        print(w)
    print("\n")

if __name__ == '__main__':
    wl = read_words('Advanced_Programming\Exams\\2023-06-20\Es1\wordlist-wordle.txt')
    print_wordlet(wordle('model', 'melon', wl))
    print_wordlet(wordle('slice', 'mount', wl))
    print_wordlet(wordle('crane', 'vowel', wl))
    print_wordlet(wordle('drive', 'sooty', wl))
    print_wordlet(wordle('yacht', 'sassy', wl))
    print_wordlet(wordle('happy', 'roots', wl))
    print_wordlet(wordle('lines', 'hatch', wl))