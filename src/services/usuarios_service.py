


import json
import os

RUTA = os.path.join(os.path.dirname(__file__), "..", "data", "usuarios.json")
RUTA = os.path.abspath(RUTA)

def cargar_usuarios():
    print("Ruta real:", os.path.abspath(RUTA))
    if not os.path.exists(RUTA):
        return[]
    with open (RUTA, "r") as f:
        return json.load(f)
    
def guardar_usuario(usuarios):
        with open(RUTA, "w") as f:
            json.dump(usuarios, f, indent=4)
                
def registrar_usuario(usuario, contraseña):
    usuarios = cargar_usuarios()
    print("Usuarios cargados: ",usuarios)
    
    #Aqui se verifica si ya existe
    for u in usuarios:
        if u["usuario"] == usuario:
            return False #Usuario ya existe
        
        #Crear nuevo usuario
    nuevo={
        "usuario":usuario,
        "contraseña":contraseña
        }
        
    usuarios.append(nuevo)
    guardar_usuario(usuarios)
    return True
    
def autenticar (usuario, contraseña):
        usuarios=cargar_usuarios()
        
        for u in usuarios:
            if u["usuario"]==usuario and u["contraseña"]==contraseña:
                return True
            
            return False