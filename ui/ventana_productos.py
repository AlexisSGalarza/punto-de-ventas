import customtkinter as ctk
from PIL import Image, ImageDraw
import app.agregar_producto as ap
import app.modificar_producto as mp
import app.Productos as productos
from tkinter import messagebox

class VentanaProductos(ctk.CTkFrame):  # Cambiado de CTk a CTkFrame
    def __init__(self, parent, abrir_dashboard):  # Añadido parent como parámetro
        super().__init__(parent)  # Pasando parent al constructor
        self.configure(fg_color="#fcf3cf")
        self.abrir_dashboard = abrir_dashboard

        self.current_page = 1  # Página actual
        self.items_per_page = 10  # Número de productos por página
        self.filtered_productos = productos.obtener_productos()  # Lista inicial sin filtrar

        # Crear encabezado
        self.crear_encabezado()

        # Barra superior con buscador y botón "Agregar Producto"
        self.search_frame = ctk.CTkFrame(self, fg_color="#fcf3cf")
        self.search_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.search_frame.grid_columnconfigure(0, weight=0)  # Alinear "Agregar Producto" a la izquierda
        self.search_frame.grid_columnconfigure(1, weight=1)  # Centrar el buscador
        self.search_frame.grid_columnconfigure(2, weight=0)  # Alinear "Buscar" a la derecha

        self.add_product_button = ctk.CTkButton(self.search_frame, text="➕ Agregar Producto", fg_color="#2ecc71", text_color="white", command=self.abrir_agregar_producto)
        self.add_product_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.search_entry = ctk.CTkEntry(self.search_frame, placeholder_text="🔍 Buscar producto...", width=300, fg_color="white", text_color="black")
        self.search_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.search_button = ctk.CTkButton(self.search_frame, text="Buscar", command=self.buscar_producto, fg_color="white", text_color="black")
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        # Contenedor principal de la tabla
        self.frame_table = ctk.CTkFrame(self, fg_color="white", border_width=2, border_color="white", corner_radius=30)
        self.frame_table.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Contenedor de paginación (botones "Anterior", "Siguiente" y "Regresar al Dashboard")
        self.pagination_frame = ctk.CTkFrame(self, fg_color="#fcf3cf")
        self.pagination_frame.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        self.pagination_frame.grid_columnconfigure(0, weight=1)  # Botón "Anterior"
        self.pagination_frame.grid_columnconfigure(1, weight=1)  # Botón "Regresar al Dashboard"
        self.pagination_frame.grid_columnconfigure(2, weight=1)  # Botón "Siguiente"

        self.back_button = ctk.CTkButton(self.pagination_frame, text="🏠 Regresar al Dashboard", command=self.abrir_dashboard, fg_color="#2ecc71", text_color="white")
        self.back_button.grid(row=0, column=0, padx=5, sticky="w")

        self.prev_button = ctk.CTkButton(self.pagination_frame, text="⬅ Anterior", command=self.previous_page, fg_color="white", text_color="black")
        self.prev_button.grid(row=0, column=2, padx=5, sticky="e")

        self.next_button = ctk.CTkButton(self.pagination_frame, text="Siguiente ➡", command=self.next_page, fg_color="white", text_color="black")
        self.next_button.grid(row=0, column=3, padx=5, sticky="e")

        # Llenar la tabla
        self.populate_table()

        self.after(200, self.check_stock)   # Verificar el stock de los productos al iniciar la ventana

    def actualizar_tabla(self):
        self.filtered_productos = productos.obtener_productos()
        self.current_page = 1  # Reinicia a la primera página
        self.populate_table()  # Vuelve a llenar la tabla con toda la información

    def abrir_agregar_producto(self):
        ap.agregar_producto(on_close_callback=self.actualizar_tabla)

    def modificar_producto(self, id_producto):
        mp.modificar_producto(id_producto, on_close_callback=self.actualizar_tabla)

    def eliminar_producto(self, id_producto):
        if messagebox.askyesno("Confirmar", f"¿Estás seguro de que deseas eliminar al Producto con ID {id_producto}?"):
            try:
                productos.eliminar_producto(id_producto)  # Llama a la función que elimina al trabajador
                messagebox.showinfo("Éxito", f"El Producto con ID {id_producto} ha sido eliminado.")
                self.actualizar_tabla()  # Actualiza la tabla después de eliminar
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar al Producto: {e}")
    
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
            text="Gestionar Productos ",
            font=("Arial", 50, "bold"),
            text_color="black"
        )
        texto_encabezado.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    def buscar_producto(self):
        """Filtra productos según la búsqueda."""
        query = self.search_entry.get().lower()  # Texto ingresado en el buscador
        
        # Filtrar productos por nombre, código de barras o código de producto
        self.filtered_productos = [
            p for p in productos.obtener_productos()
            if query in p[1].lower() or query in p[3].lower() or query in p[4].lower()  # p[1]: Nombre, p[3]: Código de barras, p[4]: Código de producto
        ]
        
        self.current_page = 1  # Reinicia la paginación al comenzar una nueva búsqueda
        self.populate_table()  # Actualiza la tabla con los resultados filtrados

    def populate_table(self):
        """Llena la tabla con los productos filtrados."""
        for widget in self.frame_table.winfo_children():
            widget.destroy()  # Limpiar la tabla existente

        # Encabezados de la tabla, incluyendo "Stock"
        headers = ["ID Producto", "Producto", "Descripción", "Código barras","Código de producto", "Categoría", "Precio ($)", "Stock", "Acciones"]
        for col, header in enumerate(headers):
                    lbl = ctk.CTkLabel(self.frame_table, text=header, font=("Arial", 18, "bold"), fg_color="#f4d03f", text_color="black")
                    lbl.grid(row=0, column=col, sticky="nsew", padx=2, pady=2)
        
        all_items = self.filtered_productos
        
        # Configuración de columnas
        for col in range(len(headers)):
            if col == len(headers) - 1:  # Última columna (botones)
                self.frame_table.grid_columnconfigure(col, weight=1, minsize=150)  # Prioridad menor y tamaño mínimo
            else:
                self.frame_table.grid_columnconfigure(col, weight=2 if col < 3 else 1)

        start = (self.current_page - 1) * self.items_per_page
        end = start + self.items_per_page
        page_items = self.filtered_productos[start:end]

        for row, item in enumerate(page_items, start=1):
            # Insertar el ID en la primera columna
            lbl_id = ctk.CTkLabel(self.frame_table, text=item[0], font=("Arial", 14), text_color="black", padx=2)
            lbl_id.grid(row=row, column=0, sticky="nsew", pady=2)

            # Llenar las columnas restantes con los datos de 'item'
            for col, value in enumerate(item[1:]):  # Empezamos desde el índice 1 para excluir el ID
                lbl = ctk.CTkLabel(self.frame_table, text=value, font=("Arial", 14), text_color="black", padx=2)
                lbl.grid(row=row, column=col + 1, sticky="nsew", pady=2)


            button_frame = ctk.CTkFrame(self.frame_table, fg_color="transparent")
            button_frame.grid(row=row, column=len(headers) - 1, sticky="w", padx=2, pady=2)

            # Botón Editar
            btn_edit = ctk.CTkButton(button_frame, text="✏ Editar", fg_color="#2471a3", text_color="white", width=50, command=lambda id_producto=item[0]: self.modificar_producto(id_producto))
            btn_edit.pack(side="left", padx=5)

            # Botón Eliminar
            btn_delete = ctk.CTkButton(button_frame, text="🗑 Eliminar", fg_color="#e74c3c", text_color="white", width=50, command=lambda id_producto=item[0]: self.eliminar_producto(id_producto))
            btn_delete.pack(side="left", padx=5)

        for row in range(len(page_items) + 1):  # Incluye encabezados y filas de contenido
            self.frame_table.grid_rowconfigure(row, weight=1)
    
    def check_stock(self):
        for item in self.filtered_productos:
            stock = int(item[7])  # Asegúrate de que el índice 7 corresponde al stock
            if stock <= 1:
                # Mostrar alerta
                messagebox.showwarning("Alerta de Stock", f"El producto '{item[1]}' tiene un stock bajo ({stock} unidades).")

    def previous_page(self):
        """Cambia a la página anterior."""
        if self.current_page > 1:
            self.current_page -= 1
            self.populate_table()

    def next_page(self):
        """Cambia a la página siguiente."""
        if self.current_page < (len(self.filtered_productos) - 1) // self.items_per_page + 1:
            self.current_page += 1
            self.populate_table()

    def redondear_bordes(self, imagen, radio):
        """Redondea los bordes de una imagen."""
        mascara = Image.new("L", imagen.size, 0)
        draw = ImageDraw.Draw(mascara)
        draw.rounded_rectangle(
            (0, 0, imagen.size[0], imagen.size[1]),
            radius=radio, fill=255
        )
        imagen_redondeada = imagen.convert("RGBA")
        imagen_redondeada.putalpha(mascara)
        return imagen_redondeada