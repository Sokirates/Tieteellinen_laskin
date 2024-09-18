import math

def evaluate_postfix(expression):
    stack = []

    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        elif token == 'sqrt':
            val = stack.pop()
            stack.append(math.sqrt(val))
        elif token == 'sin':
            val = stack.pop()
            stack.append(math.sin(val))
        elif token == 'cos':
            val = stack.pop()
            stack.append(math.cos(val))
        elif token == 'tan':
            val = stack.pop()
            stack.append(math.tan(val)) 
        else:
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

    return stack[0]