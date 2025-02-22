exponents = {
    '2': '00b',
    '3': '00b',
    '4': '207',
    '5': '207',
    '6': '207',
    '7': '207',
    '8': '207',
    '9': '207'
}

# UNICODE_STRING = exponents[n] + n
# encode str to unicode: chr(int('UNICODE_STRING', 16))

class Polynomial:
    def __init__(self, *args):
        self.coeff = [n for n in args]

    def get_grade(self):
        return len(self.coeff) - 1
    
    def __add__(self, other):
        assert other is not Polynomial, "Operands must be Polynomial"
        if self.get_grade() > other.get_grade():
            new_coeff = self.coeff[:self.get_grade()-other.get_grade()] + [self.coeff[-i] + other.coeff[-i] for i in range(1, len(other.coeff) + 1)][::-1]
        else:
            new_coeff = other.coeff[:other.get_grade()-self.get_grade()] + [self.coeff[-i] + other.coeff[-i] for i in range(1, len(self.coeff) + 1)][::-1]
        while len(new_coeff) > 1 and new_coeff[0] == 0:
            new_coeff = new_coeff[1:]
        return Polynomial(*new_coeff)
    
    def __sub__(self, other):
        assert other is not Polynomial, "Operands must be Polynomial"
        if self.get_grade() > other.get_grade():
            new_coeff = self.coeff[:self.get_grade()-other.get_grade()] + [self.coeff[-i] - other.coeff[-i] for i in range(1, len(other.coeff) + 1)][::-1]
        else:
            new_coeff = other.coeff[:other.get_grade()-self.get_grade()] + [self.coeff[-i] - other.coeff[-i] for i in range(1, len(self.coeff) + 1)][::-1]
        while len(new_coeff) > 1 and new_coeff[0] == 0:
            new_coeff = new_coeff[1:]
        return Polynomial(*new_coeff)
    
    def __lshift__(self, other):
        pass
    def __mul__(self, other):
        pass
    def ruffini(self, other):
        pass
    def __truediv__(self, other):
        pass
    def __str__(self):
        return '\t'.join(map(lambda x: str(x), self.coeff))
    
    def monomials(self):
        return [Polynomial(*([item] + [0 for _ in range(i)])) for i,item in enumerate(self.coeff[::-1])][::-1]