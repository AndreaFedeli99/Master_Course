# Let's write a module (a pool of functions) that given a quite large text (over than 2000 words) counts how frequent each word occurs in the text. 
# In particular the module should provide the function freqs that given a filename and a number would return a list of words (with their frequencies) that occur more than the given number; the list is sorted by frequency with the higher first.

# The text is read from a file and it is a real text with punctuation (i.e., commas, semicolons, ...) that shouldn't be counted.

# Note that words that differ only for the case should be considered the same.

import string, re

def freqs(filename, min_freq):
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    regex2 = re.compile('[%s]' % re.escape("\n"))
    word_occurrences = {}
    with open(filename) as f:
        content = f.read().lower()

    word_list = regex2.sub('', regex.sub('', content)).split(' ')
    for word in word_list:
            if word in word_occurrences:
                word_occurrences[word] += 1
            else:
                word_occurrences.update({word: 1})
    print(word_occurrences)
    return [item for item in word_occurrences.items() if item[1] > min_freq]

print(freqs("test.txt", 100))