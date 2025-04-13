import db.conexion as co
import app.Productos as productos
import mysql.connector
from db.conexion import obtener_conexion
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime
import os

class CarritoCompras:
    def __init__(self):
        self.items = {}  # Diccionario para almacenar {id_producto: cantidad}
        self.total = 0.0
    def agregar_producto(self, id_producto, cantidad=1):
        """Agrega un producto al carrito."""
        producto = productos.obtener_producto_por_id(id_producto)
        if not producto:
            raise ValueError(f"Producto con ID {id_producto} no encontrado.")
        
        if int(producto['Stock_pr']) < cantidad:
            raise ValueError(f"Stock insuficiente. Solo hay {producto['Stock_pr']} unidades disponibles.")
        
        if id_producto in self.items:
            self.items[id_producto] += cantidad
        else:
            self.items[id_producto] = cantidad
        
        self.total += float(producto['Precio_pr']) * cantidad

    def remover_producto(self, id_producto, cantidad=1):
        """Remueve una cantidad específica de un producto del carrito."""
        if id_producto not in self.items:
            raise ValueError("Producto no está en el carrito.")
        
        producto = productos.obtener_producto_por_id(id_producto)
        if not producto:
            raise ValueError(f"Producto con ID {id_producto} no encontrado.")
        
        if cantidad >= self.items[id_producto]:
            # Remover el producto completamente
            self.total -= float(producto['Precio_pr']) * self.items[id_producto]
            del self.items[id_producto]
        else:
            # Reducir la cantidad
            self.items[id_producto] -= cantidad
            self.total -= float(producto['Precio_pr']) * cantidad

    def obtener_total(self):
        """Retorna el total actual del carrito."""
        return self.total

    def obtener_items(self):
        """Retorna los items en el carrito con sus detalles."""
        items_detallados = []
        for id_producto, cantidad in self.items.items():
            producto = productos.obtener_producto_por_id(id_producto)
            if producto:
                items_detallados.append({
                    'id': id_producto,
                    'nombre': producto['Nombre_pr'],
                    'precio_unitario': producto['Precio_pr'],
                    'cantidad': cantidad,
                    'subtotal': float(producto['Precio_pr']) * cantidad
                })
        return items_detallados

    def vaciar_carrito(self):
        """Vacía el carrito de compras."""
        self.items.clear()
        self.total = 0.0

def guardar_ticket(id_trabajador, id_cliente, total, carrito):
    """Guarda el ticket y los detalles de la venta en la base de datos."""
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Insertar en la tabla tickets
        query_ticket = """
            INSERT INTO tickets (ID_cl, ID_tr, Fecha_Hora_ti, Total_ti)
            VALUES (%s, %s, NOW(), %s)
        """
        valores_ticket = (id_cliente, id_trabajador, total)
        cursor.execute(query_ticket, valores_ticket)
        id_ticket = cursor.lastrowid  # Obtener el ID del ticket generado

        # Insertar en la tabla detalles_venta
        for producto in carrito:
            query_detalle = """
                INSERT INTO detalles_venta (ID_ti, ID_pr, Cantidad_dv, Precio_Unitario_dv, Subtotal_dv)
                VALUES (%s, %s, %s, %s, %s)
            """
            valores_detalle = (
                id_ticket,
                producto["No."],
                producto["Cantidad"],
                float(producto["Precio"].replace("$", "")),
                float(producto["Subtotal"].replace("$", ""))
            )
            cursor.execute(query_detalle, valores_detalle)

        conexion.commit()
        return id_ticket
    except Exception as e:
        print(f"Error al guardar el ticket: {e}")
        conexion.rollback()
        raise
    finally:
        conexion.close()

def generar_ticket(id_ticket, detalles, total, vendedor):
    """Genera un ticket en formato PDF con detalles profesionales."""
    # Crear directorio de tickets si no existe
    if not os.path.exists('tickets'):
        os.makedirs('tickets')

    # Generar nombre del archivo con fecha y hora
    fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f'tickets/ticket_{id_ticket}_{fecha_hora}.pdf'

    # Crear el PDF
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    width, height = letter

    # Encabezado
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "TIENDA DE ABARROTES")
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 70, "Dirección: Calle Principal #123")
    c.drawString(50, height - 85, f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    c.drawString(50, height - 100, f"Vendedor: {vendedor}")

    # Línea separadora
    c.line(50, height - 110, width - 50, height - 110)

    # Detalles de la venta
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 130, "DETALLES DE LA VENTA")
    c.setFont("Helvetica", 10)

    y = height - 150
    c.drawString(50, y, "Producto")
    c.drawString(200, y, "Cantidad")
    c.drawString(300, y, "Precio Unitario")
    c.drawString(450, y, "Subtotal")
    y -= 20

    for detalle in detalles:
        c.drawString(50, y, detalle['Producto'])
        c.drawString(200, y, str(detalle['Cantidad']))
        c.drawString(300, y, f"${float(detalle['Precio'].replace('$', '')):.2f}")
        c.drawString(450, y, f"${float(detalle['Subtotal'].replace('$', '')):.2f}")
        y -= 20

    # Calcular impuestos
    impuesto = total * 0.16
    total_con_impuestos = total + impuesto

    # Mostrar totales
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y - 20, f"Subtotal: ${total:.2f}")
    c.drawString(50, y - 40, f"IVA (16%): ${impuesto:.2f}")
    c.drawString(50, y - 60, f"TOTAL: ${total_con_impuestos:.2f}")

    # Pie de página
    c.setFont("Helvetica", 8)
    c.drawString(50, 50, "¡Gracias por su compra!")
    c.drawString(50, 40, "Vuelva pronto")

    # Guardar el PDF
    c.save()

    print(f"Ticket generado: {nombre_archivo}")

