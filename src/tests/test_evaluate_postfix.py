import unittest
from evaluate_postfix import evaluate_postfix  

class TestEvaluatePostfix(unittest.TestCase):

    def test_simple_addition(self):
        expression = ['2', '3', '+']
        result = evaluate_postfix(expression)
        expected = 5
        self.assertEqual(result, expected)

    def test_subtraction(self):
        expression = ['10', '4', '-']
        result = evaluate_postfix(expression)
        expected = 6
        self.assertEqual(result, expected)

    def test_multiplication(self):
        expression = ['2', '3', '*']
        result = evaluate_postfix(expression)
        expected = 6
        self.assertEqual(result, expected)

    def test_division(self):
        expression = ['8', '2', '/']
        result = evaluate_postfix(expression)
        expected = 4
        self.assertEqual(result, expected)

    def test_exponentiation(self):
        expression = ['2', '3', '^']
        result = evaluate_postfix(expression)
        expected = 8
        self.assertEqual(result, expected)

    def test_complex_expression(self):
        expression = ['2', '3', '+', '5', '1', '-', '*']
        result = evaluate_postfix(expression)
        expected = 20
        self.assertEqual(result, expected)

    def test_sin(self):
        expression = ['0', 'sin']
        result = evaluate_postfix(expression)
        expected = 0  
        self.assertEqual(result, expected)

    def test_cos(self):
        expression = ['0', 'cos']
        result = evaluate_postfix(expression)
        expected = 1 
        self.assertEqual(result, expected)

    def test_tan(self):
        expression = ['0', 'tan']
        result = evaluate_postfix(expression)
        expected = 0  
        self.assertEqual(result, expected)

if __name__ == '__main__': # pragma: no cover
    unittest.main()
