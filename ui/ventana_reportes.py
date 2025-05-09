import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from datetime import datetime
import os
import sys
from PIL import Image, ImageDraw
import app.Productos as produ
import app.graficos as co

class VentanaReportes(ctk.CTkFrame):
    def __init__(self, parent, abrir_dashboard, abrir_graficosr=None):
        super().__init__(parent)
        self.configure(fg_color="#fcf3cf")
        self.abrir_dashboard = abrir_dashboard
        self.abrir_graficos = abrir_graficosr
        self.crear_ui()

    def crear_ui(self):
        """Crea la interfaz de usuario."""
        self.crear_encabezado()
        self.crear_panel_principal()

    def crear_encabezado(self):
        """Crea el encabezado principal."""
        # Crear frame para el encabezado
        frame_encabezado = ctk.CTkFrame(self, fg_color="#f4d03f", height=100)
        frame_encabezado.grid(row=0, column=0, columnspan=3, sticky="ew")
        
        # Título de la ventana
        titulo = ctk.CTkLabel(
            frame_encabezado,
            text="Reportes y Análisis",
            font=("Arial", 24, "bold"),
            text_color="black"
        )
        titulo.grid(row=0, column=1, padx=20, pady=20)

        # Botón para regresar al dashboard
        boton_regresar = ctk.CTkButton(
            frame_encabezado,
            text="Regresar al Dashboard",
            font=("Arial", 16),
            fg_color="#f11919",
            text_color="white",
            hover_color="#d91717",
            command=self.abrir_dashboard
        )
        boton_regresar.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        # Configurar el peso de las columnas
        frame_encabezado.grid_columnconfigure(1, weight=1)

    def crear_panel_principal(self):
        """Crea el panel principal con diseño moderno de tarjetas."""
        # Contenedor principal con fondo claro
        contenedor = ctk.CTkFrame(self, fg_color="#ffffff", corner_radius=15)
        contenedor.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=20, pady=20)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Grid de 2x2 para las tarjetas de reportes
        contenedor.grid_columnconfigure((0,1), weight=1)
        contenedor.grid_rowconfigure((0,1), weight=1)

        # Tarjeta 1: Reporte de Inventario
        self.crear_tarjeta_reporte(
            contenedor, 0, 0,
            "Reporte de Inventario",
            "Genera un informe detallado del inventario actual",
            "📦",
            self.generar_reporte_inventario
        )

        # Tarjeta 2: Productos con Bajo Stock
        self.crear_tarjeta_reporte(
            contenedor, 0, 1,
            "Productos con Bajo Stock",
            "Identifica productos que necesitan reabastecimiento",
            "⚠️",
            self.generar_reporte_bajo_stock
        )

        # Tarjeta 3: Ventas por Categoría
        self.crear_tarjeta_reporte(
            contenedor, 1, 0,
            "Ventas por Categoría",
            "Analiza el rendimiento por categoría de productos",
            "📊",
            self.generar_reporte_ventas_por_categoria
        )

        # Tarjeta 4: Clientes Frecuentes
        self.crear_tarjeta_reporte(
            contenedor, 1, 1,
            "Clientes Frecuentes",
            "Identifica y analiza los clientes más leales",
            "👥",
            self.generar_reporte_clientes_frecuentes
        )

        # Botón para ver gráficos
        boton_graficos = ctk.CTkButton(
            contenedor,
            text="Ver Gráficos Detallados 📈",
            font=("Helvetica", 16, "bold"),
            fg_color="#f4d03f",
            hover_color="#e6c430",
            height=40,
            corner_radius=10,
            command=self.abrir_graficos
        )
        boton_graficos.grid(row=2, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

    def crear_tarjeta_reporte(self, parent, row, col, titulo, descripcion, emoji, comando):
        """Crea una tarjeta de reporte con diseño moderno."""
        frame = ctk.CTkFrame(parent, fg_color="#fcf3cf", corner_radius=10)
        frame.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")
        
        # Emoji grande
        ctk.CTkLabel(
            frame,
            text=emoji,
            font=("Helvetica", 48)
        ).grid(row=0, column=0, pady=(20,10))
        
        # Título
        ctk.CTkLabel(
            frame,
            text=titulo,
            font=("Helvetica", 20, "bold"),
            text_color="black"
        ).grid(row=1, column=0, pady=(0,10))
        
        # Descripción
        ctk.CTkLabel(
            frame,
            text=descripcion,
            font=("Helvetica", 14),
            text_color="#333333",
            wraplength=250
        ).grid(row=2, column=0, pady=(0,20))
        
        # Botón
        ctk.CTkButton(
            frame,
            text="Generar Reporte",
            font=("Helvetica", 14),
            fg_color="#f11919",
            hover_color="#d91717",
            height=35,
            corner_radius=8,
            command=comando
        ).grid(row=3, column=0, pady=(0,20))

    def generar_reporte_inventario(self):
        try:
            # Obtener productos de la base de datos
            productos = produ.obtener_productos()

            if not productos:
                messagebox.showwarning("Sin datos", "No hay productos en la base de datos para generar el reporte.")
                return

            # Crear DataFrame con columnas adecuadas
            columnas = ["ID", "Nombre", "Descripción", "Código de Barras","Codigo de Producto", "Categoría", "Precio", "Stock"]
            df = pd.DataFrame(productos, columns=columnas)

            # Generar nombre del archivo con fecha y hora
            fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = os.path.join(os.getcwd(), f"reporte_inventario_{fecha_hora}.xlsx")

            # Guardar en Excel
            df.to_excel(nombre_archivo, index=False)

            messagebox.showinfo("Éxito", f"Reporte generado: {nombre_archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar el reporte: {str(e)}")

    def generar_reporte_bajo_stock(self):
        try:
            # Obtener productos con bajo stock
            productos = co.obtener_productos_bajo_stock(umbral=10)  # Umbral de stock bajo

            if not productos:
                messagebox.showwarning("Sin datos", "No hay productos con bajo stock.")
                return

            # Crear DataFrame
            columnas = ["ID", "Nombre", "Stock"]
            df = pd.DataFrame(productos, columns=columnas)

            # Guardar en Excel
            fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = os.path.join(os.getcwd(), f"reporte_bajo_stock_{fecha_hora}.xlsx")
            df.to_excel(nombre_archivo, index=False)

            messagebox.showinfo("Éxito", f"Reporte generado: {nombre_archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar el reporte: {str(e)}")

    def generar_reporte_ventas_por_categoria(self):
        try:
            # Obtener ventas por categoría
            ventas = co.obtener_ventas_por_categoria()

            if not ventas:
                messagebox.showwarning("Sin datos", "No hay datos de ventas por categoría.")
                return

            # Crear DataFrame
            columnas = ["Categoría", "Total Ventas"]
            df = pd.DataFrame(ventas, columns=columnas)

            # Guardar en Excel
            fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = os.path.join(os.getcwd(), f"reporte_ventas_categoria_{fecha_hora}.xlsx")
            df.to_excel(nombre_archivo, index=False)

            messagebox.showinfo("Éxito", f"Reporte generado: {nombre_archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar el reporte: {str(e)}")

    def generar_reporte_clientes_frecuentes(self):
        try:
            # Obtener clientes frecuentes
            clientes = co.obtener_clientes_frecuentes()

            if not clientes:
                messagebox.showwarning("Sin datos", "No hay clientes frecuentes registrados.")
                return

            # Crear DataFrame
            columnas = ["ID Cliente", "Nombre", "Compras Realizadas"]
            df = pd.DataFrame(clientes, columns=columnas)

            # Guardar en Excel
            fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = os.path.join(os.getcwd(), f"reporte_clientes_frecuentes_{fecha_hora}.xlsx")
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