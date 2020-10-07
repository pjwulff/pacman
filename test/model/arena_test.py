import random
import unittest
from pacman_game.model import arena
from pacman_game.model.coordinate import Coordinate
from pacman_game.model.node import Node

class TestArena(arena.Arena):
    def __init__(self):
        super().__init__(10, 10, 100, 100, "shape")

    def _generate_nodes(self, width, height):
        nodes = [None] * 100
        for i in range(10):
            for j in range(10):
                coordinate = Coordinate(i*10, j*10)
                node = Node(coordinate)
                nodes[i+j*10] = node

        for i in range(10):
            for j in range(10):
                node = nodes[i + j*10]
                if i < 9:
                    node_right = nodes[(i+1) + j*10]
                    node.add_geoneighbour(node_right)
                    node_right.add_geoneighbour(node)
                if j < 9:
                    node_down = nodes[i + (j+1)*10]
                    node.add_geoneighbour(node_down)
                    node_down.add_geoneighbour(node)
        return nodes

class ArenaTestCase(unittest.TestCase):
    def setUp(self):
        self.arena = TestArena()
        self.nodes = self.arena.nodes

    def test_shape(self):
        assert(self.arena.shape == "shape")

    def test_smoke_nodes(self):
        assert(len(self.nodes) == 100)

    def test_closest(self):
        top_left = self.nodes[0]
        top_right = self.nodes[9]
        bottom_left = self.nodes[90]
        bottom_right = self.nodes[99]
        assert(self.arena.closest_node(0, 0) == top_left)
        assert(self.arena.closest_node(100, 0) == top_right)
        assert(self.arena.closest_node(0, 100) == bottom_left)
        assert(self.arena.closest_node(100, 100) == bottom_right)

    def test_heuristic(self):
        ## This that the triangle inequality holds for the generated heuristic.
        for i in range(100):
            node = self.nodes[i]
            other_node = None
            while True:
                other_node = random.choice(self.nodes)
                if other_node not in node.neighbours:
                    break
            path_length = self.arena.heuristic(node, other_node)
            for neighbour in node.neighbours:
                neighbour_distance = node.distance(neighbour)
                neighbour_heuristic = self.arena.heuristic(neighbour, other_node)
                assert(path_length <= neighbour_distance + neighbour_heuristic)

    def test_start_pos(self):
        assert(self.arena.start_pos("avatar") == self.arena.closest_node(50, 50))
        assert(self.arena.start_pos("pinky") == self.arena.closest_node(0, 0))
        assert(self.arena.start_pos("blinky") == self.arena.closest_node(100, 0))
        assert(self.arena.start_pos("clyde") == self.arena.closest_node(0, 100))
        assert(self.arena.start_pos("inky") == self.arena.closest_node(100, 100))

    def test_logical_width(self):
        assert(self.arena.logical_width == 10)

    def test_logical_height(self):
        assert(self.arena.logical_height == 10)

    def test_dots(self):
        dots = self.arena.dots
        ## There should be 100 vertices in the maze, but 5 will take by
        ## start positions, and 4 will be power pills, so there should be
        ## 91 dots in the arena.
        assert(len(dots) == 91)

    def test_powers(self):
        powers = self.arena.powers
        assert(len(powers) == 4)

    def test_rect(self):
        rect = self.arena.rect
        assert(rect.width == 100)
        assert(rect.height == 100)

    def test_width(self):
        assert(self.arena.width == 100)

    def test_height(self):
        assert(self.arena.height == 100)

arena_tests = unittest.makeSuite(ArenaTestCase, "test")
