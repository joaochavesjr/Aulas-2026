import unittest

from calculator import Calculator


class TestSubtract(unittest.TestCase):
    def test_subtract_positive(self):
        self.assertEqual(Calculator.subtract(5, 3), 2)

    def test_subtract_negative(self):
        self.assertEqual(Calculator.subtract(-5, -3), -2)

    def test_subtract_zero(self):
        self.assertEqual(Calculator.subtract(5, 0), 5)


if __name__ == "__main__":
    unittest.main()
