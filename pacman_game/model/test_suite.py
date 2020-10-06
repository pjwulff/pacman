import unittest
from .angle_test import angle_tests
from .arena_test import arena_tests
from .avatar_test import avatar_tests
from .blinky_test import blinky_tests
from .circle_test import circle_tests
from .clyde_test import clyde_tests
from .coordinate_test import coordinate_tests
from .dot_test import dot_tests
from .ghost_test import ghost_tests
from .inky_test import inky_tests
from .moving_sprite_test import moving_sprite_tests
from .node_test import node_tests
from .pinky_test import pinky_tests
from .power_test import power_tests

tests = unittest.TestSuite((
    angle_tests,
    arena_tests,
    avatar_tests,
    blinky_tests,
    circle_tests,
    clyde_tests,
    coordinate_tests,
    dot_tests,
    ghost_tests,
    inky_tests,
    moving_sprite_tests,
    node_tests,
    pinky_tests,
    power_tests,
))
