from services.libro_service import registrar_libro, buscar_libro, listar_libros
from controllers.prestar_controller import prestar_libro_controller
from controllers.devolver_controller import devolver_libro_controller

def listar_libros_controller():

    return listar_libros()    

def registrar_libro_controller(id_libro, titulo, autor):

    if not titulo or not autor:
        return "Campos vacios"

    return registrar_libro(id_libro, titulo, autor)


def buscar_libro_controller(id_libro):
    libro = buscar_libro(id_libro)
    return libro