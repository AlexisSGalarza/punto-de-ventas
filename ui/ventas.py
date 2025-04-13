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
        return False
    
    try:
        cursor = conn.cursor()
        
        # Iniciar transacción
        conn.start_transaction()
        
        # Insertar ticket
        query_ticket = """
        INSERT INTO tickets  (ID_cl_ti, ID_tr_ti, Total_ti, Estado_ti)
        VALUES (%s, %s, %s, 'Completado')
        """
        cursor.execute(query_ticket, (id_cliente, id_trabajador, total))
        id_ticket = cursor.lastrowid
        
        # Insertar detalles de venta y actualizar stock
        for item in items:
            # Insertar detalle de venta
            query_detalle = """
            INSERT INTO detalles_venta (ID_ti_dv, ID_pr_dv, Cantidad_dv)
            VALUES (%s, %s, %s)
            """
            cursor.execute(query_detalle, (id_ticket, item['No.'], item['Cantidad']))
            
            # Actualizar stock
            query_stock = """
            UPDATE productos 
            SET Stock_pr = Stock_pr - %s
            WHERE ID_pr = %s
            """
            cursor.execute(query_stock, (item['Cantidad'], item['No.']))
        
        # Confirmar transacción
        conn.commit()
        return True
        
    except Exception as e:
        # Revertir cambios en caso de error
        conn.rollback()
        print(f"Error al crear venta: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def obtener_ultimo_numero_venta():

    conn = co.obtener_conexion()
    if conn is None:
        return 1
    
    try:
        cursor = conn.cursor()
        query = "SELECT MAX(ID_ti) FROM ticket"
        cursor.execute(query)
        resultado = cursor.fetchone()
        return resultado[0] + 1 if resultado[0] else 1
    except Exception as e:
        print(f"Error al obtener último número de venta: {e}")
        return 1
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close() 