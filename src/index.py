from shunting_yard import shunting_yard_algorithm
from evaluate_postfix import evaluate_postfix
from variable_manager import define_variable, get_variable, list_variables

while True:  # pragma: no cover
    var = input("Haluatko määritellä muuttujan? (y/n): ").strip().lower()

    if var == "y":
        while True:
            variable = input("Syötä muuttujan nimi (yksi kirjain): ").strip()
            if len(variable) != 1 or not variable.isalpha():
                print("Virhe: Muuttujan nimen tulee olla vain yksi kirjain.")
                continue  
        
            while True:
                try:
                    variable_value = float(input(f"Syötä muuttujan '{variable}' arvo (numero): ").strip())
                    define_variable(variable, variable_value)
                    print('Muuttuja ja sen arvo on tallennettu.')  
                    break  
                except ValueError:
                    print("Virhe: Anna kelvollinen numero muuttujan arvoksi.")  

            break  

    elif var == "n":
        break  

    else:
        print("Virhe: Anna 'y' tai 'n'.") 

while True:  # pragma: no cover
    equation = input("Kirjoita yhtälö ('exit' lopettaa): ")
    if equation.lower() == "exit":
        print("Ohjelma lopetetaan.")
        break

    try:
        output = shunting_yard_algorithm(equation)
        
        contains_variables = any(token.isalpha() and token in list_variables() for token in output)
        
        if not contains_variables:
            print(f"Postfix-muoto: {output}")
        else:
            new_output = []
            for token in output:
                if token.isalpha() and len(token) == 1:
                    if token in list_variables():
                        new_output.append(str(get_variable(token)))
                    else:
                        raise ValueError(f"Muuttujaa '{token}' ei ole määritelty.")
                else:
                    new_output.append(token)
            print(f"Postfix-muoto: {output}")
            print(f"Postfix-muoto muuttujien arvoilla: {new_output}")
            output = new_output  

        result = evaluate_postfix(output)
        print(f"Tulos: {result}")

        save_result = input("Haluatko tallentaa tuloksen muuttujaan? (y/n): ").strip().lower()
        if save_result == "y":
            while True:
                result_variable = input("Syötä muuttujan nimi (yksi kirjain): ").strip()
                try:
                    define_variable(result_variable, result)
                    break
                except ValueError as ve:
                    print(ve)

    except ValueError as ve:
        print(f"Syötteessä virhe: {ve}")
    except Exception as e:
        print(f"Virhe: {e}")

