import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(1, -2), -1)

    # Add the following test methods to the TestCalculator class:

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-2, 2), -4)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)

    def test_multiply_negative_positive(self):
        self.assertEqual(self.calc.multiply(-2, 2), -4)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-2, -2), 4)

    def test_multiply_left_zero(self):
        self.assertEqual(self.calc.multiply(0, 2), 0)

    def test_multiply_right_zero(self):
        self.assertEqual(self.calc.multiply(2, 0), 0)

    def test_multiply_left_zero_negative(self):
        self.assertEqual(self.calc.multiply(0, -2), 0)

    def test_multiply_right_zero_negative(self):
        self.assertEqual(self.calc.multiply(-2, 0), 0)

    def test_divide_1(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_divide_2(self):
        self.assertEqual(self.calc.divide(0, 3), 0)

    def test_divide_3(self):
        self.assertEqual(self.calc.divide(-6, 3), -2)

    def test_divide_4(self):
        self.assertEqual(self.calc.divide(6, -3), -2)

    def test_divide_5(self):
        self.assertEqual(self.calc.divide(-6, -3), 2)

    def test_modulo_1(self):
        self.assertEqual(self.calc.modulo(2, 1), 0)

    def test_modulo_2(self):
        self.assertEqual(self.calc.modulo(-2, -1), 0)

if __name__ == '__main__':
    unittest.main()