import db.conexion as co
import mysql.connector
import bcrypt

def autentacacion_login(usuario, contrasena):

    try:
        conn = co.obtener_conexion()  # Obtener la conexión desde el módulo externo
        cursor = conn.cursor(dictionary=True)  # Crear el cursor para ejecutar la consulta

        # Seleccionar el nombre, el rol y la contraseña hasheada
        consulta = """
            SELECT Nombre_tr, Rol_tr, Contraseña_tr 
            FROM trabajadores
            WHERE Usuario_tr = %s
        """
        cursor.execute(consulta, (usuario,))  # Ejecutar la consulta con usuario dentro de una tupla
        resultado = cursor.fetchone()  # Obtener el primer resultado

        cursor.close()  # Cerrar el cursor
        conn.close()  # Cerrar la conexión

        if resultado:
            # Verificar la contraseña ingresada con el hash almacenado
            hash_almacenado = resultado["Contraseña_tr"].encode('utf-8')  # Convertir el hash a bytes
            if bcrypt.checkpw(contrasena.encode('utf-8'), hash_almacenado):
                # Si la contraseña coincide, retorna el nombre y el rol
                return {"Nombre_tr": resultado["Nombre_tr"], "Rol_tr": resultado["Rol_tr"]}
            else:
                return None  # Contraseña incorrecta
        else:
            return None  # Usuario no encontrado

    except mysql.connector.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None