class Usuario:
    def __init__(self, id_usuario, nombre, usuario, contraseña):
    #Juan estos son loos atributos que se necestian para crear un usuario
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__usuario = usuario
        self.__contraseña = contraseña

    def get_id(self):
        return self.__id_usuario

    def get_nombre(self):
        return self.__nombre
    
    def get_usuario(self):
        return self.__usuario
    
    def get_contraseña(self):
        return self.__contraseña

