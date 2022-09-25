class Rectangle:
    def __int__(self, length, width):
        self.length = None
        self.width = None

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @length.setter
    def length(self, new_length):
        Rectangle.CheckValue(new_length)
        self._length = new_length

    @width.setter
    def width(self, new_width):
        Rectangle.CheckValue(new_width)
        self._width = new_width

    @staticmethod
    def CheckValue(value):
        if (value < 0.0 or value > 20.0) or not isinstance(value, float):
            raise Exception

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width


res1 = Rectangle()
res1.length = 4.0
res1.width = 2.0
print(res1.perimeter())
print(res1.area())


