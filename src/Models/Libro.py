# Clase que representa un libro dentro del sistema
class Libro:

    # Constructor: inicializa los atributos del libro
    def __init__(self, id_libro, titulo, autor):
        self.__id_libro = id_libro
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = True  # Por defecto, el libro está disponible

    # =======================
    # GETTERS (consultas)
    # =======================

    # Retorna el ID del libro
    def getId(self):
        return self.__id_libro

    # Retorna el título del libro
    def getTitulo(self):
        return self.__titulo

    # Retorna el autor del libro
    def getAutor(self):
        return self.__autor

    # Retorna el estado de disponibilidad (True/False)
    def getDisponible(self):
        return self.__disponible

    # =======================
    # MÉTODOS DE ESTADO
    # =======================

    # Marca el libro como prestado (disponible = False)
    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True  # Operación exitosa
        return False  # Ya estaba prestado

    # Marca el libro como devuelto (disponible = True)
    def devolver(self):
        if not self.__disponible:
            self.__disponible = True
            return True  # Operación exitosa
        return False  # Ya estaba disponible