from .arena import Arena
from .coordinate import Coordinate
from .node import Node

class HexagonalArena(Arena):
    def __init__(self, rect):
        super().__init__(rect)
        self._width = self._logical_width*24 + 64
        self._height = self._logical_height*24 + 96

    def _generate_nodes(self, width, height):
        num_nodes = width * height
        nodes = [None] * num_nodes
        for i in range(width):
            for j in range(height):
                x = 36 + i*24
                y = 108 + j*24*0.866
                if j % 2 == 0:
                    x += 12
                node = Node(Coordinate(x, y))
                nodes[i+j*width] = node
        for i in range(width):
            for j in range(height):
                num = i+j*width
                node = nodes[num]
                if j % 2 == 0:
                    if i % 3 == 0 and i < (width -1):
                        node.add_geoneighbour(nodes[num+1])
                        nodes[num+1].add_geoneighbour(node)
                    elif i % 3 == 1:
                        if j > 0:
                            node.add_geoneighbour(nodes[num+1-width])
                            nodes[num+1-width].add_geoneighbour(node)
                        node.add_geoneighbour(nodes[num+1+width])
                        nodes[num+1+width].add_geoneighbour(node)
                else:
                    if i % 3 == 2 and i < (width - 1):
                        node.add_geoneighbour(nodes[num+1])
                        nodes[num+1].add_geoneighbour(node)
                    elif i % 3 == 0:
                        node.add_geoneighbour(nodes[num-width])
                        nodes[num-width].add_geoneighbour(node)
                        if j < (height - 1):
                            node.add_geoneighbour(nodes[num+width])
                            nodes[num+width].add_geoneighbour(node)
        middle = num_nodes // 2
        return nodes
