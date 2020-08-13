#what is encapsulation in python?

#encapsulation is the process of hiding the elements


class Polygon:
    """This class describes about the polygon"""
    def __init__(self, sides): #This can be accessed only by the class which is inherited
        self._side = sides


class Rectangle(Polygon):
    """This describes about the rectangle"""
    def __init__(self, side, length, breadth):
        """This is used tbro initialize the values"""
        self._side = side
        self.__length = length
        self.__breadth = breadth

    def area(self):
        """This is used to provide the area of the rectangle"""
        return self.__length * self.__breadth

r = Rectangle(4, 2, 6)
print(r.area())
#print(r._sides)
print(r._Rectangle__length)
