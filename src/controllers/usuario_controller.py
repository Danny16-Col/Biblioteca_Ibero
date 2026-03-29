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
    
    nombre = input("Nombre completo: ").strip()
    usuario=input("Nuevo usuario: ").strip()
    contraseña = input("Nueva contraseña: ").strip()
             
    id_creado = registrar_usuario(nombre,usuario,contraseña)
             
    if id_creado:
        print(f"Usuario creado con ID: {id_creado}")
        print("Usuario registrado con exito")
        
    else:
        print("Ese usuario ya existe")
                    
                    

                        
                        