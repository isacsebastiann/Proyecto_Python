import sqlite3

def inicializar_db():
    conexion = sqlite3.connect('contrasenas.db')
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contrasenas
                      (id INTEGER PRIMARY KEY, servicio TEXT, usuario TEXT, contrasena BLOB)''')
    conexion.commit()
    conexion.close()

def agregar_contrasena(servicio, usuario, contrasena_cifrada):
    conexion = sqlite3.connect('contrasenas.db')
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO contrasenas (servicio, usuario, contrasena) VALUES (?, ?, ?)",
                   (servicio, usuario, contrasena_cifrada))
    conexion.commit()
    conexion.close()

def obtener_contrasenas():
    conexion = sqlite3.connect('contrasenas.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT servicio, usuario, contrasena FROM contrasenas")
    filas = cursor.fetchall()
    conexion.close()
    return filas
