import mysql.connector
from mysql.connector import Error

def connect(host='localhost', database='mis_trapitos', user='root', password=''):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        if connection.is_connected():
            connection.autocommit = True
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None