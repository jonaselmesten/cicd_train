import calculator
import unittest


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(4, calculator.add(2, 2))

    def test_sub(self):
        self.assertEqual(2, calculator.subtract(4, 2))

    def test_string_add(self):
        self.assertEqual(type(calculator.add_and_return_string(1, 2)), str)
