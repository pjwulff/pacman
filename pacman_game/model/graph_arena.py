import math
import random
from .angle import *
from .arena import Arena
from .coordinate import Coordinate
from .node import Node

## An arbitary graph based Arena.
class GraphArena(Arena):

    ## Create a new GraphArena.
    #
    # @param width The logical width of the graph.
    # @param height The logical height of the graph.
    def __init__(self, width, height):
        super().__init__(width, height, (width-1)*24, (height-1)*24, "graph")

    ## When generating nodes randomly we don't want them too close together.
    ## This functions returns true if some node is too close to some other
    ## nodes.
    #
    # @param node The node to test.
    # @param nodes A list of nodes against which to test the node.
    #
    # @return True if the node is too close to any in the list of nodes.
    def _too_close(self, node, nodes):
        for n in nodes:
            if n.distance(node) <= 24.0:
                return True
        return False

    ## Generate nodes randomly.
    #
    # @param width The logical width of the Arena.
    # @param height The logical height of the Arena.
    #
    # @return A list of nodes.
    def _generate_nodes(self, width, height):
        nodes = []
        max_nodes = width * height
        n = 0
        for i in range(width * height // 2):
            while True:
                x = random.uniform(0, (width-1)*24)
                y = random.uniform(0, (height-1)*24)
                node = Node(Coordinate(x, y))
                if not self._too_close(node, nodes):
                    nodes += [node]
                    break

        for a in nodes:
            a_nodes = nodes[:]
            a_nodes = sorted(a_nodes, key = a.distance)
            for node in a_nodes[1:]:
                a.add_geoneighbour(node)
        for a in nodes:
            temp = a.geoneighbours[:]
            for i in range(len(temp)):
                d1 = temp[i].direction(a)
                for j in range(i+1, len(temp)):
                    d2 = temp[j].direction(a)
                    if close(d1, d2, math.pi/4.) and temp[j] in a.geoneighbours:
                        a.remove_geoneighbour(temp[j])
                        temp[j].remove_geoneighbour(a)
        return nodes
