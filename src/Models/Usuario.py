# se crea para puebas
class Usuario:
    def __init__(self, id_usuario, nombre):
        self.__id_usuario = id_usuario
        self.__nombre = nombre

    def getId(self):
        return self.__id_usuario

    def getNombre(self):
        return self.__nombre