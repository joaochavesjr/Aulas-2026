import unittest

from calculator import Calculator


class TestDivide(unittest.TestCase):
    def test_divide_positive(self):
        self.assertEqual(Calculator.divide(10, 2), 5)

    def test_divide_negative(self):
        self.assertEqual(Calculator.divide(-10, 2), -5)

    def test_divide_zero_numerator(self):
        self.assertEqual(Calculator.divide(0, 5), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Calculator.divide(5, 0)


if __name__ == "__main__":
    unittest.main()
