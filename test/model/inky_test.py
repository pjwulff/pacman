import unittest
from pacman_game.model import inky
from pacman_game.model.coordinate import Coordinate
from pacman_game.model.node import Node

class MockArena:
    def start_pos(self, name):
        return Node(Coordinate(50, 50))

class MockAvatar:
    @property
    def from_pos(self):
        return Node(Coordinate(0., 0.))

    @property
    def to_pos(self):
        return Node(Coordinate(10., 0.))

class MockBlinky:
    @property
    def coordinate(self):
        return Coordinate(100., 100.)

class InkyTestCase(unittest.TestCase):
    def setUp(self):
        self.inky = inky.Inky(MockArena())

    def test_name(self):
        assert(self.inky.name == "inky")

    def test_target(self):
        target = self.inky.target(MockAvatar(), {"blinky": MockBlinky()})
        assert(target.x == -60.)
        assert(target.y == -100.)

inky_tests = unittest.makeSuite(InkyTestCase, "test")
