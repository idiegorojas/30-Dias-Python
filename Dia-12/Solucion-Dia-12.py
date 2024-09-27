import csv
from collections import defaultdict

def leer_datos_ventas(ruta_archivo):
    ventas = []
    with open(ruta_archivo, mode='r') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            fila['cantidad'] = int(fila['cantidad'])
            fila['precio_unitario'] = float(fila['precio_unitario'])
            ventas.append(fila)
    return ventas

def analizar_ventas(ventas):
    total_ventas = 0
    producto_mas_vendido = defaultdict(int)
    ventas_por_dia = defaultdict(float)

    for venta in ventas:
        total_ventas += venta['cantidad'] * venta['precio_unitario']
        producto_mas_vendido[venta['producto']] += venta['cantidad']
        ventas_por_dia[venta['fecha']] += venta['cantidad'] * venta['precio_unitario']

    producto_mas_vendido = max(producto_mas_vendido, key=producto_mas_vendido.get)
    dia_mayores_ventas = max(ventas_por_dia, key=ventas_por_dia.get)

    resultados = {
        'total_ventas': total_ventas,
        'producto_mas_vendido': producto_mas_vendido,
        'dia_mayores_ventas': dia_mayores_ventas
    }

    return resultados

def menu():
    while True:
        print("\nAnálisis de Datos de Ventas")
        print("1. Cargar archivo CSV")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ruta_archivo = input("Ingrese la ruta del archivo CSV: ")
            ventas = leer_datos_ventas(ruta_archivo)
            resultados = analizar_ventas(ventas)
            print(f"Total de ventas: {resultados['total_ventas']}")
            print(f"Producto más vendido: {resultados['producto_mas_vendido']}")
            print(f"Día con mayores ventas: {resultados['dia_mayores_ventas']}")
        elif opcion == '2':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()