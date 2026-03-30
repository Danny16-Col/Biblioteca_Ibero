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

def listar_libros_controller():

    return listar_libros()    