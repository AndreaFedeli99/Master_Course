class editor:
    def __init__(self):
        self.txt = ""
        self.idx = -1

    def x(self):
        self.txt = self.txt[:self.idx] + self.txt[self.idx+1:]
        self.idx -= 1 if self.idx >= len(self.txt) else 0

    def dw(self):
        try:
            space_idx = self.idx + self.txt[self.idx:].index(" ") + 1
            self.txt = self.txt[:self.idx] + self.txt[space_idx:]
        except ValueError:
            self.txt = self.txt[:self.idx]
        self.idx -= 1 if self.idx >= len(self.txt) else 0

    def i(self, c):
        self.idx += 1
        self.txt = self.txt[:self.idx] + c + self.txt[self.idx:]

    def iw(self, w):
        self.idx += 1
        self.txt = self.txt[:self.idx] + w + " " + self.txt[self.idx:]
        self.idx += len(w)

    def h(self, n=1):
        self.idx = self.idx - n if self.idx - n >= -1 else -1

    def l(self, n=1):
        self.idx = self.idx + n if self.idx + n < len(self.txt)-1 else len(self.txt)-1
    
    def __str__(self):
        return self.txt