from .coordinate import Coordinate

## A base class for shapes.
class Shape:

    ## Create a new Shape object.
    #
    # @param coordinate The coordinates in space where this shape lives.
    def __init__(self, coordinate = None):
        if coordinate is not None:
            self._coordinate = coordinate
        else:
            self._coordinate = Coordinate(0, 0)

    ## Get the x-coordinate of this shape.
    #
    # @return The x-coordinate of this shape.
    @property
    def x(self):
        return self._coordinate.x

    ## Set the x-coordinate of this shape.
    #
    # @param x The x-coordinate of this shape.
    @x.setter
    def x(self, x):
        self._coordinate.x = x

    ## Get the y-coordinate of this shape.
    #
    # @return The y-coordinate of this shape.
    @property
    def y(self):
        return self._coordinate.y

    ## Set the y-coordinate of this shape.
    #
    # @param y The y-coordinate of this shape.
    @y.setter
    def y(self, y):
        self._coordinate.y = y
    
    ## Get the coordinates of this shape.
    #
    # @return The coordinates of this shape.
    @property
    def coordinate(self):
        return self._coordinate

    ## Set the coordinates of this shape.
    #
    # @param coordinate The coordinates of this shape.
    @coordinate.setter
    def coordinate(self, coordinate):
        self._coordinate = coordinate
