import unittest

from Calculator import calculate_result


class MyTestCase(unittest.TestCase):
    def test_calculate_result_addition(self):
        self.assertEqual(8, calculate_result("+", 3, 5))

    def test_calculate_result_subtraction(self):
        self.assertEqual(12, calculate_result("-", 15, 3))

    def test_calculate_result_multiplication(self):
        self.assertEqual(25, calculate_result("*", 5, 5))

    def test_calculate_result_division(self):
        self.assertEqual(7, calculate_result("/", 49, 7))


if __name__ == '__main__':
    unittest.main()
