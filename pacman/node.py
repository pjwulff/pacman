import math

class Node:
    def __init__(self, arena, x, y):
        self.x_ = x
        self.y_ = y
        self.arena = arena
        self.neighbours = {}
        self.portals = {}

    def x(self):
        return self.x_

    def y(self):
        return self.y_

    def set_neighbour(self, direction, neighbour):
        self.neighbours[direction] = neighbour

    def set_portal(self, direction, portal):
        self.portals[direction] = portal

    def neighbour(self, direction):
        if direction in self.neighbours:
            return self.neighbours[direction]
        else:
            return None

    def portal(self, direction):
        if direction in self.portals:
            return self.portals[direction]
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
