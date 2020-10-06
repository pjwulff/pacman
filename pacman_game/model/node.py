import math
from itertools import count
from queue import PriorityQueue
from .coordinate import Coordinate
from .angle import *

## Represents a node or vertex in the directed graph of the maze.
class Node:

    ## Create a new node.
    #
    # @param coordinate The coordinates where this node is located.
    def __init__(self, coordinate):
        self._coordinate = coordinate
        self._geoneighbours = []
        self._neighbours = []

    ## Get the x-coordinate of this node.
    #
    # @return The x-coordinate of this node.
    @property
    def x(self):
        return self._coordinate.x

    ## Get the y-coordinate of this node.
    #
    # @return The y-coordinate of this node.
    @property
    def y(self):
        return self._coordinate.y

    ## Get the neighbours of this node; that is, other nodes which are connected
    ## to this one by an edge.
    #
    # @return A list of neighbouring nodes.
    @property
    def neighbours(self):
        return self._neighbours

    ## Get the geoneighbours of this node; that is, nodes which are `next to'
    ## this node in space, but which may not be connected by an edge in the
    ## graph.
    #
    # @return A list of geoneighbouring nodes.
    @property
    def geoneighbours(self):
        return self._geoneighbours
    
    ## Get the coordinates of this node.
    #
    # @return The coordinates of this node.
    @property
    def coordinate(self):
        return self._coordinate

    ## Add another node as a neighbour of this node. That is, add a
    ## directed edge from this node to the other node.
    #
    # @param neighbour The node which to add as a neighbour.
    def add_neighbour(self, neighbour):
        if neighbour is None:
            raise ValueError("neighbour cannot be None")
        if neighbour not in self.neighbours:
            self._neighbours += [neighbour]

    ## Remove another node as a neighbour of this node. That is, remove the
    ## edge from this node to the other node.
    #
    # @param neighbour The neighbouring node to remove.
    def remove_neighbour(self, neighbour):
        if neighbour is None:
            raise ValueError("neighbour cannot be None")
        self._neighbours.remove(neighbour)

    ## Add another node as a geoneighbour to this node; that is, a neighbour
    ## in space, but not necessarily in the directed graph.
    #
    # @param neighbour The geoneighour to add.
    def add_geoneighbour(self, neighbour):
        if neighbour not in self.geoneighbours:
            self._geoneighbours += [neighbour]

    ## Remove another node as a geoneighbour to this node.
    #
    # @param neighbour The geoneighbour to remove.
    def remove_geoneighbour(self, neighbour):
        self._geoneighbours.remove(neighbour)

    ## Calculates the distance between this node and another node.
    #
    # @param other The other node.
    #
    # @return The distance between them.
    def distance(self, other):
        other_x = other.x
        other_y = other.y
        dx = (other_x - self.x) ** 2
        dy = (other_y - self.y) ** 2
        return math.sqrt(dx + dy)

    ## A predicate to detect if two nodes are neighbours.
    #
    # @param node The other node.
    #
    # @return True if the nodes are neighbours.
    def is_neighbour(self, node):
        return node in self.neighbours

    ## A predicate to detect if two nodes are geoneighbours.
    #
    # @param node The other node.
    #
    # @return True if the nodes are geoneighbours.
    def is_geoneighbour(self, node):
        return node in self.geoneighbours

    ## Finds the neighbouring node which is closest to the desired direction
    ## within some threshold. May return if this node has no neighbour
    ## in the desired direction.
    #
    # @param direction The direction in which to look for a neighbour.
    # @param threshold The threshold angle to decide if a neighbouring node
    # is sufficiently in the target direction. Defaults to pi/8.
    #
    # @return A node if a neighbour could be found, or None otherwise.
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

    ## Calculate the angle or direction from this node to another.
    #
    # @param node The other node.
    #
    # @return The angle between them if travelling from this node to the other
    # node.
    def direction(self, node):
        dx = node.x - self.x
        dy = node.y - self.y
        return normalise(math.atan2(-dy, dx))
