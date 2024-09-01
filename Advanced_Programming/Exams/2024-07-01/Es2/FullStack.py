class FullStack:
    def __init__(self, size):
        self.__size__ = size
        self.__top__ = 0
        self.__container__ = [0]*size

    def pop(self):
        self.__top__ -= 1
        return self.__container__[self.__top__]
    
    def __str__(self):
        return "type :- "+type(self).__name__+",\t"+str(self.__top__)+"/"+str(self.__size__)+\
            ",\tcontainer :- ["+', '.join(map(str, self.__container__[:self.__top__]))+']'