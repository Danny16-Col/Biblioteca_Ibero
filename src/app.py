from controllers.usuario_controller import registro
from controllers.libro_controller import listar_libros_controller, buscar_libro_controller, registrar_libro_controller
from controllers.prestar_controller import prestar_libro_controller
from controllers.devolver_controller import devolver_libro_controller

while True:

    print("\n--- BIBLIOTECA ---")

    print("1. Registrar Usuario")
    print("2. Registrar Libro")
    print("3. Listar Libros")
    print("4. Buscar Libro por ID")
    print("5. Prestar Libro")
    print("6. Devolver libro")
    print("7. SALIR")

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:

        registro()

    elif opcion == 2:

        id_libro = int(input("Ingrese ID del libro: "))
        titulo = input("Ingrese titulo: ")
        autor = input("Ingrese autor: ")

        resultado = registrar_libro_controller(id_libro, titulo, autor)
        print(resultado)

    elif opcion == 3:
        lista = listar_libros_controller()

        if lista:
            for libro in lista:
               print(f"{libro.getId()} - {libro.getTitulo()} - {libro.getAutor()}")
        else:
             print("No hay libros registrados")


    elif opcion == 4:

        id_libro = int(input("ID del libro seleccionado: "))

        libro = buscar_libro_controller(id_libro)

        if libro:
            print(f"Libro: {libro.getTitulo()} - {libro.getAutor()}")
        else:
            print("Libro no encontrado")

    elif opcion == 5:

        prestar_libro_controller()

    elif opcion == 6:
        
        devolver_libro_controller()

    elif opcion == 7:

        print("Gracias por utilizar nuestro sistema")
        break 

    else:

        print("Opcion invalida, intente de nuevo.")


    
