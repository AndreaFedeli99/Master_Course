
def getanimals(path="Advanced_Programming/Exams/2023-07-18/Es2/animals.txt"):
    animals = {}
    with open(path) as f:
        for animal in f:
            animal = animal.strip().lower()
            if animal[0] in animals:
                animals[animal[0]].append(animal)
            else:
                animals[animal[0]] = [animal]
    return animals

animals = getanimals()

class node:
    def __init__(self, val):
        self.value = val
        self.sons = []
        self.used_values = [val]

    def isleaf(self):
        return len(self.sons) == 0
    
    def buildchains(self, current_chain):
        current_chain.append(self.value)

        if self.isleaf():
            return [current_chain]
        else:
            chains = []
            for son in self.sons:
                chains.extend(son.buildchains(current_chain[:]))
            return chains

def genchain(animal, filter=max):
    def buildtree(word, previous):
        letter = word[-1]
        valid_words = [] if letter not in animals else [w for w in animals[letter] if (previous is None) or (w not in previous.used_values and w != word)]

        new_node = node(word)
        if previous is not None:
            new_node.used_values.extend(previous.used_values)
        
        if len(valid_words) == 0:
            return new_node
        else:
            new_node.sons = [buildtree(w, new_node) for w in valid_words]
            return new_node
    
    chains_tree = buildtree(animal, None)
    return filter(chains_tree.buildchains([]), key=lambda item: len(item))