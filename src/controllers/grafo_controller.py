from services.grafo_service import relacionar_libros_service


def relacionar_libros_controller():

    print("\n" + "=" * 35)
    print("        BIBLIOTECA")
    print("=" * 35)
    print("   RELACIONAR LIBROS (GRAFO)")
    print("-" * 35)

    # ID 1
    while True:
        entrada = input("Ingrese ID del primer libro: ")

        if not entrada.strip():
            print("El campo no puede estar vacío")
            continue

        if not entrada.isdigit():
            print("Debe ingresar solo números")
            continue

        id_libro1 = int(entrada)

        if id_libro1 <= 0:
            print("El ID debe ser mayor a 0")
            continue

        break

    # ID 2
    while True:
        entrada = input("Ingrese ID del segundo libro: ")

        if not entrada.strip():
            print("El campo no puede estar vacío")
            continue

        if not entrada.isdigit():
            print("Debe ingresar solo números")
            continue

        id_libro2 = int(entrada)

        if id_libro2 <= 0:
            print("El ID debe ser mayor a 0")
            continue

        break

    # proceso
    resultado = relacionar_libros_service(id_libro1, id_libro2)

    print("-" * 35)
    print(f"Resultado: {resultado}")
    print("=" * 35)