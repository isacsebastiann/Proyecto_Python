from cryptography.fernet import Fernet
import os

def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as clave_file:
        clave_file.write(clave)

def cargar_clave():
    if not os.path.exists("clave.key"):
        generar_clave()
    return open("clave.key", "rb").read()

def inicializar_fernet():
    clave = cargar_clave()
    return Fernet(clave)

def cifrar_contrasena(contrasena):
    f = inicializar_fernet()
    contrasena_cifrada = f.encrypt(contrasena.encode())
    return contrasena_cifrada

def descifrar_contrasena(contrasena_cifrada):
    f = inicializar_fernet()
    contrasena_descifrada = f.decrypt(contrasena_cifrada).decode()
    return contrasena_descifrada
