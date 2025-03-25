import customtkinter as ctk
from PIL import Image, ImageOps, ImageDraw
from pathlib import Path
import os

ventana = ctk.CTk()
ventana.title("login-Abarrotes Gael")
ventana.geometry("1920x1080")  
ventana.configure(fg_color="#fcf3cf")

# Crear el cuadro blanco centrado
cuadro_blanco = ctk.CTkFrame(ventana, fg_color="white", width=1400, height=700, corner_radius=15)
cuadro_blanco.place(relx=0.5, rely=0.5, anchor="center")  # Centrar el cuadro blanco


frame_logo = ctk.CTkFrame(cuadro_blanco, fg_color="white")
frame_logo.pack(side="left", padx=20, pady=20, fill="both")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, '..', 'assets', 'logo.jpg')
logo_imagen = Image.open(image_path)

# Convertir la imagen para usarla en CTkImage de customtkinter
logo_imagen_ctk = ctk.CTkImage(logo_imagen, size=(400, 400)) # Ajustar el tamaño del logo

# Etiqueta para mostrar el logo
label_logo = ctk.CTkLabel(frame_logo, image=logo_imagen_ctk, text="")
label_logo.pack(anchor="center", pady=50)  # Centrado verticalmente en el frame izquierdo

# Frame derecho para el formulario
login_frame = ctk.CTkFrame(cuadro_blanco, fg_color="white", width=900, height=700)
login_frame.pack(side="right", padx=100, pady=30, fill="both")

# Título del formulario
label_titulo = ctk.CTkLabel(login_frame, text="Iniciar Sesión", font=("Arial", 30, "bold"),text_color="black")
label_titulo.pack(pady=40)

# Campo de Usuario
label_usuario = ctk.CTkLabel(login_frame, text="Usuario:", font=("Arial", 20),text_color="black")
label_usuario.pack(pady=10)
entry_usuario = ctk.CTkEntry(login_frame, width=400, height=30, fg_color="white", border_color="#f4d03f", text_color="black" )
entry_usuario.pack(pady=10)

# Campo de Contraseña
label_contrasena = ctk.CTkLabel(login_frame, text="Contraseña:", font=("Arial", 20), text_color="black", )
label_contrasena.pack(pady=10)
entry_contrasena = ctk.CTkEntry(login_frame, width=400, height=30, fg_color="white", text_color="black" , border_color="#f4d03f", show="*")  # Oculta el texto de la contraseña
entry_contrasena.pack(pady=10)

# Botón de inicio de sesión
boton_login = ctk.CTkButton(login_frame, text="Iniciar Sesión", corner_radius=10, fg_color="#f4d03f", text_color="black", width=400, height=30)
boton_login.pack(pady=40)

# Mensaje de estado
label_mensaje = ctk.CTkLabel(login_frame, text="", font=("Arial", 14))
label_mensaje.pack()





ventana.mainloop()




