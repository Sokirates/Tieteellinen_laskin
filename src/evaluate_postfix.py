import math

def evaluate_postfix(expression):
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
