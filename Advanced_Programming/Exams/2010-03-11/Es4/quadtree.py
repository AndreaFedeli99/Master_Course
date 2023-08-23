from enum import Enum
from math import sqrt

class color(Enum):
    BLACK = 1,
    WHITE = 0,
    GREY = -1

class node:
    def __init__(self, val, subs=None):
        self.val = val
        self.subs = subs
    def isLeaf(self):
        return self.subs is None

class quadtree:
    def __init__(self, img):
        def build(root, vec):
            return
        self.img = img
        self.root = build()

    def count(self):
        def countLeaf(root):
            if root.isLeaf():
                return 1
            else:
                return sum(map(lambda s: countLeaf(s), self.root.subs))
        return len(self.img) - countLeaf(self.root)