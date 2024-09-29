tasas_de_cambio = {
    'USD': {'EUR': 0.85, 'JPY': 110.0, 'GBP': 0.75},
    'EUR': {'USD': 1.18, 'JPY': 129.53, 'GBP': 0.88},
    'JPY': {'USD': 0.0091, 'EUR': 0.0077, 'GBP': 0.0068},
    'GBP': {'USD': 1.33, 'EUR': 1.14, 'JPY': 147.0}
}

def convertir_moneda(cantidad, moneda_origen, moneda_destino):
    if moneda_origen == moneda_destino:
        return cantidad
    else:
        tasa = tasas_de_cambio[moneda_origen][moneda_destino]
        return cantidad * tasa


def menu():
    while True:
        print("\nConversor de Monedas")
        print("1. Convertir moneda")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            moneda_origen = input("Ingrese la moneda de origen (USD, EUR, JPY, GBP): ").upper()
            moneda_destino = input("Ingrese la moneda de destino (USD, EUR, JPY, GBP): ").upper()
            cantidad = float(input("Ingrese la cantidad a convertir: "))

            resultado = convertir_moneda(cantidad, moneda_origen, moneda_destino)
            if resultado is not None:
                print(f"{cantidad} {moneda_origen} son {resultado:.2f} {moneda_destino}")
            else:
                print("Conversión no disponible para las monedas seleccionadas.")
        elif opcion == '2':
            break
        else:
            print("Opción no válida. Intente de nuevo.")


menu()