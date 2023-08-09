
FILE_NAME = "Advanced_Programming\Exams\\2023-06-20\Es1\wordlist-wordle.txt"

WHITE = '\u001b[37;1m'
GREEN = '\u001b[32;1m'
YELLOW = '\u001b[33;1m'
RESET = '\u001b[0m'

WORDLE_LENGTH = 5

def read_words(fn):
    with open(fn) as f:
        return [word for word in (w.strip().lower() for w in f) if len(word) == WORDLE_LENGTH and word.isalpha()]

def compute_hints(guess, wordle):
    return [((guess[i] == wordle[i] and GREEN) or 
                  (guess[i] != wordle[i] and guess[i] in wordle and YELLOW) or
                  (guess[i] != wordle[i] and guess[i] not in wordle and WHITE)) 
                  for i in range(WORDLE_LENGTH)]

def wordle(guess, wordle, dictionary):

    def compute_wordle(guesses, current_guess, possible_words):

        hints = compute_hints(current_guess, wordle)
        
        colored_guess = ''.join([hints[i] + current_guess[i] for i in range(WORDLE_LENGTH)]) + RESET
        guesses.append(colored_guess)

        if current_guess == wordle:
            return guesses
        else:
            green_letters = [(i, current_guess[i]) for i in range(WORDLE_LENGTH) if hints[i] == GREEN]
            yellow_indexes = [i for i in range(WORDLE_LENGTH) if hints[i] == YELLOW]
            white_letters = {current_guess[i] for i in range(WORDLE_LENGTH) if hints[i] == WHITE}

            possible_words = [word for word in possible_words if not any(set(word).intersection(white_letters)) 
                                    and all(item[1] == word[item[0]] for item in green_letters)
                                    and set(current_guess[i] for i in yellow_indexes).issubset(set(word))
                                    and all(word[i] != current_guess[i] for i in yellow_indexes)]

            return compute_wordle(guesses, possible_words[0], possible_words)
    
    return compute_wordle([], guess, dictionary)

if __name__ == '__main__':
    wl = read_words(FILE_NAME)
    
    print('\n'.join(wordle('crane', 'vowel', wl)))

