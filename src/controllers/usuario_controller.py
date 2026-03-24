from services.usuarios_service import registrar_usuario, autenticar

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
            
def login():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
                
    if autenticar(usuario, contraseña):
        print(f"Bienvenido {usuario}")
    else:
        print("Credenciales incorrectas")
                    
def registro():
    usuario=input("Nuevo usuario: ")
    contraseña = input("Nueva contraseña: ")
             
    if registrar_usuario(usuario, contraseña):
        print("Usuario registrado con exito")
    else:
        print("Ese usuario ya existe")
                    
                    

                        
                        