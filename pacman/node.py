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

    def get_neighbour(self, direction):
        return self.neighbours[direction]
