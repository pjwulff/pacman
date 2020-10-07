import unittest
from .config_test import config_tests
from .ghost_controller_test import ghost_controller_tests
from .moving_sprite_controller_test import moving_sprite_controller_tests

tests = unittest.TestSuite((
    config_tests,
    ghost_controller_tests,
    moving_sprite_controller_tests,
))
