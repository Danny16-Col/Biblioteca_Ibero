"""
from services.libro_service import registrar_libro, buscar_libro, listar_libros

def registrar_libro_controller(id_libro, titulo, autor):

    #controlador para registrar un libro, valida datos y llama al servicio.
    if not titulo or not autor:
        return "Campos vacios"

    return registrar_libro(id_libro, titulo, autor)

def buscar_libro_controller(id_libro):
    
    #controlador para buscar un libro.
    libro = buscar_libro(id_libro)
    
    return libro

    
from services.libro_service import registrar_libro, buscar_libro
from controllers.prestar_controller import prestar_libro_controller
from controllers.devolver_controller import devolver_libro_controller


def registrar_libro_controller(id_libro, titulo, autor):

    if not titulo or not autor:
        return "Campos vacios"

    return registrar_libro(id_libro, titulo, autor)


def buscar_libro_controller(id_libro):
    libro = buscar_libro(id_libro)
    return libro


def menu_biblioteca():
    while True:

        print("\n--- BIBLIOTECA ---")

        print("1. Prestar")
        print("2. Devolver")
        print("3. Registrar libro")
        print("4. Buscar libro")
        print("5. SALIR")

        try:
            opcion = int(input("Seleccione una opcion: "))
        except:
            print("Ingrese un número válido")
            continue

        if opcion == 1:
            prestar_libro_controller()

        elif opcion == 2:
            devolver_libro_controller()

        elif opcion == 3:
            id_libro = int(input("Ingrese ID del libro: "))
            titulo = input("Ingrese titulo: ")
            autor = input("Ingrese autor: ")

            resultado = registrar_libro_controller(id_libro, titulo, autor)
            print(resultado)

        elif opcion == 4:
            id_libro = int(input("ID del libro seleccionado: "))

            libro = buscar_libro_controller(id_libro)

            if libro:
                print(f"Libro: {libro.getTitulo()} - {libro.getAutor()}")
            else:
                print("Libro no encontrado")

        elif opcion == 5:
            print("Saliendo del sistema...")
            break

        else:
            print("Opcion invalida, intente de nuevo.")


def listar_libros_controller():

    return listar_libros()    

""""""