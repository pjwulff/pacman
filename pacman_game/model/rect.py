from .shape import Shape

## A class to represent rectangles by their size and position.
class Rect(Shape):

    ## Create a new Rectangle object.
    #
    # @param width The width of the rectangle.
    # @param height The height of the rectangle.
    # @param coordinate The coordinates where this rectangle is located
    # (can be None).
    def __init__(self, width, height, coordinate = None):
        Shape.__init__(self, coordinate)
        self._width = width
        self._height = height

    ## Get the width of the rectangle.
    #
    # @return The width of the rectangle.
    @property
    def width(self):
        return self._width

    ## Set the width of the rectangle.
    #
    # @param width The width of the rectangle.
    @width.setter
    def width(self, width):
        self._width = width

    ## Get the height of the rectangle.
    #
    # @return The height of the rectangle.
    @property
    def height(self):
        return self._height

    ## Set the height of the rectangle.
    #
    # @param height The height of the rectangle.
    @height.setter
    def height(self, height):
        self._height = height

    ## Create a new rectangle by moving this one by some offset.
    #
    # @param offset A coordinate object to be used as the amount by which
    # to move the rectangle.
    #
    # @return A new rectangle object moved by the amount offset.
    def move(self, offset):
        return Rect(self.width, self.height, self.coordinate.move(offset))

    ## Return a string to represent this rectangle.
    #
    # @return A string to represent this rectangle.
    def __str__(self):
        return f"{self.x}, {self.y}, {self.width}, {self.height}"
