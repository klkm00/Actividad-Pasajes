import json
precio_normal = 78900
precio_vip = 240000
descuento = 0.85

asientos = [[None for _ in range(6)] for _ in range(7)]
pasajeros ={}

def mostrar_asientos():
    print("ASIENTOS DISPONIBLES")
    for row in range(7):
        if row == 5:
            print("_________________________")
            print("_________________________")
        for col in range(6):
            numero_asiento = row * 6 + col + 1
            asiento_disponible = 'X' if asientos[row][col] else numero_asiento
            print(f"{asiento_disponible:>3}", end=" ")
        print()

def comprar_asiento():
    print("COMPRAR ASIENTOS")
    print(" ⤷ Para comprar un asiento primero debe registrar los siguientes datos del pasajero: ")
    nombre = input("Nombre: ")
    while True:
            rut = input("RUT \n ⤷ sin puntos, con guión: ")
            if rut.__contains__("-"):
             break
            else:
                print("Debe ingresar el RUT sin puntos y con guión")
    while True:
        telefono = input("Teléfono:")
        if len(telefono) == 9:
            break
        else:
            print("Debe ingresar un numero de teléfono válido, una serie de 9 números") 
    banco = input("Banco:")

    print("⟶ ESCOGER ASIENTO")
    mostrar_asientos()
    numero_asiento = int(input("Asiento seleccionado: "))

    row, col = divmod(numero_asiento - 1, 6)
    if asientos[row][col] is None:
        precio = precio_vip if numero_asiento > 30 else precio_normal
        if banco.lower() == "bancoduoc":
            precio = precio*descuento
        print(f"El valor del asiento seleccionado es: ${precio}")
        while True:
            try:
                confirmar = input("¿Desea confirmar la compra? (si/no): ")
                if confirmar.lower() == "si":
                    asientos[row][col] = rut
                    pasajeros[rut] = {
                        "nombre": nombre,
                        "telefono": telefono,
                        "banco": banco
                    }
                    print("Compra realizada con éxito.")
                    break
                else:
                    if confirmar.lower() == "no":
                        print("Se ha cancelado la compra")
                        return
            except ValueError:
                print("Ingrese una opcion valida")
    else:
        print("El asiento no está disponible.")

def cancelar_asiento():
    print("ANULAR PASAJE")
    rut = input("Ingrese RUT del pasajero para anular el vuelo: ")
    if rut in pasajeros:
        for row in range(7):
            for col in range(6):
                if asientos[row][col] == rut:
                    asientos[row][col] = None
                    del pasajeros[rut]
                    print("La compra ha sido anulada y el asiento está disponible nuevamente.")
                    return
    else:
        print("No se encontró un pasajero con ese RUT.")

def modificar_datos_cliente():
    print("MODIFICAR DATOS")
    rut = input("Ingrese RUT del pasajero: ")
    if rut in pasajeros:
        print(f"Datos actuales: {pasajeros[rut]}")
        print("1. Modificar nombre")
        print("2. Modificar teléfono")
        opcion = int(input("Seleccione la opción a modificar: "))
        if opcion == 1:
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            pasajeros[rut]["nombre"] = nuevo_nombre
        elif opcion == 2:
            nuevo_telefono = input("Ingrese el nuevo teléfono: ")
            pasajeros[rut]["telefono"] = nuevo_telefono
        print("Datos actualizados.")
    else:
        print("No se encontró un pasajero con ese RUT.")

def menu():
    while True:
        print("VUELOS-DUOC")
        print("1. Ver asientos disponibles")
        print("2. Comprar asiento")
        print("3. Anular pasaje")
        print("4. Modificar datos de pasajero")
        print("5. Salir")
        try:
            opcion = int(input("Ir a: "))
        except ValueError:
            print("Opcion no válida. Debe ingresar una opcion valida entre 1 y 5.")

        if opcion == 1:
            mostrar_asientos()
        elif opcion == 2:
            comprar_asiento()
        elif opcion == 3:
            cancelar_asiento()
        elif opcion == 4:
            modificar_datos_cliente()
        elif opcion == 5:
            print("Gracias por usar el sistema de venta de pasajes. ¡Hasta luego!")
            break
        else:
            print("Opcion no válida. Debe ingresar una opcion valida de 1 y 5.")

menu()

with open('Pasajes.json','w') as archivo:
    json.dump(pasajeros, archivo)