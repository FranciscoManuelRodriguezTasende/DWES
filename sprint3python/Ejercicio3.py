cuenta = {"nombre": "Fran", "saldo": 1200.0}

while True:
    print("\n MENÚ DEL CAJERO ")
    print("1️ Consultar saldo")
    print("2️ Ingresar dinero")
    print("3️ Retirar dinero")
    print("4️ Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        print(f"Usuario: {cuenta['nombre']}")
        print(f"Saldo actual: {cuenta['saldo']:.2f} €")

    elif opcion == "2":
        try:
            cantidad = float(input("Introduce la cantidad a ingresar: "))
            if cantidad > 0:
                cuenta["saldo"] += cantidad
                print(f"Has ingresado {cantidad:.2f} €. Nuevo saldo: {cuenta['saldo']:.2f} €")
            else:
                print("La cantidad debe ser positiva.")
        except ValueError:
            print("Entrada no válida. Debes escribir un número.")

    elif opcion == "3":
        try:
            cantidad = float(input("Introduce la cantidad a retirar: "))
            if cantidad <= 0:
                print("La cantidad debe ser positiva.")
            elif cantidad > cuenta["saldo"]:
                print("Saldo insuficiente.")
            else:
                cuenta["saldo"] -= cantidad
                print(f"Has retirado {cantidad:.2f} €. Saldo restante: {cuenta['saldo']:.2f} €")
        except ValueError:
            print("Entrada no válida. Debes escribir un número.")

    elif opcion == "4":
        print("Gracias por usar el cajero. ¡Hasta pronto!")
        break

    else:
        print("Opción no válida. Elige un número del 1 al 4.")
