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

def crear_cuadro_botones(ventana):
    """Crea un cuadro que contenga los botones de sección."""
    cuadro_botones = ctk.CTkFrame(ventana, fg_color="#e0e0e0",width=600, height=400)  # Cuadro sin tamaño fijo para expandirse dinámicamente
    cuadro_botones.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")  # Ocupa toda la pantalla

    # Botón de 'Venta'
    boton_venta = ctk.CTkButton(cuadro_botones, text="Agregar producto", width=200, height=70,corner_radius=25, fg_color="#85c1e9",text_color="black",font=("Arial", 20, "bold"))
    boton_venta.grid(row=0, column=0, padx=40, pady=30, sticky="nsew")
    
    # Botón de 'Gestión de productos'
    boton_productos = ctk.CTkButton(cuadro_botones, text="Eliminar producto", width=200, height=70,corner_radius=25, fg_color="#85c1e9",text_color="black",font=("Arial", 20, "bold"))
    boton_productos.grid(row=0, column=1, padx=40, pady=30, sticky="nsew")
    
    # Botón de 'Gestión de clientes'
    boton_clientes = ctk.CTkButton(cuadro_botones, text="Detalle de producto", width=200, height=70,corner_radius=25, fg_color="#85c1e9",text_color="black",font=("Arial", 20, "bold"))
    boton_clientes.grid(row=1, column=0, padx=40, pady=30, sticky="nsew")
    
    # Botón de 'Gestión de trabajadores'
    boton_trabajadores = ctk.CTkButton(cuadro_botones, text="Inventario", width=200, height=70, corner_radius=25, fg_color="#85c1e9",border_color="#3498db ",text_color="black",font=("Arial", 20, "bold"))
    boton_trabajadores.grid(row=1, column=1, padx=40, pady=30, sticky="nsew")

    # Configuración de las columnas y filas dentro del cuadro
    cuadro_botones.grid_rowconfigure(0, weight=1)
    cuadro_botones.grid_rowconfigure(1, weight=1)
    cuadro_botones.grid_columnconfigure(0, weight=1)
    cuadro_botones.grid_columnconfigure(1, weight=1)

    # Configuración de la ventana principal
    ventana.grid_rowconfigure(0, weight=0)  # Encabezado
    ventana.grid_rowconfigure(1, weight=1)  # Cuadro botones
    ventana.grid_rowconfigure(2, weight=0)  # Pie de página
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=1)
    ventana.grid_columnconfigure(2, weight=1)

def crear_cuadro_inferior(ventana):
    """Crea un cuadro que contenga el botón de cerrar sesión y el pie de página."""
    # Crear el cuadro
    cuadro_inferior = ctk.CTkFrame(ventana, fg_color="#f0f0f0", height=150, width=800)
    cuadro_inferior.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

    # Botón de cerrar sesión
    def Regresar():
        print("Has cerrado sesión.")
    boton = ctk.CTkButton(
        cuadro_inferior, text="Regresar", command=Regresar, fg_color="gray", height=50
    )
    boton.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

    # Pie de página
    hora_fecha = ctk.CTkLabel(
        cuadro_inferior, text="07:05 p.m. - 23/03/2025", font=("Arial", 14, "italic"), text_color="gray"
    )
    hora_fecha.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

    # Configurar el peso interno del cuadro
    cuadro_inferior.grid_rowconfigure(0, weight=1)
    cuadro_inferior.grid_rowconfigure(1, weight=1)
    cuadro_inferior.grid_columnconfigure(0, weight=1)



def main():
    """Función principal para ejecutar la aplicación."""
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    
    ventana = ctk.CTk()
    ventana.title("Mi Aplicación")
    ventana.geometry("1920x1080")

    encabezado(ventana)
    crear_cuadro_botones(ventana)
    crear_cuadro_inferior(ventana)

    ventana.mainloop()

# Ejecutar la aplicación
if __name__ == "__main__":
    main()