import mysql.connector

# Función para establecer y retornar la conexión
def obtener_conexion():
    conexion = mysql.connector.connect(
        host="localhost",  # Dirección del servidor
        port=3306,         # Puerto predeterminado para MySQL
        user="root",       # Nombre de usuario
        password="1234",   # Contraseña
        database="nuevo_ventas"  # Nombre de la base de datos
    )
    
    if conexion.is_connected():
        print("¡Conexión exitosa!")
        return conexion
    else:
        print("Error en la conexión.")
        return None

# Uso de la función
conexion = obtener_conexion()

# Aquí puedes realizar tus consultas SQL utilizando el objeto `conexion`
