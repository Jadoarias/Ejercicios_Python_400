def login():
    usuario = "usuario1"
    contraseña = "asdasd"
    c = 0
    ingresausuario = input("Ingrese su usuario: ")
    ingresacontraseña= input("Ingrese su contraseña: ")
    while (c <= 2):
        c = c + 1
        if usuario == ingresausuario and contraseña == ingresacontraseña:
            print("Bienvenido")
            break
        else:
            if c < 2:
                print("Contraseña Incorrecta, vuelve a intentarlo")
            else:
                ingresausuario = input("Ingrese su usuario: ")
                ingresacontraseña= input("Ingrese su contraseña: ")
    return
login()