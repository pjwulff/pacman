import math
from itertools import count
from queue import PriorityQueue
from .coordinate import Coordinate
from .angle import *

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

    def remove_geoneighbour(self, neighbour):
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

    def neighbour(self, direction, threshold = math.pi/8.):
        if direction is None:
            return None
        best_neighbour = None
        best_error = 1000.0
        for n in self.neighbours:
            error = angle(self.direction(n), direction)
            if error <= threshold and error < best_error:
                best_error = error
                best_neighbour = n
        return best_neighbour

    def direction(self, node):
        dx = node.x - self.x
        dy = node.y - self.y
        return normalise(math.atan2(-dy, dx))
