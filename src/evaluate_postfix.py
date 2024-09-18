import math

def evaluate_postfix(expression):
    stack = []

    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        elif token == 'sqrt':
            val = stack.pop()
            stack.append(math.sqrt(val))
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