class Node(object):
    def __init__(self, left = None, right = None, parent = None, value = None, value_morse = None, final_value = None):
        self.left = left
        self.right = right
        self.parent = parent
        self.value = value
        self.value_morse = value_morse
        self.final_value = final_value

class Tree(object):
    def build_tree(self):
        for i in range(len(self.l_morse)):
            tmp = self.root
            for ch in self.l_morse[i]:
                if ch == '.':
                    if tmp.left == None:
                        tmp.left = Node(value_morse = '.') 
                        tmp.parent = tmp
                    tmp = tmp.left
                if ch == '_':
                    if tmp.right == None:
                        tmp.right = Node(value_morse = '_') 
                        tmp.parent = tmp
                    tmp = tmp.right
            tmp.value = chr(ord('a') + i) 
            tmp.final_value = self.l_morse[i] 
            self.l[i] = tmp

    def dfs(self):
        [print(i.value, i.final_value) for i in self.l]
        print()
        def wrapper(current):
            print(current.value, " ", current.final_value)
            if current.right != None:
                wrapper(current.right)
            if current.left != None:
                wrapper(current.left)
        return wrapper(self.root)
    
    def __init__(self, l_morse):
        self.root = Node()
        self.l_morse = l_morse
        self.l = [0] * len(l_morse) 
        self.build_tree()

class Morse(object):
    def __init__(self):
        l_morse = ['._', '_...', '_._.', '_..', \
                   '.', '.._.', '__.', '....', \
                   '..', '.___', '_._', '._..', \
                   '__', '_.', '___', '.__.', \
                   '__._', '._.', '...', '_', \
                   '.._', '..._', '.__', '_.._', \
                   '_.__', '__..']
        self.tree = Tree(l_morse)
        #self.tree.dfs()

    def decode(self, s):
        tmp = []
        current = self.tree.root
        for i in range(len(s)):
            if s[i] == ".":
                current = current.left 
            elif s[i] == "_":
                current = current.right 
            elif s[i] == "u":
                tmp.append(current.value)
                current = self.tree.root
            if s[i] == " " or i == len(s) - 1:
                tmp.append(current.value)
                tmp.append(" ")
                current = self.tree.root
        return ''.join(tmp)

    def encode(self, s):
        s = s.lower()
        tmp = []
        for i in range(len(s)):
            if s[i] == " " or i == len(s) - 1:
                tmp.append(" ")
            else:    
                tmp.append(self.tree.l[ord(s[i]) - ord('a')].final_value)
                if s[i + 1] != " ": 
                    tmp.append('u')
        return ''.join(tmp)
    
if __name__ == "__main__":
    M = Morse()
    print(f"SOS SAVE THE DEVS CHATGPT RULEZ, {M.encode('SOS SAVE THE DEVS CHATGPT RULEZ')}")
    print(f"....u.u._..u._..u___ .__u___u._.u._..u_.., {M.decode('....u.u._..u._..u___ .__u___u._.u._..u_..')}")