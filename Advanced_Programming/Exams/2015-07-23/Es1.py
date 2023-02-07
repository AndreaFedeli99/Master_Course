from itertools import compress

dictionary = open('dictionary.txt').read().split()

def chain(start, target):
    def get_path(current, path):
        if current == target:
            return path
        next_words = [word for word in dictionary if len(word) == len(current) and len(list(compress(word, [word[i] != current[i] for i in range(len(current))]))) == 1]
        return '\n'.join([res for res in [str(get_path(word,path+[word])) for word in next_words if word not in path] if res])
    return get_path(start, [start])
            

if __name__ == '__main__':
    print("### witness → fatness")
    print(chain("witness", "fatness"))
    print("### warning → earring")
    print(chain("warning", "earring"))
    print("### sailing → writing")
    print(chain("sailing", "writing"))