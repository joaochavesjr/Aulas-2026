import unittest

from calculator import Calculator


class TestMultiply(unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(Calculator.multiply(3, 4), 12)

    def test_multiply_negative(self):
        self.assertEqual(Calculator.multiply(-3, 4), -12)

    def test_multiply_zero(self):
        self.assertEqual(Calculator.multiply(0, 10), 0)


if __name__ == "__main__":
    unittest.main()
