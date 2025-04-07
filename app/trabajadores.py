import ui.conexion as co
import mysql.connector 

def obtener_trabajadores():
    try:
        conn = co.obtener_conexion()
        if conn is not None:
            cursor = conn.cursor()
            query = """
            SELECT ID_tr, Nombre_tr, Apellido_tr, Cargo_tr, Salario, Fecha_Contratacion_tr, Correo_tr, Telefono_tr 
            FROM trabajadores
            """

            cursor.execute(query)
            trabajadores = cursor.fetchall()
            cursor.close()
            conn.close()
            return trabajadores
        else:
            print("No se pudo establecer conexión con la base de datos.")
            return []
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
        return []
# Función para insertar un nuevo trabajador
def insertar_trabajador(trabajador):
    """Inserta un nuevo trabajador en la base de datos."""
    conn = co.obtener_conexion()  # Obtiene la conexión desde tu módulo de conexión
    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO trabajadores (
            Nombre_tr, Apellido_tr, Cargo_tr, Salario, Fecha_Contratacion_tr, Correo_tr, Telefono_tr, 
            RFC_tr, CURP_tr, Direccion_tr, Codigo_Postal_tr, Rol_tr, Usuario_tr, Contraseña_tr
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            trabajador["nombre"], trabajador["apellido"], trabajador["cargo"], trabajador["salario"],
            trabajador["fecha_contratacion"], trabajador["correo"], trabajador["telefono"],
            trabajador["rfc"], trabajador["curp"], trabajador["direccion"], 
            trabajador["codigo_postal"], trabajador["rol"], trabajador["usuario"], trabajador["contrasena"]
        )
        cursor.execute(query, values)
        conn.commit()  # Confirmar los cambios
        print("Trabajador insertado correctamente.")
    except mysql.connector.Error as err:
        if err.errno == 1062:
            print("Error: El trabajador ya existe (clave duplicada).")
        else:
            print(f"Error al insertar el trabajador: {err}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        cursor.close()
        conn.close()

def obtener_trabajador_por_id(id_trabajador):
    """Devuelve los datos de un trabajador específico por su ID."""
    conn = co.obtener_conexion()
    if conn is None:
        raise ValueError("Error: No se pudo establecer la conexión con la base de datos.")

    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM trabajadores WHERE ID_tr = %s"
        cursor.execute(query, (id_trabajador,))
        resultado = cursor.fetchone()
        if resultado is None:
            print(f"No se encontró un trabajador con ID {id_trabajador}.")
        return resultado
    except Exception as e:
        print(f"Error al obtener el trabajador: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def modificar_trabajador(id_trabajador, nuevos_datos):
    """
    Modifica un trabajador existente en la base de datos.
    :param id_trabajador: ID del trabajador a modificar.
    :param nuevos_datos: Diccionario con los nuevos valores.
    """
    if not id_trabajador or not all(nuevos_datos.values()):
        raise ValueError("Error: Algunos campos en 'nuevos_datos' están vacíos o el ID no es válido.")

    conn = co.obtener_conexion()
    if conn is None:
        raise ValueError("Error: No se pudo establecer la conexión con la base de datos.")

    try:
        cursor = conn.cursor()
        query = """
        UPDATE trabajadores
        SET Nombre_tr = %s, Apellido_tr = %s, Cargo_tr = %s, Salario = %s, 
            Fecha_Contratacion_tr = %s, Correo_tr = %s, Telefono_tr = %s, RFC_tr = %s, 
            CURP_tr = %s, Direccion_tr = %s, Codigo_Postal_tr = %s, 
            Usuario_tr = %s, Contraseña_tr = %s
        WHERE ID_tr = %s
        """
        values = (
            nuevos_datos["nombre"], nuevos_datos["apellido"], nuevos_datos["cargo"],
            nuevos_datos["salario"], nuevos_datos["fecha_contratacion"],
            nuevos_datos["correo"], nuevos_datos["telefono"], nuevos_datos["rfc"],
            nuevos_datos["curp"], nuevos_datos["direccion"], nuevos_datos["codigo_postal"],
            nuevos_datos["usuario"], nuevos_datos["contrasena"], id_trabajador
        )
        cursor.execute(query, values)
        conn.commit()
        print(f"Trabajador con ID {id_trabajador} modificado correctamente.")
    except Exception as e:
        print(f"Error al modificar el trabajador: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def eliminar_trabajador(id_trabajador):
    """
    Elimina un trabajador de la base de datos.
    :param id_trabajador: ID del trabajador a eliminar.
    """
    conn = co.obtener_conexion()  # Obtiene la conexión
    try:
        cursor = conn.cursor()
        query = "DELETE FROM trabajadores WHERE ID_tr = %s"
        cursor.execute(query, (id_trabajador,))
        conn.commit()  # Confirmar los cambios
        print(f"Trabajador con ID {id_trabajador} eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar el trabajador: {e}")
    finally:
        cursor.close()
        conn.close()

