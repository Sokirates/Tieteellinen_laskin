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

    def test_sqrt_function(self):
        equation = "sqrt(9)"
        result = shunting_yard_algorithm(equation)
        expected = ['9', 'sqrt']
        self.assertEqual(result, expected)

    def test_sin_function(self):
        equation = "sin(0)"
        result = shunting_yard_algorithm(equation)
        expected = ['0', 'sin']
        self.assertEqual(result, expected)

    def test_cos_function(self):
        equation = "cos(0)"
        result = shunting_yard_algorithm(equation)
        expected = ['0', 'cos']
        self.assertEqual(result, expected)

    def test_tan_function(self):
        equation = "tan(0)"
        result = shunting_yard_algorithm(equation)
        expected = ['0', 'tan']
        self.assertEqual(result, expected)

    def test_invalid_characters(self):
        equation = "1 + 2 w 3" 
        with self.assertRaises(ValueError) as context:
            shunting_yard_algorithm(equation)
        self.assertEqual(str(context.exception), "Syötteessä on virheellisiä merkkejä.")

    def test_unbalanced_parentheses_open(self):
        equation = "(1 + 2"  
        with self.assertRaises(ValueError) as context:
            shunting_yard_algorithm(equation)
        self.assertEqual(str(context.exception), "Sulkeet eivät ole tasapainossa.")

    def test_unbalanced_parentheses_open(self):
        equation = "1 + 2)"  
        with self.assertRaises(ValueError) as context:
            shunting_yard_algorithm(equation)
        self.assertEqual(str(context.exception), "Sulkeet eivät ole tasapainossa.")

if __name__ == '__main__': # pragma: no cover
    unittest.main()
