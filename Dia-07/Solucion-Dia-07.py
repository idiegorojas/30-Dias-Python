from datetime import datetime

# Solicitar al usuario su fecha de nacimiento
dia_nacimiento = int(input("Ingrese el día de su nacimiento: "))
mes_nacimiento = int(input("Ingrese el mes de su nacimiento: "))
anio_nacimiento = int(input("Ingrese el año de su nacimiento: "))

# Solicitar al usuario la fecha actual
dia_actual = int(input("Ingrese el día actual: "))
mes_actual = int(input("Ingrese el mes actual: "))
anio_actual = int(input("Ingrese el año actual: "))

# Crear objetos de fecha
fecha_nacimiento = datetime(anio_nacimiento, mes_nacimiento, dia_nacimiento)
fecha_actual = datetime(anio_actual, mes_actual, dia_actual)

# Calcular la diferencia en días
diferencia_dias = (fecha_actual - fecha_nacimiento).days

# Mostrar la edad en días
print(f"Su edad en días es: {diferencia_dias} días.")