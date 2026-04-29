from services.libro_service import buscar_libro, listar_libros
from controllers.prestar_controller import prestar_libro_controller
from controllers.devolver_controller import devolver_libro_controller
from services.buffer_libros import registrar_libro_buffer


# funcion para registrar libros usando el buffer libros
def registrar_libro_controller(id_libro, titulo, autor):

    if not titulo or not autor:  # validacion para evitar campos vacios
        return "Campos vacios"

    return registrar_libro_buffer(id_libro, titulo, autor)


# funcion para buscar un libro por ID
def buscar_libro_controller(id_libro):
    libro = buscar_libro(id_libro)
    return libro


# funcion para listar todos los libros
def listar_libros_controller():
    return listar_libros()