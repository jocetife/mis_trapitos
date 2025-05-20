import mysql.connector
from mysql.connector import Error

def connect(host='localhost', database='mis_trapitos', user='root', password=''):
    """Crea y devuelve una conexión a la base de datos MySQL."""
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None