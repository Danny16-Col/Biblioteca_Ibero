from Models.Libro import Libro

# Lista que almacena los libros (estructura de datos lineal tipo lista)
libros = []

def registrar_libro(id_libro, titulo, autor): 
    
    #Registra un nuevo libro en la lista y valida que el ID no esté repetido.
   

    # Verificar si el libro ya existe
    for libro in libros:
        if libro.getId() == id_libro:
            return "El libro ya existe"

    # Crear nuevo objeto Libro
    nuevo_libro = Libro(id_libro, titulo, autor)

    # Agregar el libro a la lista
    libros.append(nuevo_libro)

    return "Libro registrado correctamente"


def buscar_libro(id_libro):
    
    #Busca un libro por su ID recorriendo la lista y retorna el libro si existe, de lo contrario None.
    

    for libro in libros:
        if libro.getId() == id_libro:
            return libro

    return None