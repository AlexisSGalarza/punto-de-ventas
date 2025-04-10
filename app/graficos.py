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
            ID_tr_ti AS TrabajadorID, 
            COUNT(*) AS TotalVentas,
            SUM(Total_ti) AS TotalIngresos
        FROM 
            ticket
        WHERE 
            Estado_ti = 'Completado'
        GROUP BY 
            ID_tr_ti
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
            ID_pr_dv AS ProductoID, 
            SUM(Cantidad_dv) AS CantidadVendida
        FROM 
            detalles_venta
        GROUP BY 
            ID_pr_dv
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