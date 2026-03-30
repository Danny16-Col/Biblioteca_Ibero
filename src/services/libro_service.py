from Models.Libro import Libro
from data.storage import libros #se llama a libros desde data/storage
def registrar_libro(id_libro, titulo, autor): 
    
    # registra un nuevo libro en la lista y validar que el ID no este repetido, asi como verificar si el libro ya existe
    for libro in libros:
        if libro.getId() == id_libro:
            return "El libro ya existe"

    # crear nuevo objeto Libro
    nuevo_libro = Libro(id_libro, titulo, autor)

    # agregar el libro a la lista
    libros.append(nuevo_libro)

    return "Libro registrado correctamente"

def buscar_libro(id_libro):
    
    # busca un libro por su ID recorriendo la lista y retorna el libro si existe, de lo contrario None.
    for libro in libros:
        if libro.getId() == id_libro:
            return libro

    return None

def listar_libros():
    
    return libros