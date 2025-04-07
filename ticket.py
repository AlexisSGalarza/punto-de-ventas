from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import inch
from datetime import datetime

# Definir el tamaño personalizado para el ticket (80 mm x 150 mm)
# 80 mm = 226 puntos y 150 mm = 425 puntos
custom_size = (226, 425)

def generar_ticket_pdf(nombre_cliente, producto, precio, filename="ticket.pdf"):
    # Obtener la fecha y hora actuales
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Crear el objeto canvas con el tamaño de ticket personalizado
    c = canvas.Canvas(filename, pagesize=custom_size)
    width, height = custom_size  # Tamaño de la página personalizada

    # Título del ticket
    c.setFont("Helvetica-Bold", 12)
    c.drawString(20, height - 40, "------------------------------")
    c.drawString(20, height - 60, "        TICKET DE COMPRA       ")
    c.drawString(20, height - 80, "------------------------------")
    
    # Detalles de la compra
    c.setFont("Helvetica", 10)
    c.drawString(20, height - 120, f"Nombre del Cliente: {nombre_cliente}")
    c.drawString(20, height - 140, f"Producto: {producto}")
    c.drawString(20, height - 160, f"Precio: ${precio:.2f}")
    c.drawString(20, height - 180, f"Fecha de Compra: {fecha}")
    
    # Mensaje de agradecimiento
    c.drawString(20, height - 200, "------------------------------")
    c.drawString(20, height - 220, "      ¡Gracias por su compra!  ")
    c.drawString(20, height - 240, "------------------------------")
    
    # Guardar el PDF
    c.save()

# Datos de ejemplo
nombre_cliente = "Juan Pérez"
producto = "Camiseta"
precio = 19.99

# Generar el ticket en PDF
generar_ticket_pdf(nombre_cliente, producto, precio)
