import random

while True:
    print("Bienvenido al juego: ¡Adivina el número!")
    print("El programa pensará un número entre 1 y un máximo que tú elijas según el nivel.")
    print("Intenta adivinarlo con la menor cantidad de intentos posible.\n")

    while True:
        nivel = input("Elige nivel (fácil / medio / difícil): ").lower()

        if nivel in ["fácil", "facil"]:
            maximo = 50
            break
        elif nivel == "medio":
            maximo = 100
            break
        elif nivel in ["difícil", "dificil"]:
            maximo = 500
            break
        else:
            print("Nivel no válido. Escribe 'fácil', 'medio' o 'difícil'.\n")

    numero_secreto = random.randint(1, maximo)
    intentos = 0

    while True:
        try:
            numero_usuario = int(input(f"Adivina el número (entre 1 y {maximo}): "))
            intentos += 1

            if numero_usuario < 1 or numero_usuario > maximo:
                print(f"El número debe estar entre 1 y {maximo}. Inténtalo de nuevo.\n")
                continue

            if numero_usuario < numero_secreto:
                print("Demasiado bajo.\n")
            elif numero_usuario > numero_secreto:
                print("Demasiado alto.\n")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.\n")
                break

        except ValueError:
            print("❌ Entrada no válida. Debes escribir un número entero.\n")

    while True:
        jugar_otra = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_otra == "s":
            break
        elif jugar_otra == "n":
            print("¡Gracias por jugar! ¡Hasta la próxima!")
            exit()
        else:
            print("Respuesta no válida. Escribe 's' para sí o 'n' para no.\n")
