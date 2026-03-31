from services.libro_service import registrar_libro, buscar_libro, listar_libros
from controllers.prestar_controller import prestar_libro_controller
from controllers.devolver_controller import devolver_libro_controller
  
# función para registrar libros
def registrar_libro_controller(id_libro, titulo, autor):

    if not titulo or not autor: # validacion para evitar campos vacios
        return "Campos vacios"

    return registrar_libro(id_libro, titulo, autor)# se llama al service para registrar el libro

# función para buscar un libro por ID, si existe lo retorna
def buscar_libro_controller(id_libro):
    libro = buscar_libro(id_libro)
    return libro

# funcion para listar todos los libros registrados, con ID, titulo y autor
def listar_libros_controller():

    return listar_libros()  