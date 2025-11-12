import random

opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]

reglas = {
    "tijera": ["papel", "lagarto"],
    "papel": ["piedra", "spock"],
    "piedra": ["tijera", "lagarto"],
    "lagarto": ["spock", "papel"],
    "spock": ["piedra", "tijera"]
}

def determinar_resultado(jugador, cpu):
    if jugador == cpu:
        return 0
    elif cpu in reglas[jugador]:
        return 1
    else:
        return -1

def jugar_ronda():
    while True:
        jugador = input("Elige tu jugada (piedra, papel, tijera, lagarto, spock): ").lower()
        if jugador in opciones:
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")

    cpu = random.choice(opciones)
    print(f"\nTú: {jugador}  vs  CPU: {cpu}")

    resultado = determinar_resultado(jugador, cpu)

    if resultado == 0:
        print("¡Empate!\n")
    elif resultado == 1:
        print("¡Ganaste esta ronda!\n")
    else:
        print("Gana la CPU esta ronda.\n")

    return resultado

def jugar_partida():
    while True:
        try:
            n = int(input("¿A cuántas rondas (impar ≥ 1) quieres jugar?: "))
            if n >= 1 and n % 2 == 1:
                break
            else:
                print("El número debe ser impar y mayor o igual a 1.\n")
        except ValueError:
            print("Debes escribir un número entero.\n")

    victorias_necesarias = n // 2 + 1
    puntos_jugador = 0
    puntos_cpu = 0

    while puntos_jugador < victorias_necesarias and puntos_cpu < victorias_necesarias:
        resultado = jugar_ronda()

        if resultado == 1:
            puntos_jugador += 1
        elif resultado == -1:
            puntos_cpu += 1

        print(f"Marcador: {puntos_jugador} - {puntos_cpu} \n")

    if puntos_jugador > puntos_cpu:
        print("¡Ganaste la partida!\n")
    else:
        print("La CPU gana la partida.\n")

while True:
    jugar_partida()

    while True:
        repetir = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if repetir == "s":
            break
        elif repetir == "n":
            print("¡Gracias por jugar! ¡Hasta la próxima!")
            exit()
        else:
            print("Respuesta no válida. Escribe 's' para sí o 'n' para no.\n")
