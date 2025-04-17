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
        return conexion
    else:
        return None

# Uso de la función
conexion = obtener_conexion()



def guardar_factura(id_ticket, datos_fiscales):
    """
    Guarda los datos fiscales de una factura en la tabla facturas.
    Args:
        id_ticket: ID del ticket asociado a la factura
        datos_fiscales: Diccionario con los datos fiscales
    Returns:
        id_factura: ID de la factura generada
    """
    conn = obtener_conexion()
    if conn is None:
        return None
    
    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO facturas (
            ID_ti_fa, Fecha_Emision_fa, Metodo_Pago_fa, 
            Total_fa, Estado_fa, RFC_Receptor_fa, 
            Direccion_Receptor_fa, Codigo_Postal_Receptor_fa,
            Forma_Pago_fa, Uso_CFDI_fa
        ) VALUES (
            %s, NOW(), %s, 
            %s, 'ACTIVA', %s, 
            %s, %s, 
            %s, %s
        )
        """
        values = (
            id_ticket,
            datos_fiscales.get('metodo_pago', 'Efectivo'),
            datos_fiscales.get('total', 0.0),
            datos_fiscales.get('rfc', ''),
            datos_fiscales.get('direccion', ''),
            datos_fiscales.get('codigo_postal', ''),
            datos_fiscales.get('forma_pago', '01'),  # 01 = Efectivo
            datos_fiscales.get('uso_cfdi', 'G01')    # G01 = Adquisición de mercancías
        )
        
        cursor.execute(query, values)
        conn.commit()
        return cursor.lastrowid
        
    except Exception as e:
        print(f"Error al guardar factura: {e}")
        conn.rollback()
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def obtener_datos_factura(id_factura):
    """
    Obtiene los datos de una factura específica.
    Args:
        id_factura: ID de la factura
    Returns:
        datos: Diccionario con los datos de la factura
    """
    conn = obtener_conexion()
    if conn is None:
        return None
    
    try:
        cursor = conn.cursor(dictionary=True)
        query = """
        SELECT * FROM facturas WHERE ID_fa = %s
        """
        cursor.execute(query, (id_factura,))
        return cursor.fetchone()
        
    except Exception as e:
        print(f"Error al obtener datos de factura: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
