import math

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
        if token.isdigit():
            stack.append(int(token))
        elif token == 'sqrt':
            if not stack:
                raise ValueError("Virhe: Yritettiin poistaa arvo tyhjältä pinolta.")
            val = stack.pop()
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
                stack.append(val1 / val2)
            elif token == '^':
                stack.append(val1 ** val2)

    if len(stack) != 1:
        raise ValueError("Virhe: Tyhjentämättömiä arvoja pinossa.")

    return stack[0]
