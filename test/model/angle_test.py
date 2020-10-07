import math
import unittest
from pacman_game.model import angle

class NormaliseTestCase(unittest.TestCase):
    def test_smoke(self):
        assert(angle.normalise(0) == 0)

    def test_pos(self):
        assert(angle.normalise(1.0) == 1.0)

    def test_neg(self):
        assert(angle.normalise(-1.0) == -1.0)

    def test_pos_boundary(self):
        assert(angle.normalise(math.pi) == -math.pi)

    def test_neg_boundary(self):
        assert(angle.normalise(-math.pi) == -math.pi)

    def test_double(self):
        assert(angle.normalise(2*math.pi) == 0.)

    def test_double_neg(self):
        assert(angle.normalise(-2*math.pi) == 0.)

class CloseTestCase(unittest.TestCase):
    def test_smoke(self):
        assert(angle.close(0.0, 0.0, 1.0)) == True

    def test_threshold(self):
        assert(angle.close(0., 1., 1.) == True)

    def test_threshold_flip(self):
        assert(angle.close(1., 0., 1.) == True)

    def test_split(self):
        assert(angle.close(-math.pi, math.pi - 0.1, 0.1) == True)

    def test_wrap(self):
        assert(angle.close(0, 2*math.pi, 0.01) == True)

    def test_smoke_far(self):
        assert(angle.close(0., 2., 1.0) == False)

    def test_threshold_far(self):
        assert(angle.close(0., 1., 0.5) == False)

    def test_threshold_flip_far(self):
        assert(angle.close(1., 0., 0.5) == False)

    def test_split_far(self):
        assert(angle.close(-math.pi, math.pi - 1.0, 0.5) == False)

    def test_wrap_far(self):
        assert(angle.close(0., 2*math.pi+0.1, 0.05) == False)


class FlipTestCase(unittest.TestCase):
    def test_smoke(self):
        assert(angle.flip(0.) == -math.pi)

    def test_boundary(self):
        assert(angle.flip(-math.pi) == 0.)

    def test_boundary_pos(self):
        assert(angle.flip(math.pi) == 0.)


class AngleTestCase(unittest.TestCase):
    def test_smoke(self):
        assert(angle.angle(0., 1.) == 1.)

    def test_flip(self):
        assert(angle.angle(1., 0.) == 1.)

    def test_boundary(self):
        assert(angle.angle(0., math.pi) == math.pi)

    def test_boundary_neg(self):
        assert(angle.angle(0., -math.pi) == math.pi)

normalise_test_suite = unittest.makeSuite(NormaliseTestCase, "test")
close_test_suite = unittest.makeSuite(CloseTestCase, "test")
flip_test_suite = unittest.makeSuite(FlipTestCase, "test")
angle_test_suite = unittest.makeSuite(AngleTestCase, "test")
angle_tests = unittest.TestSuite((
    normalise_test_suite,
    close_test_suite,
    flip_test_suite,
    angle_test_suite,
))

