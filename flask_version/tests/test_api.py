import unittest
from os.path import join, dirname
import sys

import os

sys.path.append(".")
print(os.getcwd())
print(__file__)


class TestApi(unittest.TestCase):
    def test_simple(self):
        s = {"id": 7}
        self.assertEqual("635950_304", s.id)
