# Solicitar al usuario que ingrese una frase
frase = input("Ingrese una frase: ")

# Dividir la frase en palabras
palabras = frase.split()

# Contar el número de palabras
numero_palabras = len(palabras)

# Mostrar el número de palabras
print(f"La frase ingresada contiene {numero_palabras} palabras.")