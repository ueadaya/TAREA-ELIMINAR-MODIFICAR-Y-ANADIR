import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # Cambia según tu usuario MySQL
        password="",          # Cambia según tu contraseña MySQL
        database="desarrollo_web"
    )
