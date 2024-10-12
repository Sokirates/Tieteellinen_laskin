import unittest
from variable_manager import define_variable

variables = {}

class TestDefineVariable(unittest.TestCase):
    def setUp(self):
        # Tyhjennetään muuttujat jokaisen testin alussa
        global variables
        variables.clear()  # Käytä clear() metodia tyhjentämiseen

    def test_define_variable_invalid_name(self):
        # Testaa virheelliset muuttujan nimet
        with self.assertRaises(ValueError):
            define_variable("xy", 5)  # Nimen tulee olla yksi kirjain

        with self.assertRaises(ValueError):
            define_variable("1", 5)  # Nimen tulee olla kirjain

        with self.assertRaises(ValueError):
            define_variable("", 5)  # Nimen tulee olla vähintään yksi kirjain

if __name__ == "__main__":
    unittest.main()
