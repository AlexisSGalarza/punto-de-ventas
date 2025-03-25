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


def main():
    # Crear la ventana principal
    ventana = ctk.CTk()
    ventana.title("Abarrotes Gael")
    ventana.geometry("1920x1080")  # Tamaño de la ventana
    ventana.configure(fg_color="#fcf3cf") 

#encabezado
    # Crear el encabezado con fondo amarillo
    encabezado = ctk.CTkFrame(ventana, fg_color="#f4d03f", height=100)
    encabezado.pack(fill="both")

    # Crear la franja roja en la parte inferior del encabezado
    franja_roja = ctk.CTkFrame(encabezado, fg_color="#f11919", height=20)
    franja_roja.pack(fill="x", side="bottom")

    logo_imagen = Image.open("assets/logo.jpg")
    logo_imagen_redondeada = redondear_bordes(logo_imagen, radio=75)  # Cambia el radio para más redondez

    # Convertir la imagen procesada para CustomTkinter
    logo_imagen_ctk = ctk.CTkImage(logo_imagen_redondeada, size=(100, 100))

    # Añadir el logo al encabezado, alineado a la izquierda
    logo = ctk.CTkLabel(encabezado, image=logo_imagen_ctk, text="")
    logo.pack(side="left", padx=10, pady=10)

    # Añadir un texto o logo en el encabezado
    texto_encabezado = ctk.CTkLabel(encabezado, text="Tienda 'Abarrotes Gael'", font=("Arial", 50, "bold"), text_color="black")
    texto_encabezado.pack(pady=20)

    


    # Iniciar la ventana principal
    ventana.mainloop()

if __name__ == "__main__":
    main()

