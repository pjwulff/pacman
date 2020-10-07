#!/usr/bin/env python
import unittest
from test.test_suite import all_tests

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(all_tests)
