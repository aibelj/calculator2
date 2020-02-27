import unittest

from RandomNumGen.ItemReturnType import
from RandomNumGen import RandomList
from RandomNumGen import RandomNumber

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.test = [0, 1, 2, 3, 4]

    def test_RandomNumber(self):