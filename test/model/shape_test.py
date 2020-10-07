import unittest
from pacman_game.model import shape
from pacman_game.model.coordinate import Coordinate

class ShapeTestCase(unittest.TestCase):
    def test_x(self):
        s = shape.Shape(Coordinate(0., 0.))
        assert(s.x == 0.)

    def test_x_set(self):
        s = shape.Shape(Coordinate(0., 0.))
        s.x = 1.
        assert(s.x == 1.)

    def test_y(self):
        s = shape.Shape(Coordinate(0., 0.))
        assert(s.y == 0.)

    def test_y_set(self):
        s = shape.Shape(Coordinate(0., 0.))
        s.y = 1.
        assert(s.y == 1.)

shape_tests = unittest.makeSuite(ShapeTestCase, "test")
