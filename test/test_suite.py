import unittest
from .model.test_suite import tests as model_tests
from .controller.test_suite import tests as controller_tests

all_tests = unittest.TestSuite((
    model_tests,
    controller_tests,
))
