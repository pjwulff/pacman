from .shape import Shape

class Rect(Shape):
    def __init__(self, width, height, coordinate = None):
        Shape.__init__(self, coordinate)
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    def move(self, offset):
        return Rect(self.width, self.height, self.coordinate.move(offset))

    def collide(self, other):
        if (self.x < other.x + other.width) and \
           (other.x < self.x + self.width) and \
           (self.y < other.y + other.height) and \
           (other.y < self.y + self.height):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.x}, {self.y}, {self.width}, {self.height}"
