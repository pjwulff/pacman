from .arena import Arena
from .coordinate import Coordinate
from .node import Node

class SquareArena(Arena):
    def __init__(self, width, height):
        super().__init__(width, height, (width-1)*24, (height-1)*24, "square")
    
    def _generate_nodes(self, width, height):
        num_nodes = width * height
        nodes = [None] * num_nodes
        for i in range(width):
            for j in range(height):
                x = i*24
                y = j*24
                node = Node(Coordinate(x, y))
                nodes[i+j*width] = node
        for i in range(width):
            for j in range(height):
                if i < (width - 1):
                    nodes[i+j*width].add_geoneighbour(nodes[i+1+j*width])
                if 0 < i:
                    nodes[i+j*width].add_geoneighbour(nodes[i-1+j*width])
                if j < (height - 1):
                    nodes[i+j*width].add_geoneighbour(nodes[i+(j+1)*width])
                if 0 < j:
                    nodes[i+j*width].add_geoneighbour(nodes[i+(j-1)*width])
        self._avatar_start = nodes[width//2 + width*(2*height//3)-1]
        self._ghost_return = nodes[width//2 + width*height//2]
        self._pinky_start = nodes[0]
        self._blinky_start = nodes[width-1]
        self._inky_start = nodes[num_nodes-1]
        self._clyde_start = nodes[num_nodes-width]
        return nodes
