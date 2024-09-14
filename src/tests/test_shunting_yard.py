import unittest
from shunting_yard import shunting_yard_algorithm

class TestShuntingYardAlgorithm(unittest.TestCase):

    def test_simple_addition(self):
        equation = "3 + 4"
        result = shunting_yard_algorithm(equation)
        expected = ['3', '4', '+']
        self.assertEqual(result, expected)

    def test_with_parentheses(self):
        equation = "( 1 + 2 ) * 3"
        result = shunting_yard_algorithm(equation)
        expected = ['1', '2', '+', '3', '*']
        self.assertEqual(result, expected)

    def test_subtraction_and_division(self):
        equation = "10 - 2 / 5"
        result = shunting_yard_algorithm(equation)
        expected = ['10', '2', '5', '/', '-']
        self.assertEqual(result, expected)

    def test_exponentiation(self):
        equation = "2 ^ 3 ^ 2"
        result = shunting_yard_algorithm(equation)
        expected = ['2', '3', '^', '2', '^']
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
