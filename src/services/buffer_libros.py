# se implementa un mecanismo interno de insercion aleatoria para reducir el riesgo de desbalanceo del arbol

import random
from services.libro_service import registrar_libro, buscar_libro

# lista temporal para guardar libros antes de insertarlos
buffer_libros = []

def registrar_libro_buffer(id_libro, titulo, autor):

    # se valida si el ID ya existe en el arbol
    if buscar_libro(id_libro) is not None:
        return "El libro ya existe..."

    # se valida si el ID ya esta en el buffer
    for libro in buffer_libros:
        if libro[0] == id_libro:
            return "El libro ya está en proceso de registro..."

    # se guarda en el buffer
    buffer_libros.append((id_libro, titulo, autor))

    # se procesa mescla e insecion
    procesar_buffer()

    return "Libro registrado correctamente."


def procesar_buffer():
    # se mescla para evitar desbalanceo del arbol
    random.shuffle(buffer_libros)

    for id_libro, titulo, autor in buffer_libros:
        registrar_libro(id_libro, titulo, autor)

    # limpiamos buffer
    buffer_libros.clear()