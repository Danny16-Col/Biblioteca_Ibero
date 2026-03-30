from models.Usuario import Usuario
import json
import os

#Ruta al archivo JSOn donde se almacena los usuarios
RUTA = os.path.join(os.path.dirname(__file__), "..", "data", "usuarios.json")
RUTA = os.path.abspath(RUTA)

def cargar_usuarios():
    """Carga los usuarios desde el archivo JSON y los convierte en objetos
    
    Returns: Lista de objetos Usuarios
    """
    
    #Si el archivo no existe, retorna una lista vacia
    if not os.path.exists(RUTA):
        return[]
    
    
    with open (RUTA, "r") as f:
        data = json.load(f)
        
        usuarios = []
        
        #Convierte cada diccionario en objeto usuario
        for i, u in enumerate(data):
            usuario_obj = Usuario(
                u.get("id", i+1),
                u.get("nombre", "sin nombre"),
                u["usuario"],
                u["contraseña"] 
            )
            usuarios.append(usuario_obj)
        return usuarios
    
def guardar_usuario(usuarios):
    data =[]
    """
    Guarda la lista de objetos Usuario en el archivo JSON.

    Args:
        usuarios (list): Lista de objetos Usuario
    """
    
    for u in usuarios:
        data.append ({
            "id": u.get_id(),
            "nombre": u.get_nombre(),
            "usuario": u.get_usuario(),
            "contraseña":
u.get_contraseña()
        })
      
      #Escribe en el archivo JSON  
    with open(RUTA, "w") as f:
            json.dump(data, f, indent=4)
                
def registrar_usuario(nombre, usuario, contraseña):
    usuarios = cargar_usuarios()
   
    
    #Aqui se verifica si ya existe
    for u in usuarios:
        if u.get_usuario() == usuario:
            return False #Usuario ya existe
        
        #Crear nuevo usuario
    nuevo= Usuario(
        len(usuarios)+1,
        nombre,
        usuario,
        contraseña
    )
        
    usuarios.append(nuevo)
    guardar_usuario(usuarios)
    return nuevo.get_id()
""""   
def autenticar (usuario, contraseña):
        usuarios=cargar_usuarios()
        
        for u in usuarios:
            if u.get_usuario() == usuario and u.get_contraseña() == contraseña:
                return True
            
            return False
"""