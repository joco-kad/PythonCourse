class Shape:
    def __init__(self, x, y=1):
        self.__x = x
        self.__y = y
        self.desc = "A really nice shape"
    def __foobar(self):
        return self.__x * self.__y
    def area(self):
        return self.__foobar()
    def scaleSize(self, scale):
        self.__x = self.__x * scale
        self.__y = self.__y * scale

class Square(Shape):
    def __init__(self, x):
        super().__init__(x, x)
        """ Unschöne Alternative:
        self._Shape__x = x
        self._Shape__y = x """

class FunkyPrinter:
    def printFunky(self):
        print("Funky!")

class FunkySquare(Shape, FunkyPrinter):
    def __init__(self, x):
        Shape.__init__(self, x, x)
    

