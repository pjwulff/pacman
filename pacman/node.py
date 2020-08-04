import math

class Node:
    def __init__(self, arena, x, y):
        self._x = x
        self._y = y
        self._arena = arena
        self._neighbours = {}
        self._portals = {}
        self._contents = None

    def x(self):
        return self._x

    def y(self):
        return self._y

    def set_contents(self, contents):
        self._contents = contents

    def contents(self):
        return self._contents

    def set_neighbour(self, direction, neighbour):
        self._neighbours[direction] = neighbour

    def set_portal(self, direction, portal):
        self._portals[direction] = portal

    def neighbour(self, direction):
        if direction in self._neighbours:
            return self._neighbours[direction]
        else:
            return None

    def portal(self, direction):
        if direction in self._portals:
            return self._portals[direction]
        else:
            return None

    def distance(self, other):
        other_x = other.x()
        other_y = other.y()
        if self.portal("left") == other:
            other_x -= self.arena.rect().width
        if self.portal("right") == other:
            other_x += self.arena.rect().width
        if self.portal("up") == other:
            other_x -= self.arena.rect().height
        if self.portal("down") == other:
            other_x += self.arena.rect().height
        dx = (other_x - self.x()) ** 2
        dy = (other_y - self.y()) ** 2
        return math.sqrt(dx + dy)
