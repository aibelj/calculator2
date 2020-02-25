import unittest

from Calculator.Calculator import Calculator
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Logarithm import logarithm
from Calculator.SquareRoot import squarerooting


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

    def test_addition(self):
        self.assertEqual(3, addition(1,2))

    def test_subtraction(self):
        self.assertEqual(10, subtraction(25,15))

    def test_multiplication(self):
        self.assertEqual(36,multiplication(2,3))

    def test_division(self):
        self.assertEqual(2, division(4,2))

       def test_logarithm(self):
        self.assertEqual(3, logarithm(729, 9))

    def test_squareRoot(self):
        self.assertEqual(5, squareroot(25))

if __name__ == '__main__':
    unittest.main()

