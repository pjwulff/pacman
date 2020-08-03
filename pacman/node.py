import math

class Node:
    def __init__(self, x, y):
        self.x_ = x
        self.y_ = y
        self.neighbours = {}

    def x(self):
        return self.x_

    def y(self):
        return self.y_

    def set_neighbour(self, direction, neighbour):
        self.neighbours[direction] = neighbour

    def neighbour(self, direction):
        if direction in self.neighbours:
            return self.neighbours[direction]
        else:
            return None

    def distance(self, other):
        dx = (other.x() - self.x()) ** 2
        dy = (other.y() - self.y()) ** 2
        return math.sqrt(dx + dy)
