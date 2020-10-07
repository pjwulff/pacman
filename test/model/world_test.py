import unittest
from pacman_game.model import world

class WorldTestCase(unittest.TestCase):
    def setUp(self):
        self.w = world.World("small", "square")

    def test_lives(self):
        assert(self.w.lives == 3)

    def test_lives_set(self):
        self.w.lives = 1
        assert(self.w.lives == 1)

    def test_score(self):
        assert(self.w.score == 0)

    def test_score_set(self):
        self.w.score = 1
        assert(self.w.score == 1)

    def test_level(self):
        assert(self.w.level == 1)

    def test_level_set(self):
        self.w.level = 2
        assert(self.w.level == 2)

world_tests = unittest.makeSuite(WorldTestCase, "test")
