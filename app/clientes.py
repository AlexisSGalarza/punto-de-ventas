import db.conexion as co
import mysql.connector 

def obtener_clientes():
    try:
        conn = co.obtener_conexion()
        if conn is not None:
            cursor = conn.cursor()
            query = """
            SELECT ID_cl, Nombre_cl, Apellido_cl, Correo_cl, Telefono_cl, Direccion_cl, Fecha_Registro_cl
            FROM clientes
            """

            cursor.execute(query)
            clientes = cursor.fetchall()
            cursor.close()  
            conn.close()
            return clientes
        else:
            print("No se pudo establecer conexión con la base de datos.")
            return []
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
        return []

# Función para insertar un nuevo cliente
def insertar_cliente(cliente):
    """Inserta un nuevo cliente en la base de datos."""
    conn = co.obtener_conexion()  # Obtiene la conexión desde tu módulo de conexión
    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO clientes (
            Nombre_cl, Apellido_cl, Correo_cl, Telefono_cl, Direccion_cl, RFC_cl, CURP_cl, Codigo_Postal_cl
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            cliente["nombre"], cliente["apellido"], cliente["correo"], cliente["telefono"],
            cliente["direccion"], cliente["rfc"], cliente["curp"], cliente["codigo_postal"]
        )
        cursor.execute(query, values)
        conn.commit()  # Confirmar los cambios
        print("Cliente insertado correctamente.")
    except mysql.connector.Error as err:
        if err.errno == 1062:
            print("Error: El cliente ya existe (clave duplicada).")
        else:
            print(f"Error al insertar el cliente: {err}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        cursor.close()
        conn.close()

def obtener_cliente_por_id(id_cliente):
    """Devuelve los datos de un cliente específico por su ID."""
    conn = co.obtener_conexion()
    if conn is None:
        raise ValueError("Error: No se pudo establecer la conexión con la base de datos.")

    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM clientes WHERE ID_cl = %s"
        cursor.execute(query, (id_cliente,))
        resultado = cursor.fetchone()
        if resultado is None:
            print(f"No se encontró un cliente con ID {id_cliente}.")
        return resultado
    except Exception as e:
        print(f"Error al obtener el cliente: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def modificar_cliente(id_cliente, nuevos_datos):
    """
    Modifica un cliente existente en la base de datos.
    :param id_cliente: ID del cliente a modificar.
    :param nuevos_datos: Diccionario con los nuevos valores.
    """
    if not id_cliente or not all(nuevos_datos.values()):
        raise ValueError("Error: Algunos campos en 'nuevos_datos' están vacíos o el ID no es válido.")

    conn = co.obtener_conexion()
    if conn is None:
        raise ValueError("Error: No se pudo establecer la conexión con la base de datos.")

    try:
        cursor = conn.cursor()
        query = """
        UPDATE clientes
        SET Nombre_cl = %s, Apellido_cl = %s, Correo_cl = %s, Telefono_cl = %s, 
            Direccion_cl = %s, RFC_cl = %s, CURP_cl = %s, Codigo_Postal_cl = %s
        WHERE ID_cl = %s
        """
        values = (
            nuevos_datos["nombre"], nuevos_datos["apellido"], nuevos_datos["correo"], nuevos_datos["telefono"],
            nuevos_datos["direccion"], nuevos_datos["rfc"], nuevos_datos["curp"], nuevos_datos["codigo_postal"], id_cliente
        )
        cursor.execute(query, values)
        conn.commit()
        print(f"Cliente con ID {id_cliente} modificado correctamente.")
    except Exception as e:
        print(f"Error al modificar el cliente: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def eliminar_cliente(id_cliente):
    """
    Elimina un cliente de la base de datos.
    :param id_cliente: ID del cliente a eliminar.
    """
    conn = co.obtener_conexion()  # Obtiene la conexión
    try:
        cursor = conn.cursor()
        query = "DELETE FROM clientes WHERE ID_cl = %s"
        cursor.execute(query, (id_cliente,))
        conn.commit()  # Confirmar los cambios
        print(f"Cliente con ID {id_cliente} eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar el cliente: {e}")
    finally:
        cursor.close()
        conn.close()