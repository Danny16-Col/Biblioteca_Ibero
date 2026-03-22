from services.usuarios_service import registrar_usuarios, autenticar

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
            