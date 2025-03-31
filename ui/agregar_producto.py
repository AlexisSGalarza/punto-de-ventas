import customtkinter as ctk
from PIL import Image, ImageDraw

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
    # Encabezado principal
    encabezado = ctk.CTkFrame(ventana, fg_color="#f4d03f", height=100)
    encabezado.grid(row=0, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

    franja_roja = ctk.CTkFrame(encabezado, fg_color="#f11919", height=20)
    franja_roja.grid(row=1, column=0, columnspan=3, sticky="ew")
    
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=1)
    ventana.grid_columnconfigure(2, weight=1)
    
    logo_imagen = Image.open("assets/logo.jpg")
    logo_imagen_redondeada = redondear_bordes(logo_imagen, radio=75)
    logo_imagen_ctk = ctk.CTkImage(logo_imagen_redondeada, size=(100, 100))
    
    logo = ctk.CTkLabel(encabezado, image=logo_imagen_ctk, text="")
    logo.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    
    texto_encabezado = ctk.CTkLabel(
        encabezado,
        text="Tienda 'Abarrotes Gael'",
        font=("Arial", 50, "bold"),
        text_color="black"
    )
    texto_encabezado.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    encabezado.grid_columnconfigure(1, weight=1)

def crear_producto(ventana):
    """Crea un cuadro blanco centrado que contenga los campos para ingresar los datos de un producto."""
    # Crear el cuadro blanco centrado (tamaño mediano)
    cuadro_blanco = ctk.CTkFrame(ventana, fg_color="#a9cce3", corner_radius=30, width=1000, height=700)
    cuadro_blanco.place(relx=0.5, rely=0.5, anchor="center")

    
    titulo = ctk.CTkLabel(cuadro_blanco, text="Agregar Producto", font=("Arial", 32, "bold"), text_color="black")
    titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="n")
    
    # Configurar las columnas del cuadro blanco para distribuir los widgets
    cuadro_blanco.grid_columnconfigure(0, weight=1)
    cuadro_blanco.grid_columnconfigure(1, weight=2)
    
    # Campo: Código del producto
    etiqueta_codigo = ctk.CTkLabel(cuadro_blanco, text="Código:", font=("Arial", 20), text_color="black")
    etiqueta_codigo.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_codigo = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
    entry_codigo.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    
    # Campo: Nombre del producto
    etiqueta_nombre = ctk.CTkLabel(cuadro_blanco, text="Nombre:", font=("Arial", 20), text_color="black")
    etiqueta_nombre.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_nombre = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
    entry_nombre.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
    
    # Campo: Precio del producto
    etiqueta_Categoría= ctk.CTkLabel(cuadro_blanco, text="Categoría:", font=("Arial", 20), text_color="black")
    etiqueta_Categoría.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    entry_Categoría = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
    entry_Categoría.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    etiqueta_Proveedor = ctk.CTkLabel(cuadro_blanco, text="Proveedor:", font=("Arial", 20), text_color="black")
    etiqueta_Proveedor.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    entry_Proveedor = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
    entry_Proveedor.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    etiqueta_Stock = ctk.CTkLabel(cuadro_blanco, text="Precio unitario :", font=("Arial", 20), text_color="black")
    etiqueta_Stock.grid(row=5, column=0, padx=10, pady=10, sticky="w")
    entry_Stock = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
    entry_Stock.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    etiqueta_precio = ctk.CTkLabel(cuadro_blanco, text="Precio unitario :", font=("Arial", 20), text_color="black")
    etiqueta_precio.grid(row=6, column=0, padx=10, pady=10, sticky="w")
    entry_precio = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
    entry_precio.grid(row=6, column=1, padx=10, pady=10, sticky="ew")
    
    # Campo: Descripción (con múltiples líneas)
    etiqueta_descripcion = ctk.CTkLabel(cuadro_blanco, text="Descripción:", font=("Arial", 20), text_color="black")
    etiqueta_descripcion.grid(row=7, column=0, padx=10, pady=10, sticky="nw")
    text_descripcion = ctk.CTkTextbox(cuadro_blanco, width=600, height=250, font=("Arial", 18), fg_color="white", text_color="black")
    text_descripcion.grid(row=7, column=1, padx=10, pady=10, sticky="ew")
    
    # Configurar la fila 5 para los botones (se expandirá uniformemente)
    cuadro_blanco.grid_rowconfigure(8, weight=1)
    
    # Botón Aceptar
    boton_aceptar = ctk.CTkButton(
        cuadro_blanco,
        text="Aceptar",
        font=("Arial", 20, "bold"),
        fg_color="#28a745",  # Verde
        text_color="white",
        height=40,
        command=lambda: print(
            "Producto agregado:",
            entry_codigo.get(),
            entry_nombre.get(),
            entry_precio.get(),
            text_descripcion.get("1.0", "end").strip()
        )
    )
    boton_aceptar.grid(row=9, column=0, padx=10, pady=20, sticky="ew")
    
    # Botón Cancelar
    boton_cancelar = ctk.CTkButton(
        cuadro_blanco,
        text="Cancelar",
        font=("Arial", 20, "bold"),
        fg_color="#dc3545",  # Rojo
        text_color="white",
        height=40,
        command=lambda: print("Operación cancelada")
    )
    boton_cancelar.grid(row=9, column=1, padx=10, pady=20, sticky="ew")

def crear_cuadro_inferior(ventana):
    """Crea un cuadro que contenga el botón de cerrar sesión y el pie de página en una sola fila."""
    # Crear el cuadro
    cuadro_inferior = ctk.CTkFrame(ventana, fg_color="#fcf3cf", height=150, width=300)
    cuadro_inferior.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="ew")  # Coloca en la fila 2

    # Pie de página (hora y fecha)
    hora_fecha = ctk.CTkLabel(
        cuadro_inferior,
        text="07:05 p.m. - 23/03/2025",
        font=("Arial", 14, "italic"),
        text_color="black"
    )
    # Colocar la etiqueta en la columna 1 de la misma fila
    hora_fecha.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

    # Botón de cerrar sesión
    def cerrar_sesion():
        print("Has cerrado sesión.")
    boton = ctk.CTkButton(
        cuadro_inferior,
        text="Cerrar sesión",
        command=cerrar_sesion,
        fg_color="gray",
        height=50,
        text_color="black"
    )
    # Colocar el botón en la columna 0 de la fila 0
    boton.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

    # Configurar las columnas para que se expandan uniformemente
    cuadro_inferior.grid_columnconfigure(0, weight=1)
    cuadro_inferior.grid_columnconfigure(1, weight=1)

def mainagregarpro():
    ventana = ctk.CTk()
    ventana.title("Abarrotes Gael")
    ventana.geometry("1920x1080")  # Tamaño de la ventana
    ventana.configure(fg_color="#fcf3cf")
    ventana.attributes('-fullscreen', True)

    # Configurar filas para que se adapten
    ventana.grid_rowconfigure(0, weight=0)  # Encabezado
    ventana.grid_rowconfigure(1, weight=1)  # Cuadro de productos
    ventana.grid_rowconfigure(2, weight=0)  # Cuadro inferior

    encabezado(ventana)
    crear_producto(ventana)
    crear_cuadro_inferior(ventana)

    ventana.mainloop()

# Ejecutar la aplicación
if __name__ == "__main__":
    mainagregarpro()
