from Models.Libro import Libro
from data.storage import libros

def registrar_libro(id_libro, titulo, autor):
    # se crea el libro
    nuevo_libro = Libro(id_libro, titulo, autor)

    # se inserta el libro en el arbol
    insertado = libros.insertar(nuevo_libro)

    # si ya existe ese ID, no lo deja registrar
    if not insertado:
        return "El libro ya existe..."

    return "Libro registrado correctamente."

    # buscar libro por ID usando el arbol
def buscar_libro(id_libro):

    # busqueda del libro en el arbol
    libro = libros.buscar(id_libro)

    # si no existe, retorna None
    return libro

    # listar

    # listar libros usando el arbol
def listar_libros():

    # retorna los libros en orden
    return libros.listar()