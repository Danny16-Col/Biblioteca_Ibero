from services.prestamos_service import devolver_libro


def devolver_libro_controller():

    print("\n" + "=" * 35)
    print("        BIBLIOTECA")
    print("=" * 35)
    print("        DEVOLUCIÓN DE LIBRO")
    print("-" * 35)

    # =======================
    # VALIDACIÓN ID USUARIO
    # =======================
    while True:
        entrada = input("Ingrese ID del usuario: ")

        if not entrada.strip():
            print("El campo no puede estar vacío")
            continue

        if not entrada.isdigit():
            print("Debe ingresar solo números")
            continue

        id_usuario = int(entrada)

        if id_usuario <= 0:
            print("El ID debe ser mayor a 0")
            continue

        break

    # =======================
    # VALIDACIÓN ID LIBRO
    # =======================
    while True:
        entrada = input("Ingrese ID del libro: ")

        if not entrada.strip():
            print("El campo no puede estar vacío")
            continue

        if not entrada.isdigit():
            print("Debe ingresar solo números")
            continue

        id_libro = int(entrada)

        if id_libro <= 0:
            print("El ID debe ser mayor a 0")
            continue

        break

    # =======================
    # PROCESO DE DEVOLUCIÓN
    # =======================
    resultado = devolver_libro(id_usuario, id_libro)

    print("-" * 35)
    print(f"Resultado: {resultado}")
    print("=" * 35)