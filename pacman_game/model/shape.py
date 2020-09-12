from .coordinate import Coordinate

class Shape:
    def __init__(self, coordinate = None):
        if coordinate is not None:
            self._coordinate = coordinate
        else:
            self._coordinate = Coordinate(0, 0)

    @property
    def x(self):
        return self._coordinate.x

    @x.setter
    def x(self, x):
        self._coordinate.x = x

    @property
    def y(self):
        return self._coordinate.y

    @y.setter
    def y(self, y):
        self._coordinate.y = y
    
    @property
    def coordinate(self):
        return self._coordinate

    @coordinate.setter
    def coordinate(self, coordinate):
        self._coordinate = coordinate
