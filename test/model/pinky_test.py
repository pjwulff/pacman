import unittest
from pacman_game.model import pinky
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

class PinkyTestCase(unittest.TestCase):
    def setUp(self):
        self.pinky = pinky.Pinky(MockArena())

    def test_name(self):
        assert(self.pinky.name == "pinky")

    def test_target(self):
        target = self.pinky.target(MockAvatar(), {})
        assert(target.x == 40.)
        assert(target.y == 0.)

pinky_tests = unittest.makeSuite(PinkyTestCase, "test")
