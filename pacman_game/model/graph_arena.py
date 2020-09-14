import math
import random
from .arena import Arena
from .coordinate import Coordinate
from .node import Node

class GraphArena(Arena):
    def __init__(self, rect):
        super().__init__(rect)

    def _too_close(self, node, nodes):
        for n in nodes:
            if n.distance(node) <= 12.0:
                return True
        return False

    def _generate_nodes(self, width, height):
        nodes = []
        max_nodes = width * height
        n = 0
        for i in range(width * height):
            while True:
                x = random.uniform(36, 36 + (width-1)*24)
                y = random.uniform(108, 108 + (height-1)*24)
                node = Node(Coordinate(x, y))
                if not self._too_close(node, nodes):
                    nodes += [node]
                    break

        for a in nodes:
            a_nodes = nodes[:]
            a_nodes = sorted(a_nodes, key = a.distance)
            for node in a_nodes[1:8]:
                a.add_geoneighbour(node)
        for a in nodes:
            temp = a.geoneighbours[:]
            for i in range(len(temp)):
                d = temp[i].direction(a)
                for j in range(i+1, len(temp)):
                    d2 = temp[j].direction(a)
                    if str(d) == str(d2) and temp[j] in a.geoneighbours:
                        a.remove_geoneighbour(temp[j])
        return nodes
