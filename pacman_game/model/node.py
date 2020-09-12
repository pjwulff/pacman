import math
from .coordinate import Coordinate

class Node:
    """! Represents a vertex in the direction graph of the maze."""
    def __init__(self, arena, coordinate):
        """! Create a new node in the graph.

        @param arena The arena to which this node belonds.
        @param x,y The coordinates of this node."""
        self._coordinate = coordinate
        self._arena = arena
        self._neighbours = {}
        self._portals = {}

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
    def coordinate(self):
        return self._coordinate

    def set_neighbour(self, direction, neighbour):
        """! Sets another node in the graph as a neighbour to this node.

        @param direction A label to describe how the two nodes relate.
        @param neighbour The node which neighbours this one."""
        self._neighbours[str(direction)] = neighbour

    def set_portal(self, direction, portal):
        """! Sets another node as a portal destination from this node.
        This allows the avatar to wrap around the map as in the original game.

        @param direction A label to describe how the two nodes relate.
        @param portal The node to which this node warps."""
        self._portals[str(direction)] = portal

    def neighbour(self, direction):
        """! Get the neighbouring node in a particular direction.

        @param direction The label used to describe the direction.
        @returns The node in that direction if one exists, None otherwise."""
        if str(direction) in self._neighbours:
            return self._neighbours[str(direction)]
        else:
            return None

    def portal(self, direction):
        """! Gets the portal node in a particular direction.

        @param direction The label used to describe the direction.
        @returns The node in that direction if one exists, None otherwise."""
        if str(direction) in self._portals:
            return self._portals[str(direction)]
        else:
            return None

    def distance(self, other):
        """ The euclidean distance between two nodes. This method takes into
        account if one node is a portal to another.

        @param other The other node to which the distance should be calculated.
        @returns The euclidean distance between if not connected by a portal,
        or the logical distance if they do."""
        other_x = other.x
        other_y = other.y
        if self.portal("left") == other:
            other_x -= self._arena.rect.width
        if self.portal("right") == other:
            other_x += self._arena.rect.width
        if self.portal("up") == other:
            other_x -= self._arena.rect.height
        if self.portal("down") == other:
            other_x += self._arena.rect.height
        dx = (other_x - self.x) ** 2
        dy = (other_y - self.y) ** 2
        return math.sqrt(dx + dy)
