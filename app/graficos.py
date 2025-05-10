import mysql.connector
import pandas as pd
from datetime import datetime, timedelta
import db.conexion as co

def obtener_tendencias_ventas():
    """Consulta las ventas diarias y semanales."""
    conn = co.obtener_conexion()
    if conn is None:
        print("No se pudo establecer conexión con la base de datos.")
        return None
    try:
        query = """
        SELECT 
            DATE(Fecha_Hora_ti) as Fecha,
            SUM(Total_ti) as TotalVentas,
            COUNT(*) as NumeroVentas,
            AVG(Total_ti) as TicketPromedio
        FROM 
            tickets
        WHERE 
            Estado_ti = 'Completado'
            AND Fecha_Hora_ti >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY)
        GROUP BY 
            DATE(Fecha_Hora_ti)
        ORDER BY 
            Fecha DESC;
        """
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
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

def obtener_ventas_por_trabajador():
    """Obtiene estadísticas detalladas de ventas por trabajador."""
    conn = co.obtener_conexion()
    if conn is None:
        print("No se pudo establecer conexión con la base de datos.")
        return None
    try:
        query = """
        SELECT 
            CONCAT(t.Nombre_tr, ' ', t.Apellido_tr) as Trabajador,
            DATE(ti.Fecha_Hora_ti) as Fecha,
            COUNT(DISTINCT ti.ID_ti) as NumVentas,
            SUM(ti.Total_ti) as TotalVentas,
            AVG(ti.Total_ti) as PromedioVenta,
            COUNT(DISTINCT ti.ID_cl_ti) as NumClientes,
            SUM(dv.Cantidad_dv) as ProductosVendidos
        FROM 
            tickets ti
            JOIN trabajadores t ON ti.ID_tr_ti = t.ID_tr
            LEFT JOIN detalles_venta dv ON ti.ID_ti = dv.ID_ti_dv
        WHERE 
            ti.Estado_ti = 'Completado'
            AND ti.Fecha_Hora_ti >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY)
        GROUP BY 
            t.ID_tr, DATE(ti.Fecha_Hora_ti)
        ORDER BY 
            Fecha DESC, TotalVentas DESC;
        """
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al consultar la base de datos: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def obtener_ventas_por_hora():
    """Obtiene estadísticas detalladas de ventas por hora del día."""
    conn = co.obtener_conexion()
    if conn is None:
        print("No se pudo establecer conexión con la base de datos.")
        return None
    try:
        query = """
        SELECT 
            DATE(t.Fecha_Hora_ti) as Fecha,
            HOUR(t.Fecha_Hora_ti) as Hora,
            COUNT(t.ID_ti) as NumTransacciones,
            SUM(t.Total_ti) as TotalVentas, 
            AVG(t.Total_ti) as TicketPromedio,
            COUNT(DISTINCT t.ID_cl_ti) as NumClientes,
            SUM(dv.Cantidad_dv) as ProductosVendidos
        FROM 
            tickets t
            LEFT JOIN detalles_venta dv ON t.ID_ti = dv.ID_ti_dv
        WHERE 
            t.Estado_ti = 'Completado'
            AND t.Fecha_Hora_ti >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY)
        GROUP BY 
            DATE(t.Fecha_Hora_ti),
            HOUR(t.Fecha_Hora_ti)
        ORDER BY 
            Fecha DESC, Hora ASC;
        """
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al consultar la base de datos: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()