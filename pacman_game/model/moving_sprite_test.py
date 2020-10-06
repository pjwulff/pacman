import unittest
from . import moving_sprite
from .coordinate import Coordinate
from .node import Node

class MockArena:
    def start_pos(self, name):
        return Node(Coordinate(0., 0.))

class MovingSpriteTestCase(unittest.TestCase):
    def setUp(self):
        self.mv = moving_sprite.MovingSprite(MockArena(), 1., "test")

    def test_return_to_spawn(self):
        self.mv.return_to_spawn()
        assert(self.mv.x == 0.)
        assert(self.mv.y == 0.)

    def test_trans_pos(self):
        assert(self.mv.trans_pos == 0.)

    def test_trans_pos_set(self):
        self.mv.trans_pos = 0.5
        assert(self.mv.trans_pos == 0.5)

    def test_from_pos(self):
        f = self.mv.from_pos
        assert(f.x == 0.)
        assert(f.y == 0.)

    def test_from_pos_set(self):
        self.mv.from_pos = Node(Coordinate(1., 1.))
        f = self.mv.from_pos
        assert(f.x == 1.)
        assert(f.y == 1.)

    def test_to_pos(self):
        t = self.mv.to_pos
        assert(t.x == 0.)
        assert(t.y == 0.)

    def test_to_pos_set(self):
        self.mv.to = Node(Coordinate(1., 1.))
        t = self.mv.to
        assert(t.x == 1.)
        assert(t.y == 1.)

    def test_calculate_position(self):
        self.mv.from_pos = Node(Coordinate(0., 0.))
        self.mv.to_pos = Node(Coordinate(1., 1.))
        self.mv.trans_pos = 0.
        self.mv.calculate_position()
        assert(self.mv.x == 0.)
        assert(self.mv.y == 0.)
        self.mv.trans_pos = 0.5
        self.mv.calculate_position()
        assert(self.mv.x == 0.5)
        assert(self.mv.y == 0.5)
        self.mv.trans_pos = 1.0
        self.mv.calculate_position()
        assert(self.mv.x == 1.)
        assert(self.mv.y == 1.)

moving_sprite_tests = unittest.makeSuite(MovingSpriteTestCase, "test")
