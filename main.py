import customtkinter as ctk
from PIL import Image, ImageOps, ImageDraw


def redondear_bordes(imagen, radio):
    mascara = Image.new("L", imagen.size, 0)
    draw = ImageDraw.Draw(mascara)
    draw.rounded_rectangle(
        (0, 0, imagen.size[0], imagen.size[1]), 
        radius=radio, fill=255
    )
    
    imagen_redondeada = imagen.convert("RGBA")
    imagen_redondeada.putalpha(mascara)
    return imagen_redondeada


def encabezado(ventana):
    encabezado = ctk.CTkFrame(ventana, fg_color="#f4d03f", height=100)
    encabezado.grid(row=0, column=0,columnspan=3, sticky="ew", padx=10, pady=10)

    # Crear la franja roja en la parte inferior del encabezado
    franja_roja = ctk.CTkFrame(encabezado, fg_color="#f11919", height=20)
    franja_roja.grid(row=1, column=0,columnspan=3, sticky="ew")
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=1)
    ventana.grid_columnconfigure(2, weight=1)
    # Logo
    logo_imagen = Image.open("assets/logo.jpg")
    logo_imagen_redondeada = redondear_bordes(logo_imagen, radio=75)  # Cambia el radio para más redondez

    # Convertir la imagen procesada para CustomTkinter
    logo_imagen_ctk = ctk.CTkImage(logo_imagen_redondeada, size=(100, 100))

    # Añadir el logo al encabezado, alineado a la izquierda
    logo = ctk.CTkLabel(encabezado, image=logo_imagen_ctk, text="")
    logo.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    # Añadir un texto o logo en el encabezado
    texto_encabezado = ctk.CTkLabel(encabezado, text="Tienda 'Abarrotes Gael'", font=("Arial", 50, "bold"), text_color="black")
    texto_encabezado.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    # Centrar el texto en la columna
    encabezado.grid_columnconfigure(1, weight=1)

def ventana_ventas(ventana):
    info_venta = ctk.CTkFrame(ventana, fg_color="#fcf3cf")  # Fondo opcional similar al encabezado
    info_venta.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

    # Configurar las filas y columnas del marco
    info_venta.grid_columnconfigure(0, weight=1)  # Columna de fecha y hora
    info_venta.grid_columnconfigure(1, weight=1)  # Columna vacía (si deseas separación)
    info_venta.grid_columnconfigure(2, weight=1)  # Columna del número de venta

    # Etiqueta para la fecha
    etiqueta_fecha = ctk.CTkLabel(
        info_venta,
        text="Fecha: 23/03/2025",
        font=("Arial", 20),
        text_color="black"
    )
    etiqueta_fecha.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    # Etiqueta para la hora
    etiqueta_hora = ctk.CTkLabel(
        info_venta,
        text="Hora: 07:05 p.m.",
        font=("Arial", 20),
        text_color="black"
    )
    etiqueta_hora.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    # Etiqueta para el número de venta
    etiqueta_numero_venta = ctk.CTkLabel(
        info_venta,
        text="No. de Venta: 0000000001",
        font=("Arial", 20, "bold"),
        text_color="black"
    )
    etiqueta_numero_venta.grid(row=0, column=2, rowspan=2, padx=10, pady=5, sticky="e")

    # Crear un marco general para los encabezados en la tabla
    cuadro_campos = ctk.CTkFrame(ventana, fg_color="#f4d03f", corner_radius=10)  # Fondo gris claro con bordes redondeados
    cuadro_campos.grid(row=2, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")

    # Configurar las columnas dentro del cuadro
    cuadro_campos.grid_columnconfigure(0, weight=1)  # No.
    cuadro_campos.grid_columnconfigure(1, weight=2)  # Producto
    cuadro_campos.grid_columnconfigure(2, weight=2)  # Código
    cuadro_campos.grid_columnconfigure(3, weight=2)  # Precio
    cuadro_campos.grid_columnconfigure(4, weight=2)  # Cantidad

    # Añadir los campos en el cuadro
    etiqueta_no = ctk.CTkLabel(cuadro_campos, text="No.", font=("Arial", 20, "bold"), text_color="black")
    etiqueta_no.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    etiqueta_producto = ctk.CTkLabel(cuadro_campos, text="Producto", font=("Arial", 20, "bold"), text_color="black")
    etiqueta_producto.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    etiqueta_codigo = ctk.CTkLabel(cuadro_campos, text="Código", font=("Arial", 20, "bold"), text_color="black")
    etiqueta_codigo.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

    etiqueta_precio = ctk.CTkLabel(cuadro_campos, text="Precio", font=("Arial", 20, "bold"), text_color="black")
    etiqueta_precio.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

    etiqueta_cantidad = ctk.CTkLabel(cuadro_campos, text="Cantidad", font=("Arial", 20, "bold"), text_color="black")
    etiqueta_cantidad.grid(row=0, column=4, padx=10, pady=10, sticky="nsew")


def main():
    # Crear la ventana principal
    ventana = ctk.CTk()
    ventana.title("Abarrotes Gael")
    ventana.geometry("1920x1080")  # Tamaño de la ventana
    ventana.configure(fg_color="#fcf3cf") 

    encabezado(ventana)
    ventana_ventas(ventana)

    # Iniciar la ventana principal
    ventana.mainloop()

if __name__ == "__main__":
    main()

