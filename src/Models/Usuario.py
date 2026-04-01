class Usuario:
    #Clase que representa un usuario del sistema.
    
    def __init__(self, id_usuario, nombre, usuario, contraseña):
        #Constructor de la clase usuario
        
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__usuario = usuario
        self.__contraseña = contraseña

    def get_id(self):
        return self.__id_usuario
    #Retorna el ID del usuario

    def get_nombre(self):
        return self.__nombre
    #Retorna el nombre del usuario
    
    def get_usuario(self):
        return self.__usuario
    #Retorna el nombre de usuario
    
    def get_contraseña(self):
        return self.__contraseña
    #Retorna la contraseña del usuario

