def evaluar_expresion(expresion):
    try:
        resultado = eval(expresion)
        return resultado
    except ZeroDivisionError:
        return "Error: División por cero."
    except Exception as e:
        return f"Error: Expresión mal formada ({e})."

def menu():
    while True:
        print("\nCalculadora de Expresiones Matemáticas")
        print("1. Ingresar expresión")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            expresion = input("Ingrese la expresión matemática: ")
            resultado = evaluar_expresion(expresion)
            print(f"Resultado: {resultado}")
        elif opcion == '2':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()