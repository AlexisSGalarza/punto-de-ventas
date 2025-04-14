import db.conexion as co
from datetime import datetime

def obtener_productos(busqueda=None):
    conn = co.obtener_conexion()
    if conn is None:
        return []
    
    try:
        cursor = conn.cursor(dictionary=True)
        if busqueda:
            # Buscar por nombre o código de barras
            query = """
            SELECT ID_pr as 'No.', Nombre_pr as 'Producto', codigo_barras_pr as 'CodigoBarras', 
                   Precio_pr as 'Precio', Stock_pr as 'Stock'
            FROM productos 
            WHERE Nombre_pr LIKE %s OR codigo_barras_pr LIKE %s
            """
            cursor.execute(query, (f'%{busqueda}%', f'%{busqueda}%'))
        else:
            # Obtener todos los productos
            query = """
            SELECT ID_pr as 'No.', Nombre_pr as 'Producto', codigo_barras_pr as 'CodigoBarras', 
                   Precio_pr as 'Precio', Stock_pr as 'Stock'
            FROM productos
            """
            cursor.execute(query)
        
        productos = cursor.fetchall()
        return productos
        
    except Exception as e:
        print(f"Error al obtener productos: {e}")
        return []
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def crear_venta(id_cliente, id_trabajador, total, items):
    conn = co.obtener_conexion()
    if conn is None:
        return None
    
    try:
        cursor = conn.cursor()
        
        # Iniciar transacción
        conn.start_transaction()
        
        # Calcular total con impuestos
        total_con_impuestos = total * 1.16

        # Insertar ticket con total con impuestos
        query_ticket = """
        INSERT INTO tickets  (ID_cl_ti, ID_tr_ti, Total_ti, Estado_ti)
        VALUES (%s, %s, %s, 'Completado')
        """
        cursor.execute(query_ticket, (id_cliente, id_trabajador, total_con_impuestos))
        id_ticket = cursor.lastrowid
        
        # Insertar detalles de venta y actualizar stock
        for item in items:
            # Obtener el precio unitario del producto (quitando el símbolo $)
            precio_unitario = float(item['Precio'].replace('$', ''))
            subtotal = precio_unitario * item['Cantidad']

            # Insertar detalle de venta con precio unitario y subtotal
            query_detalle = """
            INSERT INTO detalles_venta (ID_ti_dv, ID_pr_dv, Cantidad_dv, Precio_Unitario_dv, Subtotal_dv)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query_detalle, (id_ticket, item['No.'], item['Cantidad'], precio_unitario, subtotal))
            
            # Actualizar stock
            query_stock = """
            UPDATE productos 
            SET Stock_pr = Stock_pr - %s
            WHERE ID_pr = %s
            """
            cursor.execute(query_stock, (item['Cantidad'], item['No.']))
        
        # Confirmar transacción
        conn.commit()
        return id_ticket  # Devolver el ID del ticket creado
        
    except Exception as e:
        # Revertir cambios en caso de error
        conn.rollback()
        print(f"Error al crear venta: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def obtener_ultimo_numero_venta():
    """Obtiene el ID del último ticket insertado."""
    conn = co.obtener_conexion()
    if conn is None:
        return None
    
    try:
        cursor = conn.cursor()
        query = "SELECT ID_ti FROM tickets ORDER BY ID_ti DESC LIMIT 1"
        cursor.execute(query)
        resultado = cursor.fetchone()
        return resultado[0] if resultado else None
    except Exception as e:
        print(f"Error al obtener último número de venta: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()