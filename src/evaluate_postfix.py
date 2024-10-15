import math
import re

def is_number(token):
    """Check if the token is a valid number (integer or float)."""
    return re.match(r"^-?\d+(\.\d+)?$", token)

def evaluate_postfix(expression):
    """
    Evaluates a mathematical expression in postfix notation.

    This function processes a list of tokens that form a valid postfix expression. 
    It supports basic arithmetic operations (`+`, `-`, `*`, `/`, `^`), as well as 
    several mathematical functions (`sqrt`, `sin`, `cos`, `tan`).

    Args:
        expression (list of str): The postfix expression as a list of tokens

    Returns:
        float: The result of the evaluated expression
    """
    stack = []

    for token in expression:
        if is_number(token):
            stack.append(float(token))
        elif token == 'sqrt':
            if not stack:
                raise ValueError("Virhe: Yritettiin poistaa arvo tyhjältä pinolta.")
            val = stack.pop()
            if val < 0:
                raise ValueError("Virhe: Neliöjuuri ei voi olla negatiivinen.")
            stack.append(math.sqrt(val))
        elif token == 'sin':
            if not stack:
                raise ValueError("Virhe: Yritettiin poistaa arvo tyhjältä pinolta.")
            val = stack.pop()
            stack.append(math.sin(val))
        elif token == 'cos':
            if not stack:
                raise ValueError("Virhe: Yritettiin poistaa arvo tyhjältä pinolta.")
            val = stack.pop()
            stack.append(math.cos(val))
        elif token == 'tan':
            if not stack:
                raise ValueError("Virhe: Yritettiin poistaa arvo tyhjältä pinolta.")
            val = stack.pop()
            stack.append(math.tan(val)) 
        else:
            if token in ('+', '-', '*', '/', '^'):
                if len(stack) < 2:
                    raise ValueError("Virhe: Yritettiin poistaa arvoja tyhjältä pinolta.")
                val2 = stack.pop()
                val1 = stack.pop()

                if token == '+':
                    stack.append(val1 + val2)
                elif token == '-':
                    stack.append(val1 - val2)
                elif token == '*':
                    stack.append(val1 * val2)
                elif token == '/':
                    if val2 == 0:
                        raise ValueError("Virhe: Nollalla jakaminen.")
                    stack.append(val1 / val2)
                elif token == '^':
                    stack.append(val1 ** val2)
            else:
                raise ValueError(f"Muuttujaa '{token}' ei ole määritelty.")

    if len(stack) != 1:
        raise ValueError("Virhe: Tyhjentämättömiä arvoja pinossa.")

    return stack[0]
