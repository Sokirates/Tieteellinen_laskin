import unittest
from variable_manager import define_variable, variables

class TestVariableManager(unittest.TestCase):

    def setUp(self):
        variables.clear()

    def test_define_variable_success(self):
        define_variable('x', 10)
        self.assertEqual(variables['x'], 10)

    def test_define_variable_float(self):
        define_variable('y', 3.14)
        self.assertEqual(variables['y'], 3.14)

    def test_define_variable_invalid_name(self):
        with self.assertRaises(ValueError) as context:
            define_variable('xy', 10)
        self.assertEqual(str(context.exception), "Muuttujan nimen tulee olla vain yksi kirjain.")
    
    def test_define_variable_invalid_name_not_alpha(self):
        with self.assertRaises(ValueError) as context:
            define_variable('1', 10)
        self.assertEqual(str(context.exception), "Muuttujan nimen tulee olla vain yksi kirjain.")
    
    def test_define_variable_invalid_value(self):
        with self.assertRaises(ValueError) as context:
            define_variable('x', 'abc')
        self.assertEqual(str(context.exception), "Anna kelvollinen numero muuttujan arvoksi.")

if __name__ == '__main__':
    unittest.main()

