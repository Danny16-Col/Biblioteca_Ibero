# atributos libro
class Libro: 
    def __init__(self,id_libro,titulo,autor):
        self.__id_libro = id_libro
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = True

# getter
    def getId(self):
        return self.__id_libro
    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getDisponible(self):
        return self.__disponible
    
# setter
    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True # operacion exitosa
        return False
    
    def devolver(self):
        if not self.__disponible:
            self.__disponible = True
            return True
        return False
    