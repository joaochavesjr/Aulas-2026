import unittest

from calculator import Calculator


class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(Calculator.add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(Calculator.add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(Calculator.add(0, 5), 5)


if __name__ == "__main__":
    unittest.main()
