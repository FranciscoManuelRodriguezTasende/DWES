class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

    def mostrar_info(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.titulo} - {estado}"

    def marcar_completada(self):
        self.completada = True

    def editar(self, nuevo_titulo, nueva_descripcion):
        self.titulo = nuevo_titulo
        self.descripcion = nueva_descripcion


def main():
    tareas = []

    while True:
        print("\n MENÚ DEL GESTOR DE TAREAS ")
        print("1️ Crear tarea")
        print("2️ Mostrar todas")
        print("3️ Marcar como completada")
        print("4️ Editar tarea")
        print("5️ Eliminar tarea")
        print("6️ Salir")

        opcion = input("Elige una opción (1-6): ")

        if opcion == "1":
            titulo = input("Título de la tarea: ").strip()
            descripcion = input("Descripción: ").strip()
            tarea = Tarea(titulo, descripcion)
            tareas.append(tarea)
            print("Tarea creada correctamente.")

        elif opcion == "2":
            if len(tareas) == 0:
                print("No hay tareas registradas.")
            else:
                print("\n LISTA DE TAREAS:")
                for i, tarea in enumerate(tareas, start=1):
                    print(f"{i}. {tarea.mostrar_info()}")

        elif opcion == "3":
            titulo_buscar = input("Título de la tarea a marcar como completada: ").strip().lower()
            for tarea in tareas:
                if tarea.titulo.lower() == titulo_buscar:
                    tarea.marcar_completada()
                    print("Tarea marcada como completada.")
                    break
            else:
                print("No se encontró ninguna tarea con ese título.")

        elif opcion == "4":
            titulo_buscar = input("Título de la tarea a editar: ").strip().lower()
            for tarea in tareas:
                if tarea.titulo.lower() == titulo_buscar:
                    nuevo_titulo = input("Nuevo título: ").strip()
                    nueva_descripcion = input("Nueva descripción: ").strip()
                    tarea.editar(nuevo_titulo, nueva_descripcion)
                    print("Tarea actualizada correctamente.")
                    break
            else:
                print("No se encontró ninguna tarea con ese título.")

        elif opcion == "5":
            titulo_buscar = input("Título de la tarea a eliminar: ").strip().lower()
            for tarea in tareas:
                if tarea.titulo.lower() == titulo_buscar:
                    tareas.remove(tarea)
                    print("Tarea eliminada correctamente.")
                    break
            else:
                print("No se encontró ninguna tarea con ese título.")

        elif opcion == "6":
            print("¡Hasta pronto! Gracias por usar el gestor de tareas.")
            break

        else:
            print("Opción no válida. Elige un número del 1 al 6.")

if __name__ == "__main__":
    main()
