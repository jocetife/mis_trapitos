import mysql.connector
from mysql.connector import Error

def crear_conexion(host='localhost', database='mis_trapitos', user='root', password=''):
    """Crea y devuelve una conexión a la base de datos MySQL."""
    try:
        conexion = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None