import customtkinter as ctk
import app.Productos as db # Asegúrate de que la función de insertar_producto esté definida en el archivo de base de datos
from tkinter import messagebox

def agregar_producto(on_close_callback=None):
    # Crear ventana principal
    root = ctk.CTk()
    root.resizable(False, False)  # Desactivar redimensionamiento
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    # Cuadro blanco para los widgets
    cuadro_blanco = ctk.CTkFrame(root, fg_color="#fcf3cf")
    cuadro_blanco.grid(row=0, column=0, padx=20, pady=20)

    # Título del formulario
    titulo = ctk.CTkLabel(cuadro_blanco, text="Agregar Producto", font=("Arial", 32, "bold"), text_color="black")
    titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="n")

    # Configurar las columnas del cuadro blanco
    cuadro_blanco.grid_columnconfigure(0, weight=1)
    cuadro_blanco.grid_columnconfigure(1, weight=2)

    # Función para crear entradas estilizadas
    def crear_entry(parent, placeholder):
        return ctk.CTkEntry(
            parent, 
            placeholder_text=placeholder,
            width=600, 
            height=40,
            fg_color="white",  # Fondo blanco
            text_color="black",  # Texto negro
            border_color="#f4d03f",  # Borde color dorado
            font=("Arial", 20)
        )

    # Campos de entrada con los estilos aplicados
    entry_nombre = crear_entry(cuadro_blanco, "Nombre del Producto")
    entry_nombre.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    entry_descripcion = crear_entry(cuadro_blanco, "Descripción")
    entry_descripcion.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    entry_precio = crear_entry(cuadro_blanco, "Precio ($)")
    entry_precio.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    entry_stock = crear_entry(cuadro_blanco, "Stock")
    entry_stock.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    entry_categoria = crear_entry(cuadro_blanco, "Categoría")
    entry_categoria.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    entry_proveedor = crear_entry(cuadro_blanco, "Proveedor")
    entry_proveedor.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

    entry_codigo_barras = crear_entry(cuadro_blanco, "Código de Barras")
    entry_codigo_barras.grid(row=7, column=1, padx=10, pady=10, sticky="ew")

    entry_codigo_producto = crear_entry(cuadro_blanco, "Código de Producto")
    entry_codigo_producto.grid(row=8, column=1, padx=10, pady=10, sticky="ew")

    # Función para guardar el producto
    def guardar_producto():
        """Guarda el producto en la base de datos."""
        # Validar campos obligatorios
        if not entry_nombre.get() or not entry_precio.get() or not entry_codigo_barras.get():
            messagebox.showerror("Error", "Por favor, completa todos los campos obligatorios.")
            return
        
        # Obtener datos de los campos
        nuevo_producto = {
            "nombre": entry_nombre.get(),
            "descripcion": entry_descripcion.get(),
            "precio": entry_precio.get(),
            "stock": entry_stock.get(),
            "categoria": entry_categoria.get(),
            "proveedor": entry_proveedor.get(),
            "codigo_barras": entry_codigo_barras.get(),
            "codigo_producto": entry_codigo_producto.get(),
        }

        # Guardar en la base de datos
        try:
            db.insertar_producto(nuevo_producto)  # Asegúrate de que esta función esté definida en tu archivo de base de datos
            messagebox.showinfo("Éxito", "Producto guardado correctamente.")
            if on_close_callback:
                on_close_callback()  # Notificar a la ventana principal para actualizar la tabla
            root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el producto: {e}")

    # Función para cerrar el modal
    def cancelar_producto():
        root.destroy()

    # Botones
    frame_botones = ctk.CTkFrame(cuadro_blanco, fg_color="#fcf3cf")
    frame_botones.grid(row=9, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

    boton_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", fg_color="red", text_color="white", command=cancelar_producto)
    boton_cancelar.grid(row=0, column=0, padx=5, sticky="e")

    boton_guardar = ctk.CTkButton(frame_botones, text="Guardar", fg_color="green", text_color="white", command=guardar_producto)
    boton_guardar.grid(row=0, column=1, padx=5, sticky="e")

    root.mainloop()

