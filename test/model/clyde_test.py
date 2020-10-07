import unittest
from pacman_game.model import clyde
from pacman_game.model.coordinate import Coordinate
from pacman_game.model.node import Node

class MockArena:
    def start_pos(self, name):
        return Node(Coordinate(0, 0))

class MockAvatar:
    def __init__(self, coordinate):
        self.coordinate = coordinate

class ClydeTestCase(unittest.TestCase):
    def setUp(self):
        self.clyde = clyde.Clyde(MockArena())

    def test_name(self):
        assert(self.clyde.name == "clyde")

    def test_target(self):
        target = self.clyde.target(MockAvatar(Coordinate(100., 100.)), {})
        assert(target.x == 0.)
        assert(target.y == 0.)
        target = self.clyde.target(MockAvatar(Coordinate(200., 200.)), {})
        assert(target.x == 200.)
        assert(target.y == 200.)

clyde_tests = unittest.makeSuite(ClydeTestCase, "test")
