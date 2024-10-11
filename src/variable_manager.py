variables = {}

def define_variable(name, value):
    """
    Define a variable with a given name and value.
    """
    if len(name) != 1 or not name.isalpha():
        raise ValueError("Muuttujan nimen tulee olla vain yksi kirjain.")
    variables[name] = value
    print(f"Muuttuja '{name}' määritelty arvolla {value}.")

def get_variable(name):
    """
    Retrieve the value of a variable by name.
    """
    return variables.get(name)

def list_variables():
    """
    Return a dictionary of all defined variables.
    """
    return variables
