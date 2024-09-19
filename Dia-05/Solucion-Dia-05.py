# Solicitar al usuario su peso en kilogramos
peso = float(input("Ingrese su peso en kilogramos: "))

# Solicitar al usuario su altura en metros
altura = float(input("Ingrese su altura en metros: "))

# Calcular el IMC
imc = peso / (altura ** 2)

# Determinar la categoría del IMC
if imc < 18.5:
    categoria = "Bajo peso"
elif 18.5 <= imc < 24.9:
    categoria = "Normal"
elif 25 <= imc < 29.9:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

# Mostrar el IMC y la categoría correspondiente
print(f"Su IMC es: {imc:.2f}")
print(f"Categoría: {categoria}")