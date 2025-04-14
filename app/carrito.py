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

def generar_ticket(id_ticket, detalles, total, vendedor):
    print("Iniciando la generación del ticket PDF...")
    print(f"ID del Ticket: {id_ticket}")
    print(f"Total: {total}, Vendedor: {vendedor}")

    if not detalles:
        print("Error: La lista de detalles está vacía. No se puede generar el ticket.")
        return

    try:
        # Ensure all required keys are present in each detail
        for detalle in detalles:
            if not all(key in detalle for key in ["Producto", "Cantidad", "Precio", "Subtotal"]):
                print(f"Error: Faltan claves en el detalle: {detalle}")
                return

        # Crear directorio de tickets si no existe
        if not os.path.exists('tickets'):
            try:
                os.makedirs('tickets')
                print("Directorio 'tickets' creado exitosamente.")
            except Exception as e:
                print(f"Error al crear el directorio 'tickets': {e}")
                return

        # Generar nombre del archivo con fecha y hora
        fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f'tickets/ticket_{fecha_hora}.pdf'
        print(f"Nombre del archivo generado: {nombre_archivo}")

        # Crear el PDF
        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        width, height = letter

        # Ruta del logo
        logo_path = os.path.join(os.path.dirname(__file__), 'assets', 'logo.jpg')
        if os.path.exists(logo_path):
            try:
                c.drawImage(logo_path, 50, height - 150, width=100, height=50)
            except Exception as e:
                print(f"Error al cargar el logo: {e}")
        else:
            print("El archivo del logo no se encuentra en la ruta especificada.")

        # Update header to be more professional
        c.setFont("Helvetica-Bold", 20)
        c.drawString(200, height - 50, "TIENDA DE ABARROTES GAEL")
        c.setFont("Helvetica", 12)
        c.drawString(200, height - 70, "Dirección: Real de Cadereyta #1009 en Cadereyta Jiménez,")
        c.drawString(200, height - 85, f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        c.drawString(200, height - 100, f"Vendedor: {vendedor}")
        # Agregar el número de ticket
        c.drawString(50, height - 100, f"Ticket #: {id_ticket}")

        # Add a decorative line below the header
        c.setStrokeColor(colors.black)
        c.setLineWidth(1)
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
        print(f"Archivo PDF guardado exitosamente: {nombre_archivo}")

        # Verificar si el archivo se generó correctamente
        if os.path.exists(nombre_archivo):
            print(f"Archivo encontrado: {nombre_archivo}")
            try:
                edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
                if not os.path.exists(edge_path):
                    edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

                if os.path.exists(edge_path):
                    os.system(f'"{edge_path}" "{os.path.abspath(nombre_archivo)}"')
                else:
                    print("Microsoft Edge no está instalado en la ruta predeterminada.")
            except Exception as e:
                print(f"Error al intentar abrir el archivo en Microsoft Edge: {e}")
        else:
            print(f"Error: El archivo {nombre_archivo} no se encuentra en el sistema.")
    except Exception as e:
        print(f"Error durante la generación del PDF: {e}")


