from .circle import Circle

class Sprite:
    """! Base class for all displayable sprites.

    """
    def __init__(self, arena, coordinate, radius, name):
        """! Base constructor for sprites.

        @param arena The arena to which this sprite belongs.
        @param x,y   The coordinates where this sprite should spawn.
        @param name  The name of this sprite."""
        self._arena = arena
        self._coordinate = coordinate
        self._radius = radius
        self._name = name

    @property
    def x(self):
        return self.coordinate.x

    @x.setter
    def x(self, x):
        self.coordinate.x = x

    @property
    def y(self):
        return self.coordinate.y

    @y.setter
    def y(self, y):
        self.coordinate.y = y
    
    @property
    def coordinate(self):
        return self._coordinate
    
    @coordinate.setter
    def coordinate(self, coordinate):
        self._coordinate = coordinate
    
    @property
    def circle(self):
        return Circle(self._radius, self._coordinate)
    
    def collide(self, other):
        return self.circle.collide(other.circle)
    
    @property
    def name(self):
        return self._name
    
    @property
    def rect(self):
        return 
