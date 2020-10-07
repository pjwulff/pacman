import unittest
from pacman_game.model import power
from pacman_game.model.coordinate import Coordinate

class PowerTestCase(unittest.TestCase):
    def test_name(self):
        p = power.Power(Coordinate(0., 0.))
        assert(p.name == "power")

power_tests = unittest.makeSuite(PowerTestCase, "test")
