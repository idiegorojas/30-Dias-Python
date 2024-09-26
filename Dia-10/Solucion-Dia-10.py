class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = 'pendiente'

    def completar(self):
        self.estado = 'completada'

    def __str__(self):
        return f'Titulo: {self.titulo}, Descripcion: {self.descripcion}, Estado: {self.estado}'

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion):
        nueva_tarea = Tarea(titulo, descripcion)
        self.tareas.append(nueva_tarea)

    def eliminar_tarea(self, titulo):
        self.tareas = [tarea for tarea in self.tareas if tarea.titulo != titulo]

    def listar_tareas(self):
        for tarea in self.tareas:
            print(tarea)

    def completar_tarea(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                tarea.completar()

def menu():
    gestor = GestorTareas()
    while True:
        print("\nSistema de Gestión de Tareas")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Listar tareas")
        print("4. Completar tarea")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            gestor.agregar_tarea(titulo, descripcion)
        elif opcion == '2':
            titulo = input("Ingrese el título de la tarea a eliminar: ")
            gestor.eliminar_tarea(titulo)
        elif opcion == '3':
            gestor.listar_tareas()
        elif opcion == '4':
            titulo = input("Ingrese el título de la tarea a completar: ")
            gestor.completar_tarea(titulo)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()