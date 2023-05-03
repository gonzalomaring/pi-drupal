def login():
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    while username != "admin" or password != "admin":
        print("Credenciales incorrectas. Inténtalo de nuevo.")
        print()
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
    print()
    print("Bienvenido, admin")
    print()
