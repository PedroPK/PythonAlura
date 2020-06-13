class Rectangle :

    def __init__(self, x, y) :
        self.__x    =   x
        self.__y    =   y
        self.__area =   x * y

    def get_area(self) :
        return self.__area


r = Rectangle(7, 6)
r.area  = 7
area = r.get_area()
print(area)