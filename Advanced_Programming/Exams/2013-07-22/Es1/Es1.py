import re
import string

FILE_PATH = "Università\Advanced_Programming\Exams\\2013-07-22\synonyms-list.txt"

def replace_synonyms(s):
    def create_dict():
        synonyms = dict()
        with open(FILE_PATH) as f:
            for line in f:
                key_values = line.split(':')
                synonyms.update({k.strip(): key_values[0].strip().upper() for k in [word for word in key_values[1].split(',')]})
        return synonyms
    
    res = ''
    synonyms_dict = create_dict()
    for word in s.split(' '):
        key, punctuation = (word[:-1], word[-1]) if re.match(r"[.,;!?]", word[-1]) != None else (word, '')
        if key in synonyms_dict:
            res += synonyms_dict[key] + punctuation + " "
        else:
            res += word + " "
    return res

if __name__ == "__main__":
    s0 = "The deadline is approximately midnight though it could vary."
    s1 = "She is a fascinating lady; she has an astonishing smile, an alluring voice and an entertaining sense of humor."
    s2 = "The topic is appealing nevertheless the speaker was too monotonous."
    print(replace_synonyms(s0))
    print(replace_synonyms(s1))
    print(replace_synonyms(s2))