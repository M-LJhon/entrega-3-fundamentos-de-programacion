# Jhonalex Mejia Lopez.
# Ingenieria de sistemas.
# Codigo fuente: Autoria propia.

precios_pizzas = [10000, 15000, 20000, 25000, 35000]
porciones_pizzas = [2, 4, 6, 8, 12]
seleccion_cliente_precio = []
total_pagar_x_pedido = []
porciones_x_pedido = []
total_porciones = 0
total_valor_ventas = 0
pizza_pequena = 0
pizza_mediana = 0
pizza_larga = 0
pizza_familiar = 0
pizza_extra_familiar = 0

while True:
    while True:
        cliente_nuevo = input("Deseas registrar una venta? \n" \
                              "(si)(no): ").lower()
        if cliente_nuevo == "no":
            print("Cerrando el programa...\n" \
                f"")
            break
        elif cliente_nuevo == "si":
            break
        elif cliente_nuevo != "si":
            print("Responde: (si)(no)... Vuelve a intentarlo.")

    if cliente_nuevo == "no":
        break
        

    while True:
        try:
            seleccion = int(input("*** Tipos de pizza ***\n" \
                                "- (1) Pequena con 2 porciones: $10.000\n" \
                                "- (2) Mediana con 4 porciones: $15.000\n" \
                                "- (3) Larga con 6 porciones: $20.000\n" \
                                "- (4) Familiar con 8 prociones: $25.000\n" \
                                "- (5) Extra Familiar con 12 porciones: $35.000\n" \
                                "Escribe el numero de la opcion que desee el cliente:"))
        except ValueError:
            print("en este campo solo puedes digitar valores numericos...")
            continue

        if seleccion == 1:
            pizza_pequena += 1
            seleccion_cliente_precio.append([precios_pizzas[0], porciones_pizzas[0]])
        elif seleccion == 2:
            pizza_mediana += 1
            seleccion_cliente_precio.append([precios_pizzas[1], porciones_pizzas[1]])
        elif seleccion == 3:
            pizza_larga += 1
            seleccion_cliente_precio.append([precios_pizzas[2], porciones_pizzas[2]])
        elif seleccion == 4:
            pizza_familiar += 1
            seleccion_cliente_precio.append([precios_pizzas[3], porciones_pizzas[3]])
        elif seleccion == 5:
            pizza_extra_familiar += 1
            seleccion_cliente_precio.append([precios_pizzas[4], porciones_pizzas[4]])
        else:
            print("Ingresa una opcion valida..")
            continue

        while True:
            agreagar_pizza = input("Desea agregar otra pizza a la orden?\n" \
                                   "(si)(no): ").lower()
            if agreagar_pizza == "no" or agreagar_pizza == "si":
                break

            print("Responde: (si)(no)... Intenta de nuevo :)")

        if agreagar_pizza == "no":
            
            for item in seleccion_cliente_precio:
                total_pagar_x_pedido.append(item[0])
                porciones_x_pedido.append(item[1])

            seleccion_cliente_precio = []

            total_porciones += sum(porciones_x_pedido)
            total_valor_ventas += sum(total_pagar_x_pedido)

            print(
            f"Total de prociones del pedido: {sum(porciones_x_pedido)}\n"\
            f"Total del pedido: ${sum(total_pagar_x_pedido)}"
            )

            porciones_x_pedido = []
            total_pagar_x_pedido = []

            print("------------------------------------")
            break

print("*** Cantidad de pizzas vendidas por tipo ***\n"\
      f"- Pizza pequena: {pizza_pequena}\n"\
      f"- Pizza mediana: {pizza_mediana}\n"\
      f"- Pizza larga: {pizza_larga}\n"\
      f"- Pizza familiar: {pizza_familiar}\n"\
      f"- Pizza extra familiar: {pizza_extra_familiar}\n")
print(f"** Total de porciones vendidas: {total_porciones}\n"\
      f"*** Valor total de las ventas: ${total_valor_ventas}")
