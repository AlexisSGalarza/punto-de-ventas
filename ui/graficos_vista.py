import matplotlib.pyplot as plt
import pandas as pd
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageDraw
import app.graficos as graficos  

class ventanagraficos(ctk.CTk):
    def __init__(self, cambiar_a_dashboard):
        super().__init__()
        self.title("Sistema de Gráficos")
        self.cambiar_a_dashboard = cambiar_a_dashboard 
        self.geometry("1920x1080")
        self.configure(fg_color="#fcf3cf")  
        self.attributes("-fullscreen", True)

        # Configuración del grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=12)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Crear componentes
        self.crear_encabezado()
        self.crear_frame_botones_y_graficos()
        self.crear_footer()

    def crear_encabezado(self):
        encabezado = ctk.CTkFrame(self, fg_color="#f4d03f", height=120, corner_radius=0)
        encabezado.grid(row=0, column=0, columnspan=3, sticky="ew", padx=0, pady=(0, 10))

        # Línea decorativa superior
        franja_superior = ctk.CTkFrame(encabezado, fg_color="#f11919", height=4)
        franja_superior.grid(row=0, column=0, columnspan=3, sticky="ew")

        encabezado.grid_columnconfigure(0, weight=1)
        encabezado.grid_columnconfigure(1, weight=2)
        encabezado.grid_columnconfigure(2, weight=1)

     
        logo_imagen = Image.open("assets/logo.jpg")
        logo_imagen_redondeada = self.redondear_bordes(logo_imagen, radio=75)
        logo_imagen_ctk = ctk.CTkImage(logo_imagen_redondeada, size=(90, 90))

        logo = ctk.CTkLabel(encabezado, image=logo_imagen_ctk, text="")
        logo.grid(row=1, column=0, padx=30, pady=10, sticky="w")

        # Título con mejor tipografía y diseño
        texto_encabezado = ctk.CTkLabel(
            encabezado,
            text="Panel de Análisis de Ventas",
            font=("Helvetica", 48, "bold"),
            text_color="#2C3E50"
        )
        texto_encabezado.grid(row=1, column=1, padx=10, pady=10)

    def crear_frame_botones_y_graficos(self):
        # Frame para botones con diseño mejorado
        self.frame_botones = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_botones.grid(row=1, column=0, sticky="ew", padx=40, pady=5)

        self.frame_botones.grid_columnconfigure((0,1), weight=1)

        # Botones más modernos con iconos y efectos
        btn_productos = ctk.CTkButton(
            self.frame_botones,
            text="Productos Más Vendidos",
            command=self.grafico_productos,
            font=("Helvetica", 16, "bold"),
            fg_color="#F39C12",
            hover_color="#2573A7",
            height=45,
            corner_radius=10,
            border_spacing=10
        )
        btn_productos.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        btn_trabajadores = ctk.CTkButton(
            self.frame_botones,
            text="Ventas por Trabajador",
            command=self.grafico_trabajadores,
            font=("Helvetica", 16, "bold"),
            fg_color="#f11919",
            hover_color="#229954",
            height=45,
            corner_radius=10,
            border_spacing=10
        )
        btn_trabajadores.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

        # Frame para gráficos con sombra y bordes redondeados
        self.frame_graficos = ctk.CTkFrame(
            self,
            corner_radius=15,
            fg_color="white",
            border_width=1,
            border_color="white",
        )
        self.frame_graficos.grid(row=2, column=0, sticky="nsew", padx=40, pady=10)

    def crear_footer(self):
        """Crea un footer moderno."""
        footer = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        footer.grid(row=3, column=0, sticky="ew", padx=40, pady=15)

        footer.grid_columnconfigure(0, weight=1)

        btn_regresar = ctk.CTkButton(
            footer,
            text="Regresar al Dashboard",
            command=self.cambiar_a_dashboard,
            font=("Helvetica", 16),
            fg_color="#F39C12",
            hover_color="#F39C12",
            height=40,
            corner_radius=10,
            border_spacing=10
        )
        btn_regresar.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    def mostrar_grafico(self, fig):
        """Muestra gráficos en el frame central."""
        for widget in self.frame_graficos.winfo_children():
            widget.destroy()  # Eliminar gráficos anteriores

        canvas = FigureCanvasTkAgg(fig, master=self.frame_graficos)
        canvas.get_tk_widget().pack(fill="both", expand=True)
        canvas.draw()

    def limpiar_graficos(self):
        """Limpia los gráficos y regresa al dashboard principal."""
        for widget in self.frame_graficos.winfo_children():
            widget.destroy()

    def grafico_productos(self):
        """Crea y muestra el gráfico de productos más vendidos usando el módulo graficos."""
        data = graficos.obtener_productos_mas_vendidos()
        if data is None or data.empty:
            print("[DEBUG] No se pudieron obtener datos de productos más vendidos o los datos están vacíos.")
            return

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(data["Producto"], data["CantidadVendida"], color="deepskyblue")  # Cambié para usar el nombre del producto
        ax.set_title("Productos Más Vendidos", fontsize=14, fontweight="bold")
        ax.set_ylabel("Cantidad Vendida")
        ax.set_xlabel("Producto")  # Cambié para reflejar el nombre del producto
        ax.tick_params(axis="x", rotation=45)
        ax.grid(axis="y", linestyle="--", alpha=0.7)

        self.mostrar_grafico(fig)

    def grafico_trabajadores(self):
        """Crea y muestra el gráfico de ventas por trabajador usando el módulo graficos."""
        data = graficos.obtener_ventas_por_trabajador()
        if data is None or data.empty:
            print("No se pudieron obtener datos de ventas por trabajador.")
            return

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(data["Trabajador"], data["TotalVentas"], color="lightcoral")  # Cambié para usar el nombre del trabajador
        ax.set_title("Ventas por Trabajador", fontsize=14, fontweight="bold")
        ax.set_ylabel("Número de Ventas")
        ax.set_xlabel("Trabajador")  # Cambié para reflejar el nombre del trabajador
        ax.tick_params(axis="x", rotation=45)
        ax.grid(axis="y", linestyle="--", alpha=0.7)

        self.mostrar_grafico(fig)

    def redondear_bordes(self, imagen, radio):
        """Redondear bordes de imágenes."""
        mask = Image.new("L", imagen.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, imagen.size[0], imagen.size[1]), fill=255)
        imagen.putalpha(mask)
        return imagen


# Ejecutar aplicación
if __name__ == "__main__":
    app = ventanagraficos()
    app.mainloop()