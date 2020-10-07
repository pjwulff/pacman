import unittest
from pacman_game.model import avatar
from pacman_game.model.coordinate import Coordinate
from pacman_game.model.node import Node

class MockArena:
    def start_pos(self, name):
        return Node(Coordinate(50, 50))

class AvatarTestCase(unittest.TestCase):
    def setUp(self):
        self.avatar = avatar.Avatar(MockArena())

    def test_name(self):
        assert(self.avatar.name == "avatar")

avatar_tests = unittest.makeSuite(AvatarTestCase, "test")
