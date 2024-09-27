import re

def is_number(token):
    """
    Check if the given token is a valid number.

    Parameters:
    token (str)

    Returns:
    valid number if the token is a valid number
    otherwise return None
    """
    return re.match(r"^-?\d+(\.\d+)?$", token)

def shunting_yard_algorithm(equation):
    """
    Convert a mathematical equation into postfix notation
    using the Shunting Yard algorithm.

    Parameters: 
        equation:   A string representation of a mathematical expression in infix notation.
            Supported operators: +, -, *, /, ^, as well as the functions sqrt, sin, cos, and tan.

    Returns:
    list: A list of tokens representing the mathematical expression in postfix notation.
    """
    tokens = re.findall(r'\d+|[+*/^()-]|sqrt|sin|cos|tan', equation)

    if ''.join(tokens) != equation.replace(' ', ''):
        raise ValueError("Syötteessä on virheellisiä merkkejä.")

    open_parens = 0
    for char in equation:
        if char == '(':
            open_parens += 1
        elif char == ')':
            open_parens -= 1
    if open_parens != 0:
        raise ValueError("Sulkeet eivät ole tasapainossa.")

    operators_precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    
    holding_stack = []
    output = []
    
    for token in tokens:
        if is_number(token):
            output.append(token)
        elif token in {"sqrt", "sin", "cos", "tan"}:
            holding_stack.append(token)
        elif token in operators_precedence:
            while (holding_stack and holding_stack[-1] in operators_precedence and
                   operators_precedence[holding_stack[-1]] >= operators_precedence[token]):
                output.append(holding_stack.pop())
            holding_stack.append(token)
        elif token == "(":
            holding_stack.append(token)
        elif token == ")":
            while holding_stack and holding_stack[-1] != "(":
                output.append(holding_stack.pop())
            holding_stack.pop()
            if holding_stack and holding_stack[-1] in {"sqrt", "sin", "cos", "tan"}:
                output.append(holding_stack.pop())

    while holding_stack:
        output.append(holding_stack.pop())

    return output