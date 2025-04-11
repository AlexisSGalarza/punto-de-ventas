import customtkinter as ctk
from PIL import Image
import os
from tkinter import messagebox
from app.login import autentacacion_login

class VentanaLogin(ctk.CTk):
    def __init__(self, cambiar_a_principal,app_state):
        super().__init__()
        self.title("Login - Abarrotes Gael")
        self.geometry("1920x1080")
        self.configure(fg_color="#fcf3cf")
        self.attributes("-fullscreen", True)
        self.cambiar_a_principal = cambiar_a_principal
        self.app_state = app_state
        # Crear UI
        self.crear_ui()

    def crear_ui(self):
        # Crear el cuadro blanco centrado
        cuadro_blanco = ctk.CTkFrame(self, fg_color="white", width=1400, height=700, corner_radius=15)
        cuadro_blanco.place(relx=0.5, rely=0.5, anchor="center")

        # Frame izquierdo para el logo
        frame_logo = ctk.CTkFrame(cuadro_blanco, fg_color="white")
        frame_logo.pack(side="left", padx=20, pady=20, fill="both")

        # Cargar y mostrar el logo
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(BASE_DIR, '..', 'assets', 'logo.jpg')
        logo_imagen = Image.open(image_path)
        logo_imagen_ctk = ctk.CTkImage(logo_imagen, size=(400, 400))
        label_logo = ctk.CTkLabel(frame_logo, image=logo_imagen_ctk, text="")
        label_logo.pack(anchor="center", pady=50)

        # Frame derecho para el formulario
        login_frame = ctk.CTkFrame(cuadro_blanco, fg_color="white", width=900, height=700)
        login_frame.pack(side="right", padx=100, pady=30, fill="both")

        # Título del formulario
        label_titulo = ctk.CTkLabel(login_frame, text="Iniciar Sesión", font=("Arial", 30, "bold"), text_color="black")
        label_titulo.pack(pady=40)

        # Campo de Usuario
        label_usuario = ctk.CTkLabel(login_frame, text="Usuario:", font=("Arial", 20), text_color="black")
        label_usuario.pack(pady=10)
        self.entry_usuario = ctk.CTkEntry(login_frame, width=400, height=30, fg_color="white", border_color="#f4d03f", text_color="black")
        self.entry_usuario.pack(pady=10)

        # Campo de Contraseña
        label_contrasena = ctk.CTkLabel(login_frame, text="Contraseña:", font=("Arial", 20), text_color="black")
        label_contrasena.pack(pady=10)
        self.entry_contrasena = ctk.CTkEntry(login_frame, width=400, height=30, fg_color="white", text_color="black", border_color="#f4d03f", show="*")
        self.entry_contrasena.pack(pady=10)

        # Mensaje de estado
        self.label_mensaje = ctk.CTkLabel(login_frame, text="", font=("Arial", 14))
        self.label_mensaje.pack()

        # Botón de inicio de sesión
        boton_login = ctk.CTkButton(
            login_frame,
            text="Iniciar Sesión",
            corner_radius=10,
            fg_color="#f4d03f",
            text_color="black",
            width=400,
            height=30,
            command=self.iniciar_sesion
        )
        boton_login.pack(pady=10)

    def iniciar_sesion(self):
            usuario = self.entry_usuario.get().strip()
            contrasena = self.entry_contrasena.get().strip()

            if not usuario or not contrasena:
                self.label_mensaje.configure(text="Los campos no pueden estar vacíos", text_color="orange")
                return

            try:
                resultado = autentacacion_login(usuario, contrasena)
            except Exception as e:
                self.label_mensaje.configure(text=f"Error: {str(e)}", text_color="red")
                return

            if resultado:
                print(f"Resultado del login: {resultado}")  # Depuración
                self.app_state.iniciar_sesion(
                            id=resultado["ID_tr"],  # ID del usuario
                            usuario=resultado["Nombre_tr"],  # Nombre del usuario
                            rol=resultado["Rol_tr"]  # Rol del usuario
                        )
                self.cambiar_a_principal()
            else:
                self.label_mensaje.configure(text="Usuario o contraseña incorrectos", text_color="red")

