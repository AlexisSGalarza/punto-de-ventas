import db.conexion as co
import mysql.connector 

def obtener_productos():
    try:
        conn = co.obtener_conexion()
        if conn is not None:
            cursor = conn.cursor()
            query = """
            SELECT ID_pr, Nombre_pr, Descripcion_pr, codigo_barras_pr, codigo_producto_pr, Categoria_pr, Precio_pr,Stock_pr
            FROM productos;
            """

            cursor.execute(query)
            productos = cursor.fetchall()
            cursor.close()
            conn.close()
            return productos
        else:
            print("No se pudo establecer conexión con la base de datos.")
            return []
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
        return []
    
def insertar_producto(producto):
    """Inserta un nuevo producto en la base de datos."""
    conn = co.obtener_conexion()  # Obtiene la conexión desde tu módulo de conexión
    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO productos (
            Nombre_pr, Descripcion_pr, Precio_pr, Stock_pr, Categoria_pr, Proveedor_pr, codigo_barras_pr, codigo_producto_pr
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            producto["nombre"], producto["descripcion"], producto["precio"], producto["stock"],
            producto["categoria"], producto["proveedor"], producto["codigo_barras"], producto["codigo_producto"]
        )
        cursor.execute(query, values)
        conn.commit()  # Confirmar los cambios
        print("Producto insertado correctamente.")
    except mysql.connector.Error as err:
        if err.errno == 1062:
            print("Error: El producto ya existe (clave duplicada).")
        else:
            print(f"Error al insertar el producto: {err}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        cursor.close()
        conn.close()
def obtener_producto_por_id(id_producto):
    """Devuelve los datos de un producto específico por su ID."""
    conn = co.obtener_conexion()
    if conn is None:
        raise ValueError("Error: No se pudo establecer la conexión con la base de datos.")

    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM productos WHERE ID_pr = %s"
        cursor.execute(query, (id_producto,))
        resultado = cursor.fetchone()
        if resultado is None:
            print(f"No se encontró un producto con ID {id_producto}.")
        return resultado
    except Exception as e:
        print(f"Error al obtener el producto: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def modificar_producto(id_producto, nuevos_datos):
    """
    Modifica un producto existente en la base de datos.
    :param id_producto: ID del producto a modificar.
    :param nuevos_datos: Diccionario con los nuevos valores.
    """
    if not id_producto or not all(nuevos_datos.values()):
        raise ValueError("Error: Algunos campos en 'nuevos_datos' están vacíos o el ID no es válido.")

    conn = co.obtener_conexion()
    if conn is None:
        raise ValueError("Error: No se pudo establecer la conexión con la base de datos.")

    try:
        cursor = conn.cursor()
        query = """
        UPDATE productos
        SET Nombre_pr = %s, Descripcion_pr = %s, Precio_pr = %s, Stock_pr = %s,
            Categoria_pr = %s, Proveedor_pr = %s, codigo_barras_pr = %s, codigo_producto_pr = %s
        WHERE ID_pr = %s
        """
        values = (
            nuevos_datos["nombre"], nuevos_datos["descripcion"], nuevos_datos["precio"], nuevos_datos["stock"],
            nuevos_datos["categoria"], nuevos_datos["proveedor"], nuevos_datos["codigo_barras"], nuevos_datos["codigo_producto"], id_producto
        )
        cursor.execute(query, values)
        conn.commit()
        print(f"Producto con ID {id_producto} modificado correctamente.")
    except Exception as e:
        print(f"Error al modificar el producto: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def eliminar_producto(id_producto):
    """
    Elimina un producto de la base de datos.
    :param id_producto: ID del producto a eliminar.
    """
    conn = co.obtener_conexion()  # Obtiene la conexión
    try:
        cursor = conn.cursor()
        query = "DELETE FROM productos WHERE ID_pr = %s"
        cursor.execute(query, (id_producto,))
        conn.commit()  # Confirmar los cambios
        print(f"Producto con ID {id_producto} eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar el producto: {e}")
    finally:
        cursor.close()
        conn.close()