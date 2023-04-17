import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(1, 2), 3)


if __name__ == "__main__":
    unittest.main()
