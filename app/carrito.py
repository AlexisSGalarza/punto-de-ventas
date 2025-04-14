import db.conexion as co
import app.Productos as productos
import mysql.connector
from db.conexion import obtener_conexion
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from datetime import datetime
import os
import ui.ventas as ventas  # Importando el módulo ventas
import app.clientes as db

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
    """
    Guarda la venta y sus detalles en la base de datos.
    Args:
        id_trabajador: ID del trabajador que realiza la venta
        id_cliente: ID del cliente (puede ser None)
        total: Total de la venta
        carrito: Lista de productos en el carrito
    Returns:
        id_venta: ID de la venta generada
    """
    try:
        # Formatear los items del carrito para mantener los precios unitarios y subtotales
        items_formateados = []
        for producto in carrito:
            precio_unitario = float(producto["Precio"].replace("$", ""))
            subtotal = precio_unitario * producto["Cantidad"]
            items_formateados.append({
                "No.": producto["No."],
                "Precio": producto["Precio"],
                "Cantidad": producto["Cantidad"],
                "Subtotal": f"${subtotal:.2f}"
            })

        # Usar el método crear_venta de ventas.py con los items formateados
        exito = ventas.crear_venta(id_cliente, id_trabajador, total, items_formateados)
        
        if not exito:
            raise Exception("No se pudo crear la venta")
            
        # Obtener el ID del último ticket creado
        ultimo_id = ventas.obtener_ultimo_numero_venta()
        return ultimo_id
        
    except Exception as e:
        print(f"Error al guardar el ticket: {e}")
        raise

def generar_ticket(id_ticket, detalles, total, vendedor, es_factura=False, id_cliente=None):
    """
    Genera un PDF del ticket o factura con los colores corporativos.
    Args:
        id_ticket: ID del ticket
        detalles: Lista de productos vendidos
        total: Total de la venta
        vendedor: Nombre del vendedor
        es_factura: Si es True, incluye datos fiscales
        id_cliente: ID del cliente (requerido si es_factura es True)
    """
    if not detalles:
        print("Error: La lista de detalles está vacía.")
        return

    try:
        # Crear directorio de tickets si no existe
        if not os.path.exists('tickets'):
            os.makedirs('tickets')

        # Generar nombre del archivo
        fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f'tickets/{"factura" if es_factura else "ticket"}_{fecha_hora}.pdf'

        # Crear el PDF
        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        width, height = letter

        # Definir colores corporativos
        color_amarillo = colors.HexColor('#f4d03f')
        color_rojo = colors.HexColor('#f11919')

        # Fondo decorativo superior
        c.setFillColor(color_amarillo)
        c.rect(0, height-120, width, 120, fill=True)
        c.setFillColor(colors.black)

        # Logo y encabezado centrado
        c.setFont("Helvetica-Bold", 24)
        titulo = "TIENDA DE ABARROTES GAEL"
        titulo_width = c.stringWidth(titulo, "Helvetica-Bold", 24)
        c.setFillColor(color_rojo)
        c.drawString((width - titulo_width) / 2, height - 50, titulo)
        
        # Líneas decorativas
        c.setStrokeColor(color_rojo)
        c.setLineWidth(3)
        c.line(50, height - 65, width-50, height - 65)
        c.setLineWidth(1)
        c.line(100, height - 70, width-100, height - 70)
        
        # Información del negocio centrada
        c.setFont("Helvetica", 12)
        c.setFillColor(colors.black)
        direccion = "Real de Cadereyta #1009, Cadereyta Jiménez, N.L."
        dir_width = c.stringWidth(direccion, "Helvetica", 12)
        c.drawString((width - dir_width) / 2, height - 85, direccion)
        
        telefono = "Tel: (828) 123-4567"
        tel_width = c.stringWidth(telefono, "Helvetica", 12)
        c.drawString((width - tel_width) / 2, height - 100, telefono)

        # Marco principal del documento
        c.setStrokeColor(color_rojo)
        c.setLineWidth(2)
        c.roundRect(40, 30, width-80, height-150, 10)
        
        # Información de la transacción
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(color_rojo)
        c.drawString(60, height - 140, f"Ticket #{id_ticket}")
        
        # Fecha y vendedor en columnas
        c.setFont("Helvetica", 11)
        c.setFillColor(colors.black)
        fecha = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        c.drawString(60, height - 160, f"Fecha: {fecha}")
        c.drawString(width-220, height - 160, f"Vendedor: {vendedor}")

        # Si es factura, agregar datos fiscales con diseño mejorado
        if es_factura and id_cliente:
            try:
                datos_cliente = db.obtener_cliente_por_id(id_cliente)
                if datos_cliente:
                    # Marco elegante para datos fiscales
                    c.setFillColor(color_amarillo.clone(alpha=0.3))
                    c.roundRect(50, height - 280, width-100, 100, 10, fill=True)
                    
                    # Título datos fiscales con fondo rojo
                    c.setFillColor(color_rojo)
                    c.rect(50, height - 200, 120, 20, fill=True)
                    c.setFillColor(colors.white)
                    c.setFont("Helvetica-Bold", 12)
                    c.drawString(60, height - 195, "DATOS FISCALES")
                    
                    # Información fiscal
                    c.setFillColor(colors.black)
                    c.setFont("Helvetica", 11)
                    nombre_completo = f"{datos_cliente['Nombre_cl']} {datos_cliente['Apellido_cl']}"
                    
                    # Organizar datos fiscales en dos columnas
                    col1_x = 60
                    col2_x = width/2 + 30
                    base_y = height - 230
                    
                    c.drawString(col1_x, base_y, f"Cliente: {nombre_completo}")
                    c.drawString(col2_x, base_y, f"RFC: {datos_cliente['RFC_cl']}")
                    c.drawString(col1_x, base_y - 20, f"Dirección: {datos_cliente['Direccion_cl']}")
                    c.drawString(col2_x, base_y - 20, f"C.P.: {datos_cliente['Codigo_Postal_cl']}")
                    
                    # Guardar datos fiscales y obtener el ID de factura
                    datos_fiscales = {
                        'metodo_pago': 'Efectivo',
                        'total': total,
                        'rfc': datos_cliente['RFC_cl'],
                        'direccion': datos_cliente['Direccion_cl'],
                        'codigo_postal': datos_cliente['Codigo_Postal_cl']
                    }
                    id_factura = co.guardar_factura(id_ticket, datos_fiscales)
                    
                    # Agregar número de factura en la parte superior
                    c.setFillColor(color_rojo)
                    c.setFont("Helvetica-Bold", 14)
                    c.drawString(width-220, height - 140, f"Factura #{id_factura}")
                    
            except Exception as e:
                print(f"Error al procesar datos fiscales: {e}")

        # Tabla de productos con diseño mejorado
        y = height - (320 if es_factura else 220)
        
        # Encabezado de tabla con color rojo corporativo
        c.setFillColor(color_rojo)
        c.roundRect(45, y, width-90, 25, 5, fill=True)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 12)
        
        # Centrar textos en columnas
        cols = [
            (50, "Producto", 180),
            (240, "Cantidad", 70),
            (320, "Precio Unit.", 90),
            (420, "Subtotal", 90)
        ]
        
        for x, texto, ancho in cols:
            texto_width = c.stringWidth(texto, "Helvetica-Bold", 12)
            c.drawString(x + (ancho - texto_width)/2, y+7, texto)
        
        # Detalles de productos
        c.setFillColor(colors.black)
        c.setFont("Helvetica", 10)
        y -= 30
        
        # Alternar colores de fondo para las filas
        for i, detalle in enumerate(detalles):
            if y < 120:  # Nueva página si no hay espacio
                c.showPage()
                c.setFont("Helvetica", 10)
                y = height - 50
            
            # Fondo alternado para las filas
            if i % 2 == 0:
                c.setFillColor(color_amarillo.clone(alpha=0.1))
                c.rect(45, y-5, width-90, 20, fill=True)
            c.setFillColor(colors.black)
            
            # Alinear datos en las columnas
            producto = detalle['Producto'][:30]
            cantidad = str(detalle['Cantidad'])
            precio = float(detalle['Precio'].replace('$', ''))
            subtotal = float(detalle['Subtotal'].replace('$', ''))
            
            c.drawString(50, y, producto)
            c.drawString(240 + (70 - c.stringWidth(cantidad, "Helvetica", 10))/2, y, cantidad)
            c.drawString(320 + (90 - c.stringWidth(f"${precio:.2f}", "Helvetica", 10))/2, y, f"${precio:.2f}")
            c.drawString(420 + (90 - c.stringWidth(f"${subtotal:.2f}", "Helvetica", 10))/2, y, f"${subtotal:.2f}")
            
            y -= 25

        # Totales con diseño elegante usando el color rojo corporativo
        c.setFillColor(color_rojo)
        c.roundRect(width-250, y-80, 200, 75, 5, fill=True)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 12)
        
        # Alinear totales a la derecha
        iva = total * 0.16
        total_con_iva = total + iva
        right_x = width-70
        
        c.drawRightString(right_x, y-20, f"Subtotal: ${total:.2f}")
        c.drawRightString(right_x, y-40, f"IVA (16%): ${iva:.2f}")
        c.drawRightString(right_x, y-60, f"Total: ${total_con_iva:.2f}")

        # Pie de página elegante con color rojo corporativo
        c.setFillColor(color_rojo)
        c.rect(0, 0, width, 80, fill=True)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 10)
        mensaje = "¡Gracias por su compra!"
        msg_width = c.stringWidth(mensaje, "Helvetica-Bold", 10)
        c.drawString((width - msg_width) / 2, 60, mensaje)
        
        c.setFont("Helvetica", 8)
        submensaje = "Este documento es un comprobante oficial de su compra"
        sub_width = c.stringWidth(submensaje, "Helvetica", 8)
        c.drawString((width - sub_width) / 2, 45, submensaje)
        
        # QR Code con borde rojo
        c.setStrokeColor(color_rojo)
        c.roundRect(width-90, 20, 60, 60, 5)
        
        c.save()
        print(f"Archivo PDF generado exitosamente: {nombre_archivo}")

        # Abrir el PDF
        if os.path.exists(nombre_archivo):
            try:
                edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
                if not os.path.exists(edge_path):
                    edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
                if os.path.exists(edge_path):
                    os.system(f'"{edge_path}" "{os.path.abspath(nombre_archivo)}"')
            except Exception as e:
                print(f"Error al abrir el PDF: {e}")
    except Exception as e:
        print(f"Error al generar el PDF: {e}")


