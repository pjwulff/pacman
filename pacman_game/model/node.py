import math
from .coordinate import Coordinate
from .direction import Direction

class Node:
    """! Represents a vertex in the direction graph of the maze."""
    def __init__(self, coordinate):
        """! Create a new node in the graph.

        @param arena The arena to which this node belonds.
        @param x,y The coordinates of this node."""
        self._coordinate = coordinate
        self._geoneighbours = []
        self._neighbours = []

    @property
    def x(self):
        """! Get the x coordinate of this node.

        @returns The x coordinate of this node."""
        return self._coordinate.x

    @property
    def y(self):
        """! Get the y coordinate of this node.

        @returns the y coordinate of this node."""
        return self._coordinate.y

    @property
    def neighbours(self):
        return self._neighbours

    @property
    def geoneighbours(self):
        return self._geoneighbours
    
    @property
    def coordinate(self):
        return self._coordinate

    def add_neighbour(self, neighbour):
        if neighbour is None:
            raise "wtf"
        if neighbour not in self.neighbours:
            self._neighbours += [neighbour]

    def remove_neighbour(self, neighbour):
        if neighbour is None:
            raise "wtf"
        self._neighbours.remove(neighbour)

    def add_geoneighbour(self, neighbour):
        if neighbour not in self.geoneighbours:
            self._geoneighbours += [neighbour]

    def remove_geneighbour(self, geoneighbour):
        self._geoneighbours.remove(neighbour)

    def distance(self, other):
        other_x = other.x
        other_y = other.y
        dx = (other_x - self.x) ** 2
        dy = (other_y - self.y) ** 2
        return math.sqrt(dx + dy)

    def is_neighbour(self, node):
        return node in self.neighbours

    def is_geoneighbour(self, node):
        return node in self.geoneighbours

    def angle(self, node):
        dx = node.x - self.x
        dy = node.y - self.y
        a = math.atan2(-dy, dx)
        if a >= 2 * math.pi:
            a -= 2 * math.pi
        elif a < 0:
            a += 2 * math.pi
        return a

    def neighbour(self, direction):
        if not direction.valid:
            return None
        target = direction.angle
        for n in self.neighbours:
            if n is None:
                raise self.neighbours
            a = self.angle(n)
            if abs(target - a) <= math.pi/8.:
                return n
        return None

    def direction(self, node):
        a = self.angle(node)
        return Direction.from_angle(a)
