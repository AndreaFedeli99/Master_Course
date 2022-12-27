# To implement the classes representing: equilateral triangles, circles, rectangles, squares and pentagons with the following characteristics/properties/capabilities.

# 1. They should understand the calculate_area() and calculate_perimeter() messages with the obvious meaning 
# 2. The state must be private
# 3. A list of geometric shapes must be sortable by area and by perimeter (not at the same time, of course)
# 4. To add an hexagon class should maintain all the capabilities of the existing classes and correctly interact with them
# 5. To write a iterator that permits to return the elements of a list of geometric shapes sorted by increasing areas

import math

class circle:
    def __init__(self, radius):
        self.__radius = radius
    def calculate_perimeter(self):
        return 2*math.pi*self.__radius
    def calculate_area(self):
        return math.pi*(self.__radius**2)
    def compare(self, compare):
        pass
    def __lt__(self, other):
            return self.compare(other)
    def __str__(self):
        return f"Circle: 2p = {self.calculate_perimeter()} A = {self.calculate_area()}"

def create_polygon(polygon_name, num_side):
    class polygon:
        def __init__(self, side):
            self.__side = side
        def calculate_perimeter(self):
            return num_side*self.__side
        def calculate_area(self):
            return .25*num_side*self.__side**2*(math.tan(math.pi/num_side)**-1)
        def compare(self, other):
            pass
        def __lt__(self, other):
            return self.compare(other)
        def __str__(self):
            return f"{polygon_name}: 2p = {self.calculate_perimeter()} A = {self.calculate_area()}"
    
    return polygon

triangle = create_polygon("Triangle", 3)
rectangle = create_polygon("Rectangle", 4)
square = create_polygon("Square", 4)
pentagon = create_polygon("Pentagon", 5)

t = triangle(15)
r = rectangle(5)
s = square(3)
p = pentagon(5)
c = circle(7)

polygon_list = [t, r, s, p, c]

class polygon_iterator:
    def __init__(self, p_list, sort_method):
        self.__p_list = p_list
        self.__sort_method = sort_method
        self.__index = 0
    def __iter__(self):
        self.__index = 0
        for pol in self.__p_list:
            pol.compare = self.__sort_method.__get__(pol, type(pol))
        self.__p_list.sort()
        return self
    def __next__(self):
        while True:
            if self.__index > len(self.__p_list) - 1:
                raise StopIteration
            item = self.__p_list[self.__index]
            self.__index += 1
            return item
    def set_sort_method(self, sort_method):
        self.__sort_method = sort_method

print("---POLIGON LIST---")
print(*polygon_list,sep="\n")

p_iter = polygon_iterator(polygon_list, lambda s, o: s.calculate_perimeter() < o.calculate_perimeter())
print("\n---POLIGON LIST SORTED BY PERIMETER---")
print(*p_iter, sep="\n")

p_iter.set_sort_method(lambda s, o: s.calculate_area() > o.calculate_area())
print("\n---POLIGON LIST SORTED BY AREA (DESCENDING)---")
print(*p_iter, sep="\n")

polygon_list.append(create_polygon("Hexagon", 6)(6))
print("\n---ADDED HEXAGON TO POLIGON LIST---")
print(*polygon_list, sep="\n")

p_iter.set_sort_method(lambda s, o: s.calculate_area() < o.calculate_area())
print("\n---POLIGON SORTED BY AREA (ASCENDING)---")
print(*p_iter, sep="\n")