import unittest
from pacman_game.controller import moving_sprite_controller

class MockSprite:
    def return_to_spawn(self):
        pass

    @property
    def direction(self):
        return 0.

class MovingSpriteControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.ms = MockSprite()
        self.msc = moving_sprite_controller.MovingSpriteController(self.ms)

    def test_return_to_spawn(self):
        self.msc.return_to_spawn()
        assert(self.msc.target_direction == None)
        assert(self.msc.speed == 0.)

    def test_target_direction_set(self):
        self.msc.target_direction = 1.
        assert(self.msc.target_direction == 1.)

    def test_sprite(self):
        assert(self.msc.sprite == self.ms)

    def test_speed_set(self):
        self.msc.speed = 1.
        assert(self.msc.speed == 1.)

    def test_speed_scale_set(self):
        self.msc.speed_scale = 1.
        assert(self.msc.speed_scale == 1.)

moving_sprite_controller_tests = \
    unittest.makeSuite(MovingSpriteControllerTestCase, "test")
