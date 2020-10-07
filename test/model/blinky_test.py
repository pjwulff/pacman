import unittest
from pacman_game.model import blinky
from pacman_game.model.coordinate import Coordinate
from pacman_game.model.node import Node

class MockArena:
    def start_pos(self, name):
        return Node(Coordinate(50, 50))

class MockAvatar:
    @property
    def coordinate(self):
        return Coordinate(1, 2)

class BlinkyTestCase(unittest.TestCase):
    def setUp(self):
        self.blinky = blinky.Blinky(MockArena())

    def test_name(self):
        assert(self.blinky.name == "blinky")

    def test_target(self):
        target = self.blinky.target(MockAvatar(), {})
        assert(target.x == 1)
        assert(target.y == 2)

blinky_tests = unittest.makeSuite(BlinkyTestCase, "test")
