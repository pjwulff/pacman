from .arena import Arena
from .coordinate import Coordinate
from .node import Node

## A square (or rather rectangular grid) based Arena.
class SquareArena(Arena):

    ## Create a new SquareArena
    #
    # @param width The logical width of the graph.
    # @param height The logical height of the graph.
    def __init__(self, width, height):
        super().__init__(width, height, (width-1)*24, (height-1)*24, "square")
    
    ## Generate nodes in a grid.
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
        return nodes
