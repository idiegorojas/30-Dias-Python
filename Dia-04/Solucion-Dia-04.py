import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 10)

print("¡Bienvenido al juego de adivinar el número!")
print("He generado un número entre 1 y 100. Intenta adivinarlo.")

# Inicializar la variable de adivinanza del usuario
adivinanza = None

# Continuar solicitando adivinanzas hasta que el usuario adivine correctamente
while adivinanza != numero_secreto:
    # Solicitar al usuario que ingrese un número
    adivinanza = int(input("Ingrese su adivinanza: "))
    
    # Comparar el número ingresado con el número generado
    if adivinanza < numero_secreto:
        print("Demasiado bajo. Intenta nuevamente.")
    elif adivinanza > numero_secreto:
        print("Demasiado alto. Intenta nuevamente.")
    else:
        print("¡Felicidades! Adivinaste el número correctamente.")

print("Gracias por jugar.")