from re import split

class UpDownFile:
    def __init__(self, fn):
        with open(fn) as f:
            self.f_content = split("\W+", f.read())
        self.f_content.pop()
    def __iter__(self):
        self.f_pointer = -1
        return self
    def __next__(self):
        if self.f_pointer + 1 < len(self.f_content):
            self.f_pointer += 1
            return self.f_content[self.f_pointer]
        raise StopIteration
    def ungetw(self):
        if self.f_pointer > 0:
            self.f_pointer -= 1

if __name__ == '__main__':
    fiter = UpDownFile("wikipedia-excerpt.txt")
    iter(fiter)
    print("### Let's go up and down for a while") 
    print(next(fiter))
    print(next(fiter))
    print(next(fiter))
    print(next(fiter))
    print(next(fiter))
    print(next(fiter))
    fiter.ungetw()
    fiter.ungetw()
    fiter.ungetw()
    print(next(fiter))
    print(next(fiter))
    fiter.ungetw()
    fiter.ungetw()
    print(next(fiter))
    fiter.ungetw()
    fiter.ungetw()
    fiter.ungetw()
    print(next(fiter))
    print(next(fiter))
    print(next(fiter))
    fiter.ungetw()
    print("### Let's finish the iteration") 
    try:
        while True:
            print(next(fiter))
    except StopIteration: pass
    print("### Let's restart the iteration") 
    iter(fiter)
    print(next(fiter))
    print(next(fiter))
    print(next(fiter))
    fiter.ungetw()
    print(next(fiter))