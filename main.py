import customtkinter as ctk
from PIL import Image, ImageOps, ImageDraw
import ui.login




def main():

    ventana = ctk.CTk()
    ventana.title("Abarrotes Gael")
    ventana.geometry("1920x1080")  # Tamaño de la ventana
    ventana.configure(fg_color="#fcf3cf") 
    ventana.attributes('-fullscreen', True)
    ui.login.ventana_login(ventana)

    # Iniciar la ventana principal
    ventana.mainloop()

if __name__ == "__main__":
    main()

