import re

equation = input("Kirjoita yhtälö: ")

tokens = re.findall(r'\d+|[+*/^()-]', equation)
print(f"tokens: {tokens}")

operators_precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

holding_stack = []
output = []

def is_number(token):
    return re.match(r"^-?\d+(\.\d+)?$", token)

for token in tokens:
    if is_number(token):
        output.append(token)
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

while holding_stack:
    output.append(holding_stack.pop())

print(f"holding_stack: {holding_stack}")
print(f"output: {output}") 


