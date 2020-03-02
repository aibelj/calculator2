import unittest

from RandomNumGen.ItemReturnType import ItemReturnType
from RandomNumGen.RandomList import RandomList
from RandomNumGen.RandomNumber import RandomNumber

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.test = [0, 1, 2, 3, 4]

    def test_random_number(self):
        result = RandomNumber.random_number(0, 10)
        self.assertEqual(int, type(result))

    def test_random_number_seed(self):
        result1 = RandomNumber.random_number_seed(0, 10, 5)
        result2 = RandomNumber.random_number_seed(0, 10, 5)
        self.assertEqual(True, result1 == result2)

    def test_random_list(self):
        result1 = RandomList.random_list(0, 10, 5, 5)
        result2 = RandomList.random_list(0, 10, 5,5,)
        self.assertEqual(True, result1 == result2)

    def test_random_num(self):
        result = ItemReturnType.random_num(self.test)
        trueFalse = False
        if result in self.test and type(result) == int:
            trueFalse = True
        self.assertEqual(True, trueFalse)

    def test_random_num_seed(self):
        result1 = ItemReturnType.random_num_seed(self.test, 5)
        result2 = ItemReturnType.random_num_seed(self.test, 5)
        trueFalse = False
        if result1 in self.test and type(result1) == int and result1 == result2:
            trueFalse = True
        self.assertEqual(True, trueFalse)

    def test_aList(self):
        returnLst = ItemReturnType.aList(self.test, 2)
        trueFalse = False
        if len(returnLst) == 2:
            for num in returnLst:
                if num in self.test and type(num) == int:
                    trueFalse = True
                else:
                    trueFalse = False
        self.assertEqual(True, trueFalse)

    def test_aList_seed(self):
        returnLst = ItemReturnType.aList_seed(self.test, 2, 5)
        trueFalse = False
        if len(returnLst) == 2:
            for num in returnLst:
                if type(num) == int and num in self.test:
                    trueFalse = True
                else:
                    trueFalse = False
        self.assertEqual(True, trueFalse)
