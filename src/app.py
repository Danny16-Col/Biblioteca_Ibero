# comentario
from controllers.prestar_controller import prestar_libro_controller
from controllers.devolver_controller import devolver_libro_controller

while True:

    print("\n--- BIBLIOTECA ---")

    print("1. Prestar")
    print("2. Devolver")
    print("3. SALIR ")

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:

        prestar_libro_controller()

    elif opcion == 2:

        devolver_libro_controller()

    elif opcion == 3:

        print("Saliendo...")
        break

    else:

        print("Opcion invalida") 

