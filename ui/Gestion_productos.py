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