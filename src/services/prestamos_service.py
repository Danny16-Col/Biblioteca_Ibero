from data.storage import libros, usuarios, prestamos

# Buscamos el libro en la base de datos recorriendo el arreglo
def buscar_libro(id_libro):
    for libro in libros:
        if libro.getId() == id_libro:
            return libro
    return None

# Buscamos el id del usuario en la base de datos recorriendo el arreglo
def buscar_usuario(id_usuario):
    for usuario in usuarios:
        if usuario.getId() == id_usuario:
            return usuario
    return None

# Funcion de prestar junto con el metodo del moduls/Libro 
def prestar_libro(id_usuario, id_libro):
    libro = buscar_libro(id_libro)
    if libro is None:
        return "Libro no existe"

    usuario = buscar_usuario(id_usuario)
    if usuario is None:
        return "Usuario no existe"

    if not libro.getDisponible():
        return "Libro no disponible"

    libro.prestar()

    prestamos.append({
        "id_libro": id_libro,
        "id_usuario": id_usuario
    })

    return "Libro prestado exitosamente"

# Funcionde devolver libro junto con el metodo devolver libro del moduls/Libro
def devolver_libro(id_usuario, id_libro):
    libro = buscar_libro(id_libro)
    if libro is None:
        return "Libro no existe"

    usuario = buscar_usuario(id_usuario)
    if usuario is None:
        return "Usuario no existe"

    if libro.getDisponible():
        return "El libro ya está disponible"

    prestamo_encontrado = None

    for prestamo in prestamos:
        if prestamo["id_usuario"] == id_usuario and prestamo["id_libro"] == id_libro:
            prestamo_encontrado = prestamo
            break

    if prestamo_encontrado is None:
        return "Este usuario no tiene este libro"

    prestamos.remove(prestamo_encontrado)

    libro.devolver()

    return "Libro devuelto correctamente"