


import json
import os

RUTA = "src/data/usuarios.json"

def cargar_usuarios():
    if not os.pat.exists(RUTA):
        return[]
    with open (RUTA, "r") as f:
        return json.load(f)
    
def guardar_usuarios(usuarios):
        with open(RUTA, "w") as f:
            json.dump(usuarios, f, indent=4)
                
def registrar_usuarios(usuario, contraseña):
    usuarios = cargar_usuarios()
    
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
        guardar_usuarios(usuarios)
        return True
    
    def autenticar (usuarios, contraseña):
        usuarios=cargar_usuarios()
        
        for u in usuarios:
            if u["usuario"]==usuario and u["contraseña"]==contraseña:
                return True
            
            return False