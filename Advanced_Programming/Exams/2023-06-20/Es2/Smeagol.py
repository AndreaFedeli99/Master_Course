class Smeagol:
    def __init__(self):
        self.hasTheOneRing = False
    
    def found(self, what):
        if what == 'the one ring':
            self.hasTheOneRing = True
    
    def __str__(self):
        return "type :- " + type(self).__name__ + \
            ",\tRing " + ('🗸' if self.hasTheOneRing else 'x')
    