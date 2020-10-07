import unittest
from pacman_game.model import dot
from pacman_game.model.coordinate import Coordinate

class DotTestCase(unittest.TestCase):
    def test_name(self):
        d = dot.Dot(Coordinate(0., 0.))
        assert(d.name == "dot")

dot_tests = unittest.makeSuite(DotTestCase, "test")
