from services.usuarios_service import registrar_usuario
          
def registro():
    
    #Solicita el nombre completo del usuario y elimina espacios innecesarios
    nombre = input("Nombre completo: ").strip()
    
    #Solicita un nombre de usuario
    usuario=input("Nuevo usuario: ").strip()
    #Solicita una contraseña nueva
    contraseña = input("Nueva contraseña: ").strip()
 
 #Llama al servicio para registrar el usuario            
    id_creado = registrar_usuario(nombre,usuario,contraseña)
      
      #Si se crea correctamente, el servicio retorna el ID del usuario       
    if id_creado:
        print(f"Usuario creado con ID: {id_creado}")
        print("Usuario registrado con exito")
        
        #Si no, significa que el usuario ya existe
    else:
        print("Ese usuario ya existe")
                    
                    
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
                        
                        