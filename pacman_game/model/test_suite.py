import unittest
from .angle_test import angle_tests
from .arena_test import arena_tests
from .avatar_test import avatar_tests

tests = unittest.TestSuite((
    angle_tests,
    arena_tests,
    avatar_tests,
))
