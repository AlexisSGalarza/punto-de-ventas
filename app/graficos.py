import mysql.connector
import pandas as pd
import db.conexion as co  # Usa tu módulo de conexión existente

def obtener_ventas_por_trabajador():
    """Consulta el número de ventas y los ingresos totales por trabajador."""
    conn = co.obtener_conexion()  # Conexión utilizando tu módulo de conexión
    if conn is None:
        print("No se pudo establecer conexión con la base de datos.")
        return None
    try:
        query = """
        SELECT 
            t.Nombre_tr AS Trabajador,  -- Obtenemos el nombre del trabajador desde la tabla trabajadores
            COUNT(*) AS TotalVentas,
            SUM(ti.Total_ti) AS TotalIngresos
        FROM 
            tickets ti
        JOIN 
            trabajadores t ON ti.ID_tr_ti = t.ID_tr  -- Relacionamos tickets con trabajadores
        WHERE 
            ti.Estado_ti = 'Completado'
        GROUP BY 
            t.Nombre_tr
        ORDER BY 
            TotalVentas DESC;
        """
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        resultados = cursor.fetchall()
        return pd.DataFrame(resultados)  # Convierte resultados en un DataFrame
    except mysql.connector.Error as e:
        print(f"Error al consultar la base de datos: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def obtener_productos_mas_vendidos():
    """Consulta los productos más vendidos desde la tabla detalles_venta."""
    conn = co.obtener_conexion()  # Conexión utilizando tu módulo de conexión
    if conn is None:
        print("No se pudo establecer conexión con la base de datos.")
        return None
    try:
        query = """
        SELECT 
            p.Nombre_pr AS Producto,  -- Obtenemos el nombre del producto desde la tabla productos
            SUM(dv.Cantidad_dv) AS CantidadVendida
        FROM 
            detalles_venta dv
        JOIN 
            productos p ON dv.ID_pr_dv = p.ID_pr  -- Relacionamos detalles_venta con productos
        GROUP BY 
            p.Nombre_pr
        ORDER BY 
            CantidadVendida DESC
        LIMIT 
            10;  -- Limita a los 10 productos más vendidos
        """
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        resultados = cursor.fetchall()
        return pd.DataFrame(resultados)  # Convierte resultados en un DataFrame
    except mysql.connector.Error as e:
        print(f"Error al consultar la base de datos: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def obtener_productos_bajo_stock(umbral=10):
    """Consulta los productos con stock por debajo de un umbral."""
    conn = co.obtener_conexion()
    if conn is None:
        print("No se pudo establecer conexión con la base de datos.")
        return None
    try:
        query = """
        SELECT 
            ID_pr AS ID, 
            Nombre_pr AS Nombre, 
            Stock_pr AS Stock
        FROM 
            productos
        WHERE 
            Stock_pr < %s
        ORDER BY 
            Stock_pr ASC;
        """
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (umbral,))
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as e:
        print(f"Error al consultar la base de datos: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def obtener_ventas_por_categoria():
    """Consulta las ventas agrupadas por categoría de producto."""
    conn = co.obtener_conexion()
    if conn is None:
        print("No se pudo establecer conexión con la base de datos.")
        return None
    try:
        query = """
        SELECT 
            c.Nombre_cat AS Categoria, 
            SUM(dv.Cantidad_dv * p.Precio_pr) AS TotalVentas
        FROM 
            detalles_venta dv
        JOIN 
            productos p ON dv.ID_pr_dv = p.ID_pr
        JOIN 
            categorias c ON p.ID_cat_pr = c.ID_cat
        GROUP BY 
            c.Nombre_cat
        ORDER BY 
            TotalVentas DESC;
        """
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as e:
        print(f"Error al consultar la base de datos: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def obtener_clientes_frecuentes():
    """Consulta los clientes con más compras realizadas."""
    conn = co.obtener_conexion()
    if conn is None:
        print("No se pudo establecer conexión con la base de datos.")
        return None
    try:
        query = """
        SELECT 
            c.ID_cl AS IDCliente, 
            c.Nombre_cl AS Nombre, 
            COUNT(t.ID_cl_ti) AS ComprasRealizadas
        FROM 
            tickets t
        JOIN 
            clientes c ON t.ID_cl_ti = c.ID_cl
        WHERE 
            t.Estado_ti = 'Completado'
        GROUP BY 
            c.ID_cl, c.Nombre_cl
        ORDER BY 
            ComprasRealizadas DESC
        LIMIT 10;
        """
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as e:
        print(f"Error al consultar la base de datos: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()