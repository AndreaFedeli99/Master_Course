words = dict()

def create_dictionary(fn):
    with open(fn) as f:
        for line in f:
            key = line[0]
            if key in words.keys():
                words[key] += [line[:-1]]
            else: words[key] = [line[:-1]]

def create_alternade(w, n):
    res = []
    for i in range(n): res += [w[i::n]]
    return res

def alternade_generator(fn, n):
    create_dictionary(fn)

    with open(fn) as f:
        for line in f:
            if len(line[:-1]) >= n:
                alternade = create_alternade(line[:-1], n)
                if all([a in words[a[0]] for a in alternade]):
                    yield line[:-1], alternade
    