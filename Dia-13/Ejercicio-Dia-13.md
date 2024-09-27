# Ejercicio: 

Juego de Adivinanza de Números

## Descripción: 

* Crea un juego en el que el programa elija un número aleatorio entre 1 y 100, y el usuario tenga que adivinarlo. 
* El programa debe dar pistas al usuario indicando si el número es mayor o menor que el número ingresado. 
* El juego termina cuando el usuario adivina el número o decide rendirse.

## Instrucciones:

* Genera un número aleatorio entre 1 y 100.
* Pide al usuario que adivine el número.
* Indica al usuario si el número es mayor o menor que su conjetura.
* Permite al usuario rendirse en cualquier momento.
* Muestra el número de intentos realizados al final del juego.

# Pseudocódigo:

* Importar el módulo random.
* Generar un número aleatorio entre 1 y 100.
* Inicializar el contador de intentos.
* Crear un bucle que continúe hasta que el usuario adivine el número o se rinda.
* Dentro del bucle:
    * Pedir al usuario que ingrese un número o que se rinda.
    * Incrementar el contador de intentos.
    * Comparar el número ingresado con el número generado.
    * Dar pistas al usuario.
* Mostrar el número de intentos realizados al final del juego.