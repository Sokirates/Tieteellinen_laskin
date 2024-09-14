from shunting_yard import shunting_yard_algorithm
from evaluate_postfix import evaluate_postfix

equation = input("Kirjoita yhtälö: ")
output = shunting_yard_algorithm(equation)

print(f"output: {output}")

result = evaluate_postfix(output)

print(f"result: {result}")