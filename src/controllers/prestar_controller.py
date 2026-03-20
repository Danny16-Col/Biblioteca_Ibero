from services.prestamos_service import prestar_libro

def prestar_libro_controller():

    print("\n--- BIBLIOTECA ---")
    print("\n--- PRESTAMO LIBRO---")

    id_usuario = int(input("Ingrese ID del usuario: "))
    id_libro = int(input("Ingrese ID del libro: "))

    resultado = prestar_libro(id_usuario, id_libro)

    print(resultado)