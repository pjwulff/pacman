import unittest
from . import ghost
from .coordinate import Coordinate
from .node import Node

class MockArena:
    def start_pos(self, name):
        return Node(Coordinate(0., 0.))

class GhostTestCase(unittest.TestCase):
    def setUp(self):
        self.ghost = ghost.Ghost(MockArena(), "blinky")

    def test_mode(self):
        assert(self.ghost.mode == "scatter")

    def test_mode_set(self):
        self.ghost.mode = "chase"
        assert(self.ghost.mode == "chase")

    def test_scared(self):
        assert(self.ghost.scared == False)
        self.ghost.mode = "frighten"
        assert(self.ghost.scared == True)

    def test_alive(self):
        assert(self.ghost.alive == True)

    def test_alive_set(self):
        self.ghost.alive = False
        assert(self.ghost.alive == False)

ghost_tests = unittest.makeSuite(GhostTestCase, "test")
