from services.libro_service import registrar_libro, buscar_libro

def registrar_libro_controller(id_libro, titulo, autor):

    #Controlador para registrar un libro, valida datos y llama al servicio.
   

    if not titulo or not autor:
        return "Campos vacíos"

    return registrar_libro(id_libro, titulo, autor)


def buscar_libro_controller(id_libro):
    
    #Controlador para buscar un libro.
    

    libro = buscar_libro(id_libro)

    if libro:
        return libro
    else:
        return None