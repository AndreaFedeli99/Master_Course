class mycomplex:
    def __init__(self, real, imm):
        self.real = real
        self.imm = imm

    def __str__(self):
        return '{real}{imm_sign}{imm}{i}'.format(real = self.real if self.real not in [0, 1] else "",
                                                    imm_sign = "+" if self.imm > 0 else "-" if self.imm < 0 else "",
                                                    imm = "" if self.imm in [0, 1, -1] else abs(self.imm) if self.imm < 0 else abs(self.imm),
                                                    i = "i" if self.imm != 0 else "")

    def __add__(self, other):
        if isinstance(other, mycomplex):
            return mycomplex(self.real + other.real, self.imm + other.imm)
        else:
            return mycomplex(self.real + other, self.imm)
    
    def __radd__(self, other):
        return mycomplex(self.real + other, self.imm)

    def __sub__(self, other):
        if isinstance(other, mycomplex):
            return mycomplex(self.real - other.real, self.imm - other.imm)
        else:
            return mycomplex(self.real - other.real, self.imm)
    
    def __rsub__(self, other):
        return mycomplex(other - self.real, -self.imm)
    
    def __mul__(self, other):
        if isinstance(other, mycomplex):
            real_part = (self.real * other.real) - (self.imm * other.imm)
            imm_part = (self.imm * other.real) + (self.real * other.imm)
        else:
            real_part = self.real * other
            imm_part = self.imm * other
        return mycomplex(real_part, imm_part)
    
    def __rmul__(self, other):
        return mycomplex(self.real * other, self.imm * other)

    def __truediv__(self, other):
        if isinstance(other, mycomplex):
            real_part = ((self.real * other.real) + (self.imm * other.imm)) / (other.real**2 + other.imm**2)
            imm_part = ((self.imm * other.real) - (self.real * other.imm)) / (other.real**2 + other.imm**2)
        else:
            real_part = self.real / other
            imm_part = self.imm
        return mycomplex(real_part, imm_part)

    def __rtruediv__(self, other):
        real_part = other / self.real
        return mycomplex(real_part, self.imm)

if __name__ == "__main__":
    a = mycomplex(6,7)
    b = mycomplex(3.5,-8)
    c = a+b
    d = -9.5+c
    print("a :-", a)
    print("b :-", b)
    print("c = a+b :-", c)
    print("d = -9.5+c :-", d)
    e = a-b
    print("e = a-b :-", e)
    f = 7-b
    print("f = 7-b :-", f)
    g = e*f
    print("g = e*f :-", g)
    h = 7*g
    print("h = 7*g :-", h)
    i = mycomplex(0,-1)*mycomplex(0,-1)
    print("i :-", i)
    j = a/g
    print("j = a/g :-", j)
    k = a*(b+c)-d*(e+f-g)/(h+i*j)
    print("k :-",k)