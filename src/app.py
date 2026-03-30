"""""""""

from controllers.usuario_controller import menu_login
menu_login()

from controllers.libro_controller import registrar_libro_controller, buscar_libro_controller # se importa desde controller el registro
from controllers.prestar_controller import prestar_libro_controller
from controllers.devolver_controller import devolver_libro_controller

     while True:
from controllers.libro_controller import registrar_libro_controller, buscar_libro_controller, listar_libros_controller # se importa desde controller el registro
from controllers.prestar_controller import prestar_libro_controller
from controllers.devolver_controller import devolver_libro_controller

while True:

    print("\n--- BIBLIOTECA ---")

    print("1. Prestar")
    print("2. Devolver")
    print("3. Registrar libro")
    print("4. Buscar libro")
    print("5. Listar Libros")
    print("6. SALIR")


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

            print("Libro no encontrado")

    elif opcion == 5:

        lista = listar_libros_controller()

        if lista:
            for libro in lista:
               print(f"{libro.getId()} - {libro.getTitulo()} - {libro.getAutor()}")
        else:
             print("No hay libros registrados")

    elif opcion == 6:
        
        print("Saliendo del sistema...")
        break

    else:

        print("Opcion invalida, intente de nuevo.") 


""""""
