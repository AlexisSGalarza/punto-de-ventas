import mysql.connector

def obtener_conexion():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="nuevo_ventas"
    )
    return conexion