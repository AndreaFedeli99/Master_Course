from enum import Enum
from math import sqrt

class color(Enum):
    GREY = -1
    WHITE = 0
    BLACK = 1

class node:
    def __init__(self, val, subs=None):
        self.val = val
        self.subs = subs

    def isLeaf(self):
        return self.subs is None
    
    def getLeafs(self, leafs):
        if self.isLeaf():
            return [self.val.value]
        else:
            leafs_values = []
            for s in self.subs:
                leafs_values.extend(s.getLeafs(leafs[:]))
            return leafs_values

class quadtree:
    def __init__(self, img):
        def build(start, width):
            if self.checkColor(start, width, color.WHITE) or self.checkColor(start, width, color.BLACK):
                return node(color.WHITE) if self.checkColor(start, width, color.WHITE) else node(color.BLACK)
            else:
                n = node(color.GREY)
                n.subs = [build(start+i, width//2) for i in range(0, width//2+1, width//2)]
                n.subs.extend([build(start+(width*4)+(width//2)-i, width//2) for i in range(0, width//2+1, width//2)])
                return n
        self.img = img
        self.img_width = int(sqrt(len(self.img)))
        self.root = build(0, self.img_width)

    def checkColor(self, start, dim, c):
        return all((self.img[row+col] == c.value for row in range(0, dim*self.img_width, self.img_width) for col in range(start, start + dim)))

    def count(self):
        return len(self.img) - len(self.root.getLeafs([]))

    def showImgTree(self):
        return self.root.getLeafs([])