
operators = {
    '+': lambda x,y: x + y,
    '-': lambda x,y: x - y,
    '*': lambda x,y: x * y,
    '/': lambda x,y: x / y,
    '^': lambda x,y: x**y
}

class ExpressionNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def isLeaf(self):
        return self.left is None and self.right is None
    def evaluate(self):
        if not self.isLeaf():
            if self.left.isLeaf() and self.right.isLeaf():
                self.val = operators[self.val](self.left.val, self.right.val)
                self.left = None
                self.right = None
            else:
                self.left.evaluate()
                self.right.evaluate()
    def __str__(self):
        return str(self.val) if self.isLeaf() else "(" + str(self.left) + str(self.val) + str(self.right) + ")"

class calculator:
    def __init__(self, expr):
        self.expr = expr
        self.expTree = self.buildTree(list(self.expr))
        self.currTree = self.expTree
    
    def buildTree(self, expression):
            symbol = expression.pop(0)
            
            if symbol.isnumeric():
                return ExpressionNode(int(symbol))
            else:
                node = ExpressionNode(symbol)
                node.left = self.buildTree(expression)
                node.right = self.buildTree(expression)
                return node

    def __iter__(self):
        self.currTree = self.buildTree(list(self.expr))
        return self

    def __next__(self):
        if self.currTree.isLeaf():
            raise StopIteration
        else:
            self.currTree.evaluate()

    def __str__(self):
        return str(self.currTree)
