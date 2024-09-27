from shunting_yard import shunting_yard_algorithm
from evaluate_postfix import evaluate_postfix

while True:  # pragma: no cover
    equation = input("Kirjoita yhtälö ('exit' lopettaa): ")

    if equation.lower() == "exit":
        print("Ohjelma lopetetaan.")
        break

    try:
        output = shunting_yard_algorithm(equation)
        print(f"Postfix-muoto: {output}")

        result = evaluate_postfix(output)
        print(f"Tulos: {result}")
    except ValueError as ve:
        print(f"Syötteessä virhe: {ve}")
    except Exception as e:
        print(f"Virhe: {e}")
