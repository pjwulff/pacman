import unittest
from pacman_game.model import circle
from pacman_game.model.coordinate import Coordinate

class CircleTestCase(unittest.TestCase):
    def test_radius(self):
        c = circle.Circle(0.)
        assert(c.radius == 0.)

    def test_radius_set(self):
        c = circle.Circle(0.)
        c.radius = 1.
        assert(c.radius == 1.)

    def test_radius_move(self):
        a = circle.Circle(1., Coordinate(2., 3.))
        b = a.move(Coordinate(4., 5.))
        assert(b.radius == 1.)
        assert(b.x == 6.)
        assert(b.y == 8.)

    def test_collide(self):
        a = circle.Circle(1., Coordinate(0., 0.))
        b = circle.Circle(1., Coordinate(0.5, 0.5))
        assert(a.collide(b) == True)
        assert(b.collide(a) == True)
        b = circle.Circle(1., Coordinate(-0.5, -0.5))
        assert(a.collide(b) == True)
        assert(b.collide(a) == True)
        a = circle.Circle(1., Coordinate(10., 10.))
        b = circle.Circle(10., Coordinate(10., 0.))
        assert(a.collide(b) == True)
        assert(b.collide(a) == True)

    def test_collide_boundary(self):
        a = circle.Circle(1., Coordinate(0., 0.))
        b = circle.Circle(1., Coordinate(2., 0.))
        assert(a.collide(b) == False)
        assert(b.collide(a) == False)

    def test_collide_far(self):
        a = circle.Circle(1., Coordinate(0., 0.))
        b = circle.Circle(1., Coordinate(10., 0.))
        assert(a.collide(b) == False)
        assert(b.collide(a) == False)

circle_tests = unittest.makeSuite(CircleTestCase, "test")
