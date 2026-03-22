from services.prestamos_service import devolver_libro

def devolver_libro_controller():

    print("\n--- BIBLIOTECA ---")
    print("\n--- DEVOLVER LIBRO---")

    id_usuario = int(input("Ingrese ID del usuario: "))
    id_libro = int(input("Ingrese ID del libro: "))

    resultado = devolver_libro(id_usuario, id_libro)

    print(resultado)

