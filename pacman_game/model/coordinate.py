import math

## A class to represent coordinates.
class Coordinate:

    ## Create new coordinates.
    #
    # @param x The x coordinate (defaults to zero).
    # @param y The y coordinate (defaults to zero).
    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y
    
    ## Get the x-coordinate.
    #
    # @return The x-coordinate.
    @property
    def x(self):
        return self._x

    ## Set the x-coordinate.
    #
    # @param x The x-coordinate.
    @x.setter
    def x(self, x):
        self._x = x
        
    ## Get the y-coordinate
    #
    # @return The y-coordinate.
    @property
    def y(self):
        return self._y
    
    ## Set the y-coordiate.
    #
    # @param y The y-coordinate.
    @y.setter
    def y(self, y):
        self._y = y
    
    ## Return a new coordinate based on this one but shifted by some amount.
    #
    # @param other Another coordinate object that decides by how much to shift.
    # Equivalently the two coordinates can be viewed as vectors, in which case
    # this is just vector addition.
    #
    # @return The new shifted coordinate/vector.
    def move(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)
    
    ## Calculate the distance between two points in space.
    #
    # @param other The other coordinates.
    #
    # @return The distance between these coordinates and the other coordinates.
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx*dx + dy*dy)
