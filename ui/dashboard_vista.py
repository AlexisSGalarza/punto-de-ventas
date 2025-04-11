import customtkinter as ctk
from PIL import Image, ImageDraw
from tkinter import messagebox
from datetime import datetime

class DashboardVista(ctk.CTk):
    def __init__(self, cambiar_a_clientes, cambiar_a_trabajadores, cambiar_a_login, app_state, cambiar_a_productos, cambiar_a_reportes, cambiar_a_graficos, cambiar_a_principal):
        super().__init__()
        self.title("Dashboard - Abarrotes Gael")
        self.geometry("1920x1080")
        self.configure(fg_color="#fcf3cf")
        self.attributes("-fullscreen", True)
        self.cambiar_a_clientes = cambiar_a_clientes
        self.cambiar_a_trabajadores = cambiar_a_trabajadores
        self.cambiar_a_login = cambiar_a_login
        self.cambiar_a_productos = cambiar_a_productos
        self.cambiar_a_reportes = cambiar_a_reportes
        self.cambiar_a_graficos = cambiar_a_graficos
        self.app_state = app_state
        self.cambiar_a_principal = cambiar_a_principal

        if not self.app_state.sesion_iniciada:
            messagebox.showerror("Acceso denegado", "Debe iniciar sesión para acceder al dashboard.")
            self.cambiar_a_login()
            return

        self.encabezado()
        self.crear_cuadro_botones()
        self.crear_cuadro_inferior()

    def configurar_dashboard(self):
        """Configura las propiedades del Dashboard."""
        self.master.title("Dashboard - Abarrotes Gael")
        self.master.configure(fg_color="#fcf3cf")
        self.pack(fill="both", expand=True)

    def redondear_bordes(self, imagen, radio):
        """Redondea los bordes de una imagen."""
        mascara = Image.new("L", imagen.size, 0)
        draw = ImageDraw.Draw(mascara)
        draw.rounded_rectangle(
            (0, 0, imagen.size[0], imagen.size[1]), radius=radio, fill=255
        )
        imagen_redondeada = imagen.convert("RGBA")
        imagen_redondeada.putalpha(mascara)
        return imagen_redondeada

    def encabezado(self):
        """Crea el encabezado principal del Dashboard."""
        encabezado = ctk.CTkFrame(self, fg_color="#f4d03f", height=100)
        encabezado.grid(row=0, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

        franja_roja = ctk.CTkFrame(encabezado, fg_color="#f11919", height=20)
        franja_roja.grid(row=1, column=0, columnspan=3, sticky="ew")

        # Cargar el logo
        logo_imagen = Image.open("assets/logo.jpg")
        logo_imagen_redondeada = self.redondear_bordes(logo_imagen, radio=75)
        logo_imagen_ctk = ctk.CTkImage(logo_imagen_redondeada, size=(100, 100))

        logo = ctk.CTkLabel(encabezado, image=logo_imagen_ctk, text="")
        logo.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        texto_encabezado = ctk.CTkLabel(
            encabezado,
            text="Tienda 'Abarrotes Gael'",
            font=("Arial", 50, "bold"),
            text_color="black",
        )
        texto_encabezado.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        encabezado.grid_columnconfigure(1, weight=1)

    def crear_cuadro_botones(self):
        """Evalúa el rol del usuario y ejecuta la subfunción correspondiente para el diseño."""
        if self.app_state.rol_actual == 1:
            self.crear_cuadro_botones_rol_1()  # Diseño para rol 1
        else:
            self.crear_cuadro_botones_rol_2()  # Diseño para rol 2

    def crear_cuadro_botones_rol_1(self):
        """Crea el cuadro central con botones."""
        cuadro_botones = ctk.CTkFrame(self, fg_color="#fcf3cf", width=600, height=400)
        cuadro_botones.grid(
            row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew"
        )

        # Botones de sección
        boton_venta = ctk.CTkButton(
            cuadro_botones,
            text="Venta",
            width=200,
            height=70,
            corner_radius=25,
            fg_color="#e59866",
            text_color="black",
            font=("Arial",30, "bold"),
            command=self.cambiar_a_principal,
        )
        boton_venta.grid(row=0, column=0, padx=40, pady=30, sticky="nsew")

        boton_productos = ctk.CTkButton(
            cuadro_botones,
            text="Gestión de productos",
            width=200,
            height=70,
            corner_radius=25,
            fg_color="#e59866",
            text_color="black",
            font=("Arial", 30, "bold"),
            command=self.cambiar_a_productos,
        )
        boton_productos.grid(row=0, column=1, padx=40, pady=30, sticky="nsew")

        boton_clientes = ctk.CTkButton(
            cuadro_botones,
            text="Gestión de clientes",
            width=200,
            height=70,
            corner_radius=25,
            fg_color="#e59866",
            text_color="black",
            font=("Arial", 30, "bold"),
            command=self.cambiar_a_clientes,
        )
        boton_clientes.grid(row=1, column=0, padx=40, pady=30, sticky="nsew")

        boton_trabajadores = ctk.CTkButton(
            cuadro_botones,
            text="Gestión de trabajadores",
            width=200,
            height=70,
            corner_radius=25,
            fg_color="#e59866",
            text_color="black",
            font=("Arial", 30, "bold"),
            command=self.cambiar_a_trabajadores,
        )
        boton_trabajadores.grid(row=1, column=1, padx=40, pady=30, sticky="nsew")

        # Botón de Reporte
        boton_reporte = ctk.CTkButton(
            cuadro_botones,
            text="Reporte",
            width=200,
            height=70,
            corner_radius=25,
            fg_color="#e59866",
            text_color="black",
            font=("Arial", 30, "bold"),
            command=self.cambiar_a_reportes,
        )
        boton_reporte.grid(row=2, column=0, padx=40, pady=30, sticky="nsew")

        # Botón de Gráficos
        boton_graficos = ctk.CTkButton(
            cuadro_botones,
            text="Gráficos",
            width=200,
            height=70,
            corner_radius=25,
            fg_color="#e59866",
            text_color="black",
            font=("Arial", 30, "bold"),
            command=self.cambiar_a_graficos,
        )
        boton_graficos.grid(row=2, column=1, padx=40, pady=30, sticky="nsew")


        cuadro_botones.grid_rowconfigure(0, weight=1)
        cuadro_botones.grid_rowconfigure(1, weight=1)
        cuadro_botones.grid_rowconfigure(2, weight=1)
        cuadro_botones.grid_columnconfigure(0, weight=1)
        cuadro_botones.grid_columnconfigure(1, weight=1)


        self.grid_rowconfigure(0, weight=0)  # Encabezado
        self.grid_rowconfigure(1, weight=1)  # Cuadro botones
        self.grid_rowconfigure(2, weight=0)  # Pie de página
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
    def crear_cuadro_botones_rol_2(self):
        """Crea el cuadro central con botones para rol 2, expandiendo el diseño."""
        cuadro_botones = ctk.CTkFrame(self, fg_color="#fcf3cf", width=600, height=400)
        cuadro_botones.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Botón de Venta
        boton_venta = ctk.CTkButton(
            cuadro_botones,
            text="Venta",
            width=200,
            height=70,
            corner_radius=25,
            fg_color="#e59866",
            text_color="black",
            font=("Arial", 30, "bold"),
            command=self.cambiar_a_principal,
        )
        boton_venta.grid(row=0, column=0, padx=40, pady=30, sticky="nsew")

        # Botón de Gestión de Productos (expandido para rol 2)
        boton_clientes = ctk.CTkButton(
            cuadro_botones,
            text="Gestión de clientes",
            width=200,
            height=70,
            corner_radius=25,
            fg_color="#e59866",
            text_color="black",
            font=("Arial", 30, "bold"),
            command=self.cambiar_a_clientes,
        )

        boton_clientes.grid(row=0, column=1, padx=40, pady=30, sticky="nsew")

        # Botón de Gestión de Clientes
        boton_productos = ctk.CTkButton(
            cuadro_botones,
            text="Gestión de productos",
            width=400,
            height=70,
            corner_radius=25,
            fg_color="#e59866",
            text_color="black",
            font=("Arial", 30, "bold"),
            command=self.cambiar_a_productos,
        )
        boton_productos.grid(row=1, column=0,columnspan=2, padx=40, pady=30, sticky="nsew")

        cuadro_botones.grid_rowconfigure(0, weight=1)
        cuadro_botones.grid_rowconfigure(1, weight=1)
        cuadro_botones.grid_columnconfigure(0, weight=1)
        cuadro_botones.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=0)  # Encabezado
        self.grid_rowconfigure(1, weight=1)  # Cuadro botones
        self.grid_rowconfigure(2, weight=0)  # Pie de página
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def crear_cuadro_inferior(self):
        """Crea el cuadro inferior con el botón de cerrar sesión."""
        cuadro_inferior = ctk.CTkFrame(self, fg_color="#fcf3cf", height=150, width=800)
        cuadro_inferior.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        boton = ctk.CTkButton(
            cuadro_inferior,
            text="Cerrar sesión",
            command=self.cerrar_sesion,
            fg_color="gray",
            height=50,
            text_color="black",
        )
        boton.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        self.hora_fecha = ctk.CTkLabel(
            cuadro_inferior,
            text="",  # Inicialmente vacío
            font=("Arial", 14, "italic"),
            text_color="black",
        )
        self.hora_fecha.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        # Configurar el diseño del cuadro inferior
        cuadro_inferior.grid_rowconfigure(0, weight=1)
        cuadro_inferior.grid_rowconfigure(1, weight=1)
        cuadro_inferior.grid_columnconfigure(0, weight=1)

        # Iniciar la actualización de la hora
        self.actualizar_hora()

    def actualizar_hora(self):
        """Actualiza la hora y programa la próxima actualización."""
        fecha_hora_actual = datetime.now().strftime("%I:%M:%S %p - %d/%m/%Y")
        self.hora_fecha.configure(text=fecha_hora_actual)
        # Volver a llamar a esta función después de 1 segundo (1000 ms)
        self.after(1000, self.actualizar_hora)

    def cerrar_sesion(self):
        """Restablecer el estado de sesión y redirigir al login tras confirmación."""
        # Mostrar mensaje de confirmación
        confirmacion = messagebox.askyesno(
            "Confirmar cierre de sesión",
            "¿Estás seguro de que quieres cerrar sesión?",
        )
        
        if confirmacion:
            # Si el usuario confirma, cerrar sesión
            self.app_state.cerrar_sesion()
            messagebox.showinfo("Cerrar sesión", "La sesión se ha cerrado correctamente.")
            self.cambiar_a_login()
        else:
            # Si el usuario cancela, no hacer nada
            messagebox.showinfo("Cerrar sesión cancelada", "Continuando en el dashboard.")

