class Rect:
    def __init__(self, width, height, x = 0, y = 0):
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

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

    def move(self, x, y):
        return Rect(self._width, self._height, self._x + x, self._y + y)

    def collide(self, other):
        if (self.x < other.x + other.width) and \
           (other.x < self.x + self.width) and \
           (self.y < other.y + other.height) and \
           (other.y < self.y + self.height):
            return True
        else:
            return False

    def __str__(self):
        return f"{self._x}, {self._y}, {self._width}, {self._height}"
