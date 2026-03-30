from services.usuarios_service import registrar_usuario, autenticar
from controllers.libro_controller import menu_biblioteca


#aqui realice la interfaz del login de usuario

def menu_login():
    while True:
        print("\n=== SISTEMA BIBLIOTECA ===")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        
        opcion = input("Selecione una opción: ")
        
        if opcion == "1":
            login()
        elif opcion == "2":
            registro()
        elif opcion =="3":
            print("Hasto luego")
            break
        else:
            print("Opción inválida")
  
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
                    
                    

                        
                        