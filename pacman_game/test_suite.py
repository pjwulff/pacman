import unittest
from .model.test_suite import tests as model_tests

all_tests = unittest.TestSuite((model_tests))
