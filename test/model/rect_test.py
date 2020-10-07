import unittest
from pacman_game.model import rect
from pacman_game.model.coordinate import Coordinate

class RectTestCase(unittest.TestCase):
    def test_width(self):
        r = rect.Rect(0., 0.)
        assert(r.width == 0.)

    def test_width_set(self):
        r = rect.Rect(0., 0.)
        r.width = 1.
        assert(r.width == 1.)

    def test_height(self):
        r = rect.Rect(0., 0.)
        assert(r.height == 0.)

    def test_height_set(self):
        r = rect.Rect(0., 0.)
        r.height = 1.
        assert(r.height == 1.)

    def test_move(self):
        a = rect.Rect(1., 3., Coordinate(4., 5.))
        b = a.move(Coordinate(6., 7.))
        assert(a.width == 1.)
        assert(a.height == 3.)
        assert(b.x == 10.)
        assert(b.y == 12.)

rect_tests = unittest.makeSuite(RectTestCase, "test")
