from data.storage import  grafo_libros
from services.libro_service import buscar_libro

def relacionar_libros_service(id_libro1, id_libro2):

    if id_libro1 == id_libro2:
        return "Un libro no puede relacionarse consigo mismo"
    
    libro1 = buscar_libro(id_libro1)
    libro2 = buscar_libro(id_libro2)

    if libro1 is None :
        return f"El libro con el id {id_libro1} no existe"
    if libro2 is None:
        return f"El libro con el id {id_libro2} no existe"
    
    return grafo_libros.relacionar_libros(id_libro1, id_libro2)

def recomendar_libros_service(id_libro):

    relaciones = grafo_libros.obtener_relaciones(id_libro)

    libro = buscar_libro(id_libro)

    if libro is None:
        return "El libro no existe"
    
    if not relaciones:
        return "No hay recomendaciones"
    
    recomendaciones = []

    for id_relacionado in relaciones:
        libro_rel = buscar_libro(id_relacionado)

        if libro_rel:
            recomendaciones.append(libro_rel.getTitulo())

    return {
        "libro": libro.getTitulo(),
        "recomendaciones": recomendaciones
    }
    