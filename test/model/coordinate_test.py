import unittest
from pacman_game.model import coordinate

class CoordinateTestCase(unittest.TestCase):
    def test_x(self):
        c = coordinate.Coordinate(0., 0.)
        assert(c.x == 0.)
        c = coordinate.Coordinate(100., 0.)
        assert(c.x == 100.)

    def test_x_set(self):
        c = coordinate.Coordinate(0., 0.)
        c.x = 100.
        assert(c.x == 100.)

    def test_y(self):
        c = coordinate.Coordinate(0., 0.)
        assert(c.y == 0.)
        c = coordinate.Coordinate(0., 100.)
        assert(c.y == 100.)

    def test_y_set(self):
        c = coordinate.Coordinate(0., 0.)
        c.y = 100.
        assert(c.y == 100.)

    def test_move(self):
        a = coordinate.Coordinate(1., 2.)
        b = coordinate.Coordinate(3., 4.)
        c = a.move(b)
        assert(c.x == 4.)
        assert(c.y == 6.)
        c = b.move(a)
        assert(c.x == 4.)
        assert(c.y == 6.)

    def test_distance(self):
        a = coordinate.Coordinate(0., 0.)
        b = coordinate.Coordinate(1., 0.)
        assert(a.distance(b) == 1.)
        assert(b.distance(a) == 1.)

coordinate_tests = unittest.makeSuite(CoordinateTestCase, "test")
