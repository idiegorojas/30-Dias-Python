def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Solicitar al usuario que elija el tipo de conversión
print("Elija el tipo de conversión:")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")
opcion = input("Ingrese 1 o 2: ")

# Realizar la conversión correspondiente
if opcion == "1":
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit.")
elif opcion == "2":
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    celsius = fahrenheit_a_celsius(fahrenheit)
    print(f"{fahrenheit} grados Fahrenheit son {celsius:.2f} grados Celsius.")
else:
    print("Opción no válida. Por favor, ingrese 1 o 2.")