import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import db.conexion as co
from datetime import datetime
import os
import sys
from PIL import Image, ImageDraw

class VentanaReportes(ctk.CTk):
    def __init__(self, abrir_dashboard, abrir_graficosr, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Reportes")
        self.geometry("1920x1080")
        self.configure(fg_color="#fcf3cf")
        self.attributes("-fullscreen", True)
        self.abrir_dashboard = abrir_dashboard
        self.abrir_graficos = abrir_graficosr
        self.crear_ui()

    def crear_ui(self):
        """Crea la interfaz de usuario."""
        # Crear encabezado
        self.crear_encabezado()

        # Configurar el cierre de la ventana
    
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
            text="Gestionar Trabajadores",
            font=("Arial", 50, "bold"),
            text_color="black"
        )
        texto_encabezado.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # Botón para regresar al dashboard
        boton_regresar = ctk.CTkButton(
            encabezado,
            text="Regresar al Dashboard",
            font=("Arial", 16, "bold"),
            fg_color="#58d68d",
            text_color="white",
            command=self.abrir_dashboard
        )
        boton_regresar.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Contenedor principal
        contenedor = ctk.CTkFrame(self, fg_color="#fcf3cf")
        contenedor.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        contenedor.grid_columnconfigure(0, weight=1)

        # Botón para generar reporte de inventario
        boton_inventario = ctk.CTkButton(
            contenedor,
            text="Generar Reporte de Inventario",
            font=("Arial", 16),
            fg_color="#58d68d",
            text_color="white",
            command=self.generar_reporte_inventario
        )
        boton_inventario.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Botón para ver gráficos
        boton_graficos = ctk.CTkButton(
            contenedor,
            text="Ver Gráficos",
            font=("Arial", 16),
            fg_color="#58d68d",
            text_color="white",
            command=self.abrir_graficos
        )
        boton_graficos.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    def generar_reporte_inventario(self):
        try:
            # Obtener productos de la base de datos
            productos = co.obtener_productos()
            
            # Crear DataFrame
            df = pd.DataFrame(productos)
            
            # Generar nombre del archivo con fecha y hora
            fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = f"reporte_inventario_{fecha_hora}.xlsx"
            
            # Guardar en Excel
            df.to_excel(nombre_archivo, index=False)
            
            messagebox.showinfo("Éxito", f"Reporte generado: {nombre_archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar el reporte: {str(e)}")
    def redondear_bordes(self, image, radio):
        """Redondea los bordes de la imagen."""
        # Create a mask to round edges
        mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0) + image.size, radius=radio, fill=255)
        rounded_image = Image.new("RGBA", image.size)
        rounded_image.paste(image, mask=mask)
        return rounded_image