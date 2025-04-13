import matplotlib.pyplot as plt
import pandas as pd
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageDraw
import app.graficos as graficos  # Asegúrate de que este módulo esté en la misma carpeta o ajusta la ruta

class ventanagraficos(ctk.CTk):
    def __init__(self, cambiar_a_dashboard):
        super().__init__()
        self.title("ventana graficos")
        self.cambiar_a_dashboard = cambiar_a_dashboard 
        self.geometry("1920x1080")  # Tamaño inicial ajustado
        self.configure(fg_color="#fcf3cf")  # Fondo claro
        self.attributes("-fullscreen", True)

        # Configuración para que las filas y columnas se expandan dinámicamente
        self.grid_rowconfigure(0, weight=1)  # Encabezado
        self.grid_rowconfigure(1, weight=1)  # Botones encima
        self.grid_rowconfigure(2, weight=10,)  # Aumentamos el peso del área de gráficos
        self.grid_rowconfigure(3, weight=1)  # Footer
        self.grid_columnconfigure(0, weight=1)

        # Crear componentes de la interfaz
        self.crear_encabezado()
        self.crear_frame_botones_y_graficos()
        self.crear_footer()

        # Cargar datos simulados
        self.data_productos = pd.DataFrame({
            "Producto": ["Laptop", "Mouse", "Teclado", "Monitor", "Impresora"],
            "Total_Vendido": [150, 300, 200, 180, 100]
        })
        self.data_trabajadores = pd.DataFrame({
            "Trabajador": ["Juan", "Ana", "Luis", "Sofía", "Pedro"],
            "Total_Ventas": [5000, 7000, 4500, 6000, 5500]
        })

    def crear_encabezado(self):
        """Crea el encabezado principal."""
        encabezado = ctk.CTkFrame(self, fg_color="#f4d03f", height=100)
        encabezado.grid(row=0, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

        franja_roja = ctk.CTkFrame(encabezado, fg_color="#f11919", height=20)
        franja_roja.grid(row=1, column=0, columnspan=3, sticky="ew")

        encabezado.grid_columnconfigure(0, weight=1)
        encabezado.grid_columnconfigure(1, weight=1)
        encabezado.grid_columnconfigure(2, weight=1)

        # Logo
        logo_imagen = Image.open("assets/logo.jpg")
        logo_imagen_redondeada = self.redondear_bordes(logo_imagen, radio=75)
        logo_imagen_ctk = ctk.CTkImage(logo_imagen_redondeada, size=(100, 100))

        logo = ctk.CTkLabel(encabezado, image=logo_imagen_ctk, text="")
        logo.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Texto del encabezado
        texto_encabezado = ctk.CTkLabel(
            encabezado,
            text="Graficos de Ventas",
            corner_radius=10,
            font=("Arial", 50, "bold"),
            text_color="black",
        )
        texto_encabezado.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    def crear_frame_botones_y_graficos(self):
        """Crea el marco para los botones y el área de gráficos."""
        # Frame para los botones de gráficos
        self.frame_botones = ctk.CTkFrame(self, fg_color="#fcf3cf")
        self.frame_botones.grid(row=1, column=0, sticky="ew", padx=20, pady=10)

        self.frame_botones.grid_columnconfigure(0, weight=1)
        self.frame_botones.grid_columnconfigure(1, weight=1)

        btn_productos = ctk.CTkButton(self.frame_botones, text="📈 Productos Más Vendidos", command=self.grafico_productos, fg_color="#3498db", text_color="white")
        btn_productos.grid(row=0, column=0, padx=10, pady=10)

        btn_trabajadores = ctk.CTkButton(self.frame_botones, text="📊 Ventas por Trabajador", command=self.grafico_trabajadores, fg_color="#e74c3c", text_color="white")
        btn_trabajadores.grid(row=0, column=1, padx=10, pady=10)

        # Frame para gráficos
        self.frame_graficos = ctk.CTkFrame(self, corner_radius=10, fg_color="white")
        self.frame_graficos.grid(row=2, column=0, sticky="nsew", padx=20, pady=10)

    def crear_footer(self):
        """Crea un footer con el botón de regresar al lado izquierdo."""
        footer = ctk.CTkFrame(self, fg_color="#fcf3cf", corner_radius=10)
        footer.grid(row=3, column=0, sticky="ew", padx=20, pady=10)

        footer.grid_columnconfigure(0, weight=1)

        btn_regresar = ctk.CTkButton(footer, text="⬅ Regresar al Dashboard", command=self.cambiar_a_dashboard , fg_color="#2ecc71", text_color="white")
        btn_regresar.grid(row=0, column=0, padx=10, pady=10, sticky="w")

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