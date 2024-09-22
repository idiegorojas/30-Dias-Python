# Solicitar al usuario que ingrese una cadena de texto
cadena = input("Ingrese una cadena de texto: ")

# Inicializar el contador de vocales
contador_vocales = 0

# Definir las vocales
vocales = "aeiouAEIOU"

# Recorrer cada carácter de la cadena
for caracter in cadena:
    # Verificar si el carácter es una vocal
    if caracter in vocales:
        contador_vocales += 1

# Mostrar el número total de vocales
print(f"El número total de vocales en la cadena es: {contador_vocales}")