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

        # Tarjeta 2: Tendencias de Ventas
        self.crear_tarjeta_reporte(
            contenedor, 0, 1,
            "Tendencias de Ventas",
            "Análisis de ventas diarias y semanales",
            "📈",
            self.generar_reporte_tendencias_ventas
        )

        # Tarjeta 3: Análisis por Hora
        self.crear_tarjeta_reporte(
            contenedor, 1, 0,
            "Análisis por Hora",
            "Ventas y afluencia por hora del día",
            "🕒",
            self.generar_reporte_ventas_por_hora
        )

        # Tarjeta 4: Ventas por Trabajador
        self.crear_tarjeta_reporte(
            contenedor, 1, 1,
            "Ventas por Trabajador",
            "Análisis detallado del desempeño de ventas por trabajador",
            "👥",
            self.generar_reporte_ventas_trabajador
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

    def generar_nombre_archivo(self, tipo_reporte):
        """Genera un nombre de archivo con la fecha y hora actual."""
        fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
        return os.path.join(os.getcwd(), "reportes", f"reporte_{tipo_reporte}_{fecha_hora}.xlsx")

    def generar_reporte_inventario(self):
        try:
            # Obtener productos de la base de datos
            productos = produ.obtener_productos()

            if not productos:
                messagebox.showwarning("Sin datos", "No hay productos en la base de datos para generar el reporte.")
                return

            # Crear DataFrame con columnas adecuadas
            columnas = ["ID", "Nombre", "Descripción", "Código de Barras", "Código de Producto", "Categoría", "Precio", "Stock"]
            df = pd.DataFrame(productos, columns=columnas)

            # Guardar en Excel en la carpeta reportes
            nombre_archivo = self.generar_nombre_archivo("inventario")
            df.to_excel(nombre_archivo, index=False)
            messagebox.showinfo("Éxito", f"Reporte generado: {nombre_archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar el reporte: {str(e)}")

    def generar_reporte_tendencias_ventas(self):
        try:
            # Obtener ventas diarias y semanales
            ventas = co.obtener_tendencias_ventas()

            if not ventas:
                messagebox.showwarning("Sin datos", "No hay datos de ventas para analizar.")
                return

            # Crear DataFrame con los datos
            df = pd.DataFrame(ventas)

            # Agregar análisis semanal
            df['Semana'] = pd.to_datetime(df['Fecha']).dt.isocalendar().week
            resumen_semanal = df.groupby('Semana').agg({
                'TotalVentas': 'sum',
                'NumeroVentas': 'sum',
                'TicketPromedio': 'mean'
            }).reset_index()

            # Guardar en Excel con múltiples hojas
            nombre_archivo = self.generar_nombre_archivo("tendencias_ventas")
            
            with pd.ExcelWriter(nombre_archivo, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Ventas Diarias', index=False)
                resumen_semanal.to_excel(writer, sheet_name='Resumen Semanal', index=False)

            messagebox.showinfo("Éxito", f"Reporte generado: {nombre_archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar el reporte: {str(e)}")

    def generar_reporte_ventas_por_hora(self):
        try:
            # Obtener ventas por hora
            ventas = co.obtener_ventas_por_hora()

            if not ventas:
                messagebox.showwarning("Sin datos", "No hay datos de ventas para analizar.")
                return

            # Crear DataFrame con los datos
            df = pd.DataFrame(ventas)
            
            # Resumen por hora del día
            resumen_hora = df.groupby('Hora').agg({
                'NumTransacciones': 'sum',
                'TotalVentas': 'sum',
                'TicketPromedio': 'mean',
                'NumClientes': 'sum',
                'ProductosVendidos': 'sum'
            }).round(2)
            
            # Calcular métricas adicionales
            total_ventas = resumen_hora['TotalVentas'].sum()
            resumen_hora['% del Total de Ventas'] = (resumen_hora['TotalVentas'] / total_ventas * 100).round(2)
            resumen_hora['Productos por Transacción'] = (resumen_hora['ProductosVendidos'] / resumen_hora['NumTransacciones']).round(2)
            
            # Identificar horas pico
            resumen_hora['Es Hora Pico'] = resumen_hora['NumTransacciones'] > resumen_hora['NumTransacciones'].mean()
            
            # Tendencia por día y hora
            tendencia_diaria = df.pivot_table(
                index='Fecha',
                columns='Hora',
                values=['TotalVentas', 'NumTransacciones'],
                aggfunc='sum'
            ).fillna(0)

            # Guardar en Excel con múltiples hojas
            nombre_archivo = self.generar_nombre_archivo("ventas_por_hora")
            
            with pd.ExcelWriter(nombre_archivo, engine='openpyxl') as writer:
                resumen_hora.to_excel(writer, sheet_name='Resumen por Hora')
                tendencia_diaria.to_excel(writer, sheet_name='Tendencia Diaria')
                df.to_excel(writer, sheet_name='Datos Detallados', index=False)

            messagebox.showinfo("Éxito", f"Reporte generado: {nombre_archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar el reporte: {str(e)}")

    def generar_reporte_ventas_trabajador(self):
        try:
            # Obtener ventas por trabajador
            ventas = co.obtener_ventas_por_trabajador()

            if not ventas:
                messagebox.showwarning("Sin datos", "No hay datos de ventas por trabajador para analizar.")
                return

            # Crear DataFrame con los datos
            df = pd.DataFrame(ventas)
            
            # Resumen por trabajador
            resumen_trabajador = df.groupby('Trabajador').agg({
                'NumVentas': 'sum',
                'TotalVentas': 'sum',
                'PromedioVenta': 'mean',
                'NumClientes': 'sum',
                'ProductosVendidos': 'sum'
            }).round(2)
            
            # Calcular métricas adicionales con validación para división por cero
            resumen_trabajador['Venta por Cliente'] = 0.0  # Valor predeterminado
            mask = resumen_trabajador['NumClientes'] > 0
            if mask.any():
                resumen_trabajador.loc[mask, 'Venta por Cliente'] = (
                    resumen_trabajador.loc[mask, 'TotalVentas'] / 
                    resumen_trabajador.loc[mask, 'NumClientes']
                ).round(2)

            total_ventas = resumen_trabajador['TotalVentas'].sum()
            resumen_trabajador['% del Total de Ventas'] = 0.0  # Valor predeterminado
            if total_ventas > 0:
                resumen_trabajador['% del Total de Ventas'] = (
                    resumen_trabajador['TotalVentas'] / total_ventas * 100
                ).round(2)
            
            # Tendencia diaria por trabajador
            tendencia_diaria = df.pivot_table(
                index='Fecha',
                columns='Trabajador',
                values=['TotalVentas', 'NumVentas'],
                aggfunc='sum'
            ).fillna(0)

            # Guardar en Excel con múltiples hojas
            nombre_archivo = self.generar_nombre_archivo("ventas_trabajador")
            
            with pd.ExcelWriter(nombre_archivo, engine='openpyxl') as writer:
                resumen_trabajador.to_excel(writer, sheet_name='Resumen por Trabajador')
                tendencia_diaria.to_excel(writer, sheet_name='Tendencia Diaria')
                df.to_excel(writer, sheet_name='Datos Detallados', index=False)

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