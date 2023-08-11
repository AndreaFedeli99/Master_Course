
def getanimals(path="Advanced_Programming/Exams/2023-07-18/Es2/animals.txt"):
    with open(path) as f:
        words = [word.strip() for word in f.readlines()]
    return {animal: [w for w in words if animal[-1] == w[0] and w != animal] for animal in words}

animals = getanimals()

class node:
    def __init__(self, val):
        self.value = val
        self.sons = []
        self.used_values = [val]

    def isleaf(self):
        return len(self.sons) == 0
    
    def getbranches(self, current_branch):
        current_branch.append(self.value)

        if self.isleaf():
            return [current_branch]
        else:
            branch = []
            for son in self.sons:
                branch.extend(son.getbranches(current_branch[:]))
            return branch

def genchain(animal, filter=max):
    def buildtree(word, previous):
        valid_words = [w for w in animals[word] if (previous is None) or (w not in previous.used_values)]

        new_node = node(word)
        if previous is not None:
            new_node.used_values.extend(previous.used_values)
        
        if len(valid_words) == 0:
            return new_node
        else:
            new_node.sons = [buildtree(w, new_node) for w in valid_words]
            return new_node
    
    chains_tree = buildtree(animal, None)
    return filter(chains_tree.getbranches([]), key=lambda item: len(item))
