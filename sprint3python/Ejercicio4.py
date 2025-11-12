lista_compra = []

while True:
    print("\n MENÚ DE LA LISTA DE LA COMPRA ")
    print("1️ Añadir producto")
    print("2️ Eliminar producto")
    print("3️ Ver lista")
    print("4️ Vaciar lista")
    print("5️ Salir")

    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        producto = input("Introduce el nombre del producto: ").strip().lower()
        if producto == "":
            print(" No puedes añadir un nombre vacío.")
        elif producto in lista_compra:
            print(" Ese producto ya está en la lista.")
        else:
            lista_compra.append(producto)
            print(f" '{producto}' añadido correctamente.")

    elif opcion == "2":
        producto = input("Introduce el producto a eliminar: ").strip().lower()
        if producto in lista_compra:
            lista_compra.remove(producto)
            print(f" '{producto}' eliminado correctamente.")
        else:
            print(" El producto no está en la lista.")

    elif opcion == "3":
        if len(lista_compra) == 0:
            print(" La lista está vacía.")
        else:
            print("\n Tu lista de la compra (ordenada):")
            for producto in sorted(lista_compra):
                print(f" - {producto}")

    elif opcion == "4":
        while True:
            confirmar = input("¿Seguro que quieres vaciar la lista? (s/n): ").lower()
            if confirmar == "s":
                lista_compra.clear()
                print(" Lista vaciada correctamente.")
                break
            elif confirmar == "n":
                print("Operación cancelada.")
                break
            else:
                print("Respuesta no válida. Escribe 's' o 'n'.")

    elif opcion == "5":
        print("¡Gracias por usar el gestor de la compra! Hasta pronto.")
        break
    else:
        print("Opción no válida. Elige un número del 1 al 5.")
