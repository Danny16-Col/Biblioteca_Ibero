from data.storage import libros, prestamos
from services.usuarios_service import cargar_usuarios


# =======================
# BÚSQUEDAS
# =======================

# Busca un libro por su ID recorriendo la lista
def buscar_libro(id_libro):
    for libro in libros:
        if libro.getId() == id_libro:
            return libro
    return None


# Busca un usuario por su ID cargando desde el JSON
def buscar_usuario(id):
    usuarios = cargar_usuarios()

    for usuario in usuarios:
        if usuario.get_id() == id:
            return usuario
    return None


# =======================
# PRÉSTAMO DE LIBROS
# =======================

# Permite prestar un libro a un usuario
def prestar_libro(id, id_libro):

    # Validamos que el libro exista
    libro = buscar_libro(id_libro)
    if libro is None:
        return "Libro no existe"

    # Validamos que el usuario exista
    usuario = buscar_usuario(id)
    if usuario is None:
        return "Usuario no existe"

    # Validamos que el libro esté disponible
    if not libro.getDisponible():
        return "Libro no disponible"

    # Cambiamos el estado del libro a prestado
    libro.prestar()

    # Guardamos el préstamo en la lista
    prestamos.append({
        "id_libro": id_libro,
        "id_usuario": id
    })

    return "Libro prestado exitosamente"


# =======================
# DEVOLUCIÓN DE LIBROS
# =======================

# Permite devolver un libro prestado
def devolver_libro(id, id_libro):

    # Validamos que el libro exista
    libro = buscar_libro(id_libro)
    if libro is None:
        return "Libro no existe"

    # Validamos que el usuario exista
    usuario = buscar_usuario(id)
    if usuario is None:
        return "Usuario no existe"

    # Si el libro ya está disponible, no se puede devolver
    if libro.getDisponible():
        return "El libro ya está disponible"

    prestamo_encontrado = None

    # Buscamos el préstamo en la lista
    for prestamo in prestamos:
        if prestamo["id_usuario"] == id and prestamo["id_libro"] == id_libro:
            prestamo_encontrado = prestamo
            break 

    # Si no se encontró el préstamo
    if prestamo_encontrado is None:
        return "Este usuario no tiene este libro"

    # Eliminamos el préstamo de la lista
    prestamos.remove(prestamo_encontrado)

    # Cambiamos el estado del libro a disponible
    libro.devolver()

    return "Libro devuelto correctamente"