# Jhonalex Mejia Lopez.
# Ingenieria de sistemas.
# Codigo fuente: Autoria propia.

cantidad_residentes = int(input("Ingrese la cantidad de" \
"de residentes del conjunto: "))
valor_cuota_mensual = int(input("Ingrese el valor a pagar" \
"como cuota mensual: "))

contador = 0
vecinos_al_dia = 0
vecinos_morosos = 0

while contador < cantidad_residentes:
    estatus = input(f"El vecino # {contador+1} ya realizo el pago?\n" \
    "Escribe: (si)(no): ")

    if estatus.lower() == "si":
        contador += 1
        vecinos_al_dia += 1
    elif estatus.lower() == "no":
        contador += 1
        vecinos_morosos += 1
    else:
        print("Solo puedes escribir si o no. " \
        "Por favor vuelve a intentarlo")

valor_total_adeudado = vecinos_morosos * valor_cuota_mensual

print(f"Cantidad de vecinos al dia: {vecinos_al_dia}")
print(f"Cantidad de vecinos morosos: {vecinos_morosos}")
print(f"Valor total adeudado: {valor_total_adeudado}")