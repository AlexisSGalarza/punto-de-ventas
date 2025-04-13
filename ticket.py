from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from datetime import datetime
import os

def generar_ticket_pdf(total, metodo_pago, vendedor, detalles):
    print("Iniciando la generación del ticket PDF...")
    print(f"Total: {total}, Método de pago: {metodo_pago}, Vendedor: {vendedor}")
    print(f"Detalles: {detalles}")

    # Validar los detalles de la venta
    if not detalles or not isinstance(detalles, list):
        print("Error: Los detalles de la venta no son válidos o están vacíos.")
        return

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

    try:
        # Crear el PDF
        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        width, height = letter

        # Configurar fuente y tamaño
        c.setFont("Helvetica-Bold", 16)

        # Ruta del logo
        logo_path = os.path.join(os.path.dirname(__file__), 'assets', 'logo.jpg')
        print(f"Ruta del logo: {logo_path}")
        if os.path.exists(logo_path):
            try:
                c.drawImage(logo_path, 50, height - 150, width=100, height=50)
                print("Logo agregado correctamente al PDF.")
            except Exception as e:
                print(f"Error al cargar el logo: {e}")
        else:
            print("El archivo del logo no se encuentra en la ruta especificada.")

        # Encabezado
        c.drawString(50, height - 50, "TIENDA DE ABARROTES")
        c.setFont("Helvetica", 12)
        c.drawString(50, height - 70, "Dirección: Real de Cadereyta #1009 en Cadereyta Jiménez,")
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
        print(f"Archivo PDF guardado exitosamente: {nombre_archivo}")

        # Verificar si el archivo se generó correctamente
        print("Verificando si el archivo PDF se generó correctamente...")
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
