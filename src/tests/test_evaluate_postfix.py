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

    def test_sqrt(self):
        expression = ['9', 'sqrt']
        result = evaluate_postfix(expression)
        expected = 3
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

    def test_no_values_for_sqrt(self):
        expression = ['sqrt']
        with self.assertRaises(ValueError) as context:
            evaluate_postfix(expression)
        self.assertEqual(str(context.exception), "Virhe: Yritettiin poistaa arvo tyhjältä pinolta.")


    def test_no_values_for_sin(self):
        expression = ['sin']
        with self.assertRaises(ValueError) as context:
            evaluate_postfix(expression)
        self.assertEqual(str(context.exception), "Virhe: Yritettiin poistaa arvo tyhjältä pinolta.")

    def test_too_few_values_for_cos(self):
        expression = ['cos']  
        with self.assertRaises(ValueError) as context:
            evaluate_postfix(expression)
        self.assertEqual(str(context.exception), "Virhe: Yritettiin poistaa arvo tyhjältä pinolta.")

    def test_too_few_values_for_tan(self):
        expression = ['tan']  
        with self.assertRaises(ValueError) as context:
            evaluate_postfix(expression)
        self.assertEqual(str(context.exception), "Virhe: Yritettiin poistaa arvo tyhjältä pinolta.")

    def test_no_values(self):
        expression = []  
        with self.assertRaises(ValueError) as context:
            evaluate_postfix(expression)
        self.assertEqual(str(context.exception), "Virhe: Tyhjentämättömiä arvoja pinossa.")

    def test_empty_stack_pop(self):
        with self.assertRaises(ValueError) as context:
            evaluate_postfix(['+', '3'])
        self.assertEqual(str(context.exception), "Virhe: Yritettiin poistaa arvoja tyhjältä pinolta.")

if __name__ == '__main__': # pragma: no cover
    unittest.main()
