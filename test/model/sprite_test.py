import unittest
from pacman_game.model import sprite
from pacman_game.model.coordinate import Coordinate
from pacman_game.model.node import Node

class SpriteTestCase(unittest.TestCase):
    def setUp(self):
        self.s = sprite.Sprite(Coordinate(0., 0.,), 1., "sprite")

    def test_name(self):
        assert(self.s.name == "sprite")

    def test_x(self):
        assert(self.s.x == 0.)

    def test_x_set(self):
        self.s.x = 1.
        assert(self.s.x == 1.)

    def test_y(self):
        assert(self.y == 0.)

    def test_y_set(self):
        self.s.y = 1.
        assert(self.y == 1.)

    def test_circle(self):
        c = self.s.cirlce
        assert(c.radius == 1.)
        assert(c.x == 0.)
        assert(c.y == 0.)

sprite_tests = unittest.makeSuite(SpriteTestCase, "sprite")
