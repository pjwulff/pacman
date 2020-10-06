import unittest
from . import dot
from .coordinate import Coordinate

class DotTestCase(unittest.TestCase):
    def test_name(self):
        d = dot.Dot(Coordinate(0., 0.))
        assert(d.name == "dot")

dot_tests = unittest.makeSuite(DotTestCase, "test")
