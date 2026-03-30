from services.usuarios_service import registrar_usuario


"""""
  #Inicio de sesión de usuarios registrados          
def login():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
                
    if autenticar(usuario, contraseña):
        print(f"Bienvenido {usuario}")
        
        #Aqui se entra a la biblioteca
        menu_biblioteca()
    else:
        print("Credenciales incorrectas")
"""""     
#Registro para nuevos usuarios y se asigna un id               
def registro():
    
    nombre = input("Nombre completo: ").strip()
    usuario=input("Nuevo usuario: ").strip()
    contraseña = input("Nueva contraseña: ").strip()
             
    id_creado = registrar_usuario(nombre,usuario,contraseña)
             
    if id_creado:
        print(f"Usuario creado con ID: {id_creado}")
        print("Usuario registrado con exito")
        
    else:
        print("Ese usuario ya existe")
                    
                    

                        
                        