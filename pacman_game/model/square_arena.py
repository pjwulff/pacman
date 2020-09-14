from .arena import Arena
from .coordinate import Coordinate
from .direction import Direction
from .node import Node

class SquareArena(Arena):
    def __init__(self, rect):
        super().__init__(rect)
    
    def _generate_nodes(self, width, height):
        nodes = [None] * width
        for i in range(width):
            nodes[i] = [None] * height
            for j in range(height):
                x = 36 + i*24
                y = 108 + j*24
                node = Node(self, Coordinate(x, y))
                nodes[i][j] = node
        for i in range(width):
            for j in range(height):
                if i < (width - 1):
                    nodes[i][j].set_geoneighbour(Direction("right"), nodes[i+1][j])
                if 0 < i:
                    nodes[i][j].set_geoneighbour(Direction("left"), nodes[i-1][j])
                if j < (height - 1):
                    nodes[i][j].set_geoneighbour(Direction("down"), nodes[i][j+1])
                if 0 < j:
                    nodes[i][j].set_geoneighbour(Direction("up"), nodes[i][j-1])
        self._avatar_start = (nodes[width//2-1][2*height//3], nodes[width//2][2*height//3])
        self._join(self._avatar_start[0], self._avatar_start[1])
        self._ghost_return = (nodes[width//2-1][height//2-2], nodes[width//2][height//2-2])
        self._join(self._ghost_return[0], self._ghost_return[1])
        self._ghost_return = nodes[width//2][height//2-3]

        self._pinky_start = (nodes[0][0], nodes[1][0])
        self._join(self._pinky_start[0], self._pinky_start[1])

        self._blinky_start = (nodes[width-2][0], nodes[width-1][0])
        self._join(self._blinky_start[0], self._blinky_start[1])

        self._inky_start = (nodes[width-1][height-2], nodes[width-1][height-1])
        self._join(self._inky_start[0], self._inky_start[1])

        self._clyde_start = (nodes[0][height-2], nodes[0][height-1])
        self._join(self._clyde_start[0], self._clyde_start[1])
        return nodes
