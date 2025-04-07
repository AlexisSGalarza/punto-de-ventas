import customtkinter as ctk
from PIL import Image, ImageDraw


class DashboardVista(ctk.CTkFrame): 
    def __init__(self, master,cambiar_a_trabajadores):
        super().__init__(master)
        self.master = master
        self.cambiar_a_trabajadores = cambiar_a_trabajadores
        # Further initialization
        self.configure(fg_color="#fcf3cf")
        self.configurar_dashboard()
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
            fg_color="#85c1e9",
            text_color="black",
            font=("Arial",30, "bold"),
        )
        boton_venta.grid(row=0, column=0, padx=40, pady=30, sticky="nsew")

        boton_productos = ctk.CTkButton(
            cuadro_botones,
            text="Gestión de productos",
            width=200,
            height=70,
            corner_radius=25,
            fg_color="#85c1e9",
            text_color="black",
            font=("Arial", 30, "bold"),
        )
        boton_productos.grid(row=0, column=1, padx=40, pady=30, sticky="nsew")

        boton_clientes = ctk.CTkButton(
            cuadro_botones,
            text="Gestión de clientes",
            width=200,
            height=70,
            corner_radius=25,
            fg_color="#85c1e9",
            text_color="black",
            font=("Arial", 30, "bold"),
        )
        boton_clientes.grid(row=1, column=0, padx=40, pady=30, sticky="nsew")

        boton_trabajadores = ctk.CTkButton(
            cuadro_botones,
            text="Gestión de trabajadores",
            width=200,
            height=70,
            corner_radius=25,
            fg_color="#85c1e9",
            text_color="black",
            font=("Arial", 30, "bold"),
            command=self.cambiar_a_trabajadores,
        )
        boton_trabajadores.grid(row=1, column=1, padx=40, pady=30, sticky="nsew")

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

        def cerrar_sesion():
            print("Has cerrado sesión.")

        boton = ctk.CTkButton(
            cuadro_inferior,
            text="Cerrar sesión",
            command=cerrar_sesion,
            fg_color="gray",
            height=50,
            text_color="black",
        )
        boton.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        hora_fecha = ctk.CTkLabel(
            cuadro_inferior,
            text="07:05 p.m. - 23/03/2025",
            font=("Arial", 14, "italic"),
            text_color="black",
        )
        hora_fecha.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        cuadro_inferior.grid_rowconfigure(0, weight=1)
        cuadro_inferior.grid_rowconfigure(1, weight=1)
        cuadro_inferior.grid_columnconfigure(0, weight=1)
