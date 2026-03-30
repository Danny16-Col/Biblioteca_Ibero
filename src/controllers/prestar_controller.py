from services.prestamos_service import prestar_libro


def prestar_libro_controller():

    print("\n" + "=" * 35)
    print("        BIBLIOTECA")
    print("=" * 35)
    print("        PRÉSTAMO DE LIBRO")
    print("-" * 35)

    # =======================
    # VALIDACIÓN ID USUARIO
    # =======================
    while True:
        entrada = input("Ingrese ID del usuario: ")

        # Validamos que no esté vacío y que sea número
        if not entrada.strip():
            print("El campo no puede estar vacío")
            continue

        if not entrada.isdigit():
            print("Debe ingresar solo números")
            continue

        id = int(entrada)

        if id <= 0:
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
    # PROCESO DE PRÉSTAMO
    # =======================
    resultado = prestar_libro(id, id_libro)

    print("-" * 35)
    print(f"Resultado: {resultado}")
    print("=" * 35)