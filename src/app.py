from controllers.usuario_controller import registro
from controllers.libro_controller import listar_libros_controller, buscar_libro_controller, registrar_libro_controller
from controllers.prestar_controller import prestar_libro_controller
from controllers.devolver_controller import devolver_libro_controller

while True:

    print("\n--- BIBLIOTECA ---")

    print("1. Registrar Usuario")
    print("2. Registrar Libro")     #vladimir
    print("3. Listar Libros")       #vladimir 
    print("4. Buscar Libro por ID") #vladimir 
    print("5. Prestar Libro")
    print("6. Devolver libro")
    print("7. SALIR")

    while True: # condicional para validar la opcion del menu
        try:
            opcion = int(input("Seleccione una opcion: "))
        
            if opcion < 1 or opcion > 7:   # validamos que el usuario solo marque un numero del 1 al 7
                print("Debe seleccionar un numero del 1 al 7")
                continue
        
            break  # si se cumple sale del while

        except ValueError:
            print("Debe ingresar un numero valido")

    if opcion == 1:

        registro()

    elif opcion == 2:

        while True: #validasmos que el ID sea un numero mayor a cero y que no sea una letra
            try:
                id_libro = int(input("Ingrese ID del libro: "))

                if id_libro <= 0:
                   print("El ID debe ser mayor a 0")
                   continue

                break  # si todo esta ok  sale del while

            except ValueError:
                 print("Debe ingresar un numero valido...")
        titulo = input("Ingrese titulo: ")
        autor = input("Ingrese autor: ")

        resultado = registrar_libro_controller(id_libro, titulo, autor)
        print(resultado)

    elif opcion == 3:

        lista = listar_libros_controller()

        if lista:
            print("\nID   | TITULO                | AUTOR")
            print("----------------------------------------")

            for libro in lista:
                print(f"{libro.getId():<4} | {libro.getTitulo():<20} | {libro.getAutor()}")
        else:
            print("No hay libros registrados")


    elif opcion == 4:

        while True:  # se valida la busqueda con un submenu
            print("\n--- BUSCAR LIBRO ---")
            print("1. Ingresar ID")
            print("2. Volver")

            try:
                 sub = int(input("Seleccione una opcion: "))
            except ValueError:
                print("Debe ingresar un numero valido..")
                continue

            if sub == 1:
                # se valida ID del libro, que sea un numero positivo y que no ingresen una letra u otro caracter
                while True:
                    try:
                        id_libro = int(input("ID del libro: "))

                        if id_libro <= 0:
                            print("El ID debe ser un numero positivo..")
                            continue

                        break
                    except ValueError:
                        print("Debe ingresar un numero valido..")

                # se busca el libro y se dan los datos del mismo
                libro = buscar_libro_controller(id_libro)

                if libro:
                    print(f"\nLibro encontrado:")
                    print(f"ID: {libro.getId()}")
                    print(f"Titulo: {libro.getTitulo()}")
                    print(f"Autor: {libro.getAutor()}")
                else:
                    print("Libro no encontrado")

            elif sub == 2:
                break  # aqui volvemos al menu principal

            else:
                print("Opcion no valida, intentelo nuevamente...")

    elif opcion == 5:

        prestar_libro_controller()

    elif opcion == 6:
        
        devolver_libro_controller()

    elif opcion == 7:

        print("Gracias por utilizar nuestro sistema.")
        break 

    else:

        print("Opcion invalida, intente de nuevo.")


    
