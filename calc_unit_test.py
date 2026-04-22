import unittest
from mycalculator import MathOperations as calc

class TestCalculatorOperations(unittest.TestCase):
    def setUp(self):
        self.calc = calc() 

    def test_addition(self):
        self.assertEqual(self.calc.addition([2, 3]), 5 )

    def test_subtraction(self):
        self.assertEqual(self.calc.subtraction([5, 2]), 3)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiplication([4, 3]), 12)

    def test_division(self):
        self.assertEqual(self.calc.division([10, 2]), 5)
        self.assertRaises(ZeroDivisionError, self.calc.division, [10, 0])

    def test_exponents(self):
        self.assertEqual(self.calc.exponents([2, 3]), 8)

    def test_square_value(self):
        self.assertEqual(self.calc.square_value([4]), 16)

    def test_square_root(self):
        self.assertEqual(self.calc.square_root([16]), 4)
        self.assertRaises(ValueError, self.calc.square_root, [-1])

if __name__ == '__main__':
    unittest.main()