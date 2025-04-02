import customtkinter as ctk
from PIL import Image, ImageDraw

# Datos de clientes con sus campos correspondientes
clientes = [
    ("CLI001", "Juan", "Pérez", "juan.perez@ejemplo.com", "555-1234", "Calle Ficticia 123, Colonia, Ciudad", "2023-01-15"),
    ("CLI002", "María", "López", "maria.lopez@ejemplo.com", "555-5678", "Avenida Siempre Viva 456, Colonia, Ciudad", "2022-09-30"),
    ("CLI003", "Carlos", "González", "carlos.gonzalez@ejemplo.com", "555-8765", "Boulevard del Sol 789, Colonia, Ciudad", "2021-06-10"),
    ("CLI004", "Ana", "Martínez", "ana.martinez@ejemplo.com", "555-4321", "Callejón del Río 101, Colonia, Ciudad", "2020-03-22"),
    ("CLI005", "Luis", "Hernández", "luis.hernandez@ejemplo.com", "555-1357", "Calle Libertad 202, Colonia, Ciudad", "2022-11-18"),
    # Generar dinámicamente clientes con sus IDs únicos
    *[
        (f"CLI{str(i).zfill(3)}", f"Nombre {i}", f"Apellido {i}", f"correo{i}@ejemplo.com", f"555-XXXX", f"Calle {i} XYZ, Colonia, Ciudad", f"202{i-5}-01-01")
        for i in range(6, 21)
    ]
]

class TiendaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("👨‍💼 Gestión de Clientes")
        self.geometry("1920x1080")
        self.configure(fg_color="#fcf3cf")

        self.current_page = 1  # Página actual
        self.items_per_page = 10  # Número de clientes por página
        self.filtered_clientes = clientes.copy()  # Lista inicial sin filtrar

        # Crear encabezado
        self.crear_encabezado()

        # Barra superior con buscador y botón "Agregar Cliente"
        self.search_frame = ctk.CTkFrame(self, fg_color="#fcf3cf")
        self.search_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.search_frame.grid_columnconfigure(0, weight=0)  # Alinear "Agregar Cliente" a la izquierda
        self.search_frame.grid_columnconfigure(1, weight=1)  # Centrar el buscador
        self.search_frame.grid_columnconfigure(2, weight=0)  # Alinear "Buscar" a la derecha

        self.add_cliente_button = ctk.CTkButton(self.search_frame, text="➕ Agregar Cliente", fg_color="#2ecc71", text_color="white", command=self.agregar_cliente)
        self.add_cliente_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.search_entry = ctk.CTkEntry(self.search_frame, placeholder_text="🔍 Buscar cliente...", width=300, fg_color="white", text_color="black")
        self.search_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.search_button = ctk.CTkButton(self.search_frame, text="Buscar", command=self.buscar_cliente, fg_color="white", text_color="black")
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        # Contenedor principal de la tabla
        self.frame_table = ctk.CTkFrame(self, fg_color="white", border_width=2, border_color="white", corner_radius=30)
        self.frame_table.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Contenedor de paginación (botones "Anterior" y "Siguiente")
        self.pagination_frame = ctk.CTkFrame(self, fg_color="#fcf3cf")
        self.pagination_frame.grid(row=3, column=0, padx=20, pady=10, sticky="e")

        self.prev_button = ctk.CTkButton(self.pagination_frame, text="⬅ Anterior", command=self.previous_page, fg_color="white", text_color="black")
        self.prev_button.grid(row=0, column=0, padx=5)

        self.next_button = ctk.CTkButton(self.pagination_frame, text="Siguiente ➡", command=self.next_page, fg_color="white", text_color="black")
        self.next_button.grid(row=0, column=1, padx=5)

        # Llenar la tabla
        self.populate_table()

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
            text="Gestionar Clientes",
            font=("Arial", 50, "bold"),
            text_color="black"
        )
        texto_encabezado.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    def buscar_cliente(self):
        """Filtra clientes según la búsqueda."""
        query = self.search_entry.get().lower()
        self.filtered_clientes = [c for c in clientes if query in c[1].lower() or query in c[2].lower()]
        self.current_page = 1
        self.populate_table()

    def populate_table(self):
        """Llena la tabla con los clientes filtrados."""
        # Limpiar la tabla existente
        for widget in self.frame_table.winfo_children():
            widget.destroy()

        # Encabezados de la tabla, incluyendo el ID del Cliente
        headers = ["ID Cliente", "Nombre", "Apellido", "Correo", "Teléfono", "Dirección", "Fecha Registro", "Acciones"]
        for col, header in enumerate(headers):
            lbl = ctk.CTkLabel(self.frame_table, text=header, font=("Arial", 18, "bold"), fg_color="#f4d03f", text_color="black")
            lbl.grid(row=0, column=col, sticky="nsew", padx=2, pady=2)  # Márgenes compactos

        # Configuración de columnas
        for col in range(len(headers)):
            if col == len(headers) - 1:  # Última columna (botones)
                self.frame_table.grid_columnconfigure(col, weight=1, minsize=150)  # Prioridad menor y tamaño mínimo
            else:
                self.frame_table.grid_columnconfigure(col, weight=2 if col < 3 else 1)

        # Obtener los clientes para la página actual
        start = (self.current_page - 1) * self.items_per_page
        end = start + self.items_per_page
        page_items = self.filtered_clientes[start:end]

        # Llenar las filas con datos
        for row, item in enumerate(page_items, start=1):
            # Insertar el ID en la primera columna
            lbl_id = ctk.CTkLabel(self.frame_table, text=item[0], font=("Arial", 14), text_color="black", padx=2)
            lbl_id.grid(row=row, column=0, sticky="nsew", pady=2)

            # Llenar las columnas restantes con los datos de 'item'
            for col, value in enumerate(item[1:]):  # Empezamos desde el índice 1 para excluir el ID
                lbl = ctk.CTkLabel(self.frame_table, text=value, font=("Arial", 14), text_color="black", padx=2)
                lbl.grid(row=row, column=col + 1, sticky="nsew", pady=2)

            # Crear un sub-contenedor para los botones de acción
            button_frame = ctk.CTkFrame(self.frame_table, fg_color="transparent")  # Marco para los botones
            button_frame.grid(row=row, column=len(headers)-1, sticky="w", padx=2, pady=2)

            # Botón Editar
            btn_edit = ctk.CTkButton(button_frame, text="✏ Editar", fg_color="#2471a3", text_color="white", width=50, height=40)
            btn_edit.pack(side="left", padx=5)  # Separación entre botones

            # Botón Eliminar
            btn_delete = ctk.CTkButton(button_frame, text="🗑 Eliminar", fg_color="#e74c3c", text_color="white", width=50,height=40)
            btn_delete.pack(side="left", padx=5)  # Separación entre botones

        # Configurar filas para que se expandan proporcionalmente
        for row in range(len(page_items) + 1):  # Incluye encabezados y filas de contenido
            self.frame_table.grid_rowconfigure(row, weight=1)

    def previous_page(self):
        """Cambia a la página anterior."""
        if self.current_page > 1:
            self.current_page -= 1
            self.populate_table()

    def next_page(self):
        """Cambia a la página siguiente."""
        if self.current_page < (len(self.filtered_clientes) - 1) // self.items_per_page + 1:
            self.current_page += 1
            self.populate_table()

    def agregar_cliente(self):
        """Función de agregar cliente aún por implementar."""
        print("Función de agregar cliente aún por implementar...")

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

if __name__ == "__main__":
    app = TiendaApp()
    app.mainloop()
