from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from datetime import datetime
import os

def generar_ticket_pdf(total, metodo_pago):
    # Crear directorio de tickets si no existe
    if not os.path.exists('tickets'):
        os.makedirs('tickets')
    
    # Generar nombre del archivo con fecha y hora
    fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f'tickets/ticket_{fecha_hora}.pdf'
    
    # Crear el PDF
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    width, height = letter
    
    # Configurar fuente y tamaño
    c.setFont("Helvetica-Bold", 16)
    
    # Encabezado
    c.drawString(50, height - 50, "TIENDA DE ABARROTES")
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 70, "Dirección: Calle Principal #123")
    c.drawString(50, height - 85, f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    
    # Línea separadora
    c.line(50, height - 100, width - 50, height - 100)
    
    # Detalles de la venta
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 120, "DETALLES DE LA VENTA")
    c.setFont("Helvetica", 10)
    
    # Método de pago
    c.drawString(50, height - 140, f"Método de pago: {metodo_pago.upper()}")
    
    # Total
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 160, f"TOTAL: ${total:.2f}")
    
    # Pie de página
    c.setFont("Helvetica", 8)
    c.drawString(50, 50, "¡Gracias por su compra!")
    c.drawString(50, 40, "Vuelva pronto")
    
    # Guardar el PDF
    c.save()
    
    # Abrir el PDF automáticamente
    os.startfile(nombre_archivo)
