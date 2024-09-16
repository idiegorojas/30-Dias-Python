# Solicitamos al usuario el total de la cuenta
total_cuenta = float(input("Ingrese el total de la cuenta: "))

# Solicitamos al usuario el porcentaje de propina
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar: "))

# Calculamos la cantidad de propina
cantidad_propina = total_cuenta * (porcentaje_propina / 100)

# Calculamos el total a pagar
total_pagar = total_cuenta + cantidad_propina

# Mostramos la cantidad de propina y el total a pagar
print(f"La cantidad de propina es: ${cantidad_propina:.2f}")
print(f"El total a pagar es: ${total_pagar:.3f}")