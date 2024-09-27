import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivinanza de números!")
    print("He elegido un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    while True:
        entrada = input("Ingresa tu conjetura (o 'rendirse' para terminar): ")

        if entrada.lower() == 'rendirse':
            print(f"Te has rendido. El número era {numero_secreto}.")
            break

        try:
            conjetura = int(entrada)
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        intentos += 1

        if conjetura < numero_secreto:
            print("El número es mayor.")
        elif conjetura > numero_secreto:
            print("El número es menor.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

# Ejecutar el juego
juego_adivinanza()