import re

def is_number(token):
    return re.match(r"^-?\d+(\.\d+)?$", token)

def shunting_yard_algorithm(equation):
    tokens = re.findall(r'\d+|[+*/^()-]|sqrt|sin|cos|tan', equation)

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