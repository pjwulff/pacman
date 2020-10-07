from .arena import Arena
from .coordinate import Coordinate
from .node import Node

HEX_SCALE = 0.866

## A hexagonal based Arena
class HexagonalArena(Arena):

    ## Create a new HexagonalArena
    #
    # @param width The logical width of the Arena.
    # @param height The logical height of the Arena.
    def __init__(self, width, height):
        width += width % 2
        height += height % 2
        super().__init__(width, height, (width-1)*24+12, (height-1)*24*HEX_SCALE, "hexagonal")

    ## Generate nodes based on a hexagonal grid.
    #
    # @param width The logical width of the Arena.
    # @param height The logical height of the Arena.
    #
    # @return A list of nodes.
    def _generate_nodes(self, width, height):
        num_nodes = width * height
        nodes = [None] * num_nodes
        for i in range(width):
            for j in range(height):
                x = i*24
                y = j*24*HEX_SCALE
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
                        if j > 0 and i < (width - 1):
                            node.add_geoneighbour(nodes[num+1-width])
                            nodes[num+1-width].add_geoneighbour(node)
                        if j < (height - 1) and i < (width - 1):
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
        return nodes
