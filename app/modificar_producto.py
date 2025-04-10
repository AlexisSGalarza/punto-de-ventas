import customtkinter as ctk
from tkinter import messagebox
import app.Productos as db  # Asegúrate de que las funciones necesarias estén definidas en tu módulo de base de datos

def modificar_producto(id_producto, on_close_callback=None):
    """Abre un modal para modificar los datos de un producto."""
    # Crear ventana principal
    root = ctk.CTk()
    root.title("Modificar Producto")
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", lambda: cancelar_producto())

    # Cuadro blanco principal
    cuadro_blanco = ctk.CTkFrame(root, fg_color="#fcf3cf")
    cuadro_blanco.grid(row=0, column=0, padx=20, pady=20)

    # Título del formulario
    titulo = ctk.CTkLabel(cuadro_blanco, text="Modificar Producto", font=("Arial", 32, "bold"), text_color="black")
    titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="n")

    # Configurar columnas del cuadro blanco
    cuadro_blanco.grid_columnconfigure(0, weight=1)
    cuadro_blanco.grid_columnconfigure(1, weight=2)

    # Función para crear entradas estilizadas
    def crear_entry(parent, placeholder):
        return ctk.CTkEntry(
            parent,
            placeholder_text=placeholder,
            width=600,
            height=40,
            fg_color="white",
            text_color="black",
            border_color="#f4d03f",
            font=("Arial", 20)
        )

    # Campos del formulario
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

    # Función para cargar los datos del producto
    def cargar_producto(producto):
        """Carga los datos de un producto en los campos del formulario."""
        entry_nombre.insert(0, producto["Nombre_pr"])
        entry_descripcion.insert(0, producto["Descripcion_pr"])
        entry_precio.insert(0, str(producto["Precio_pr"]))
        entry_stock.insert(0, str(producto["Stock_pr"]))
        entry_categoria.insert(0, producto["Categoria_pr"])
        entry_proveedor.insert(0, producto["Proveedor_pr"])
        entry_codigo_barras.insert(0, producto["codigo_barras_pr"])
        entry_codigo_producto.insert(0, producto["codigo_producto_pr"])

    # Recuperar datos del producto de la base de datos
    producto = db.obtener_producto_por_id(id_producto)  # Implementa esta función en tu módulo de base de datos
    if producto:
        cargar_producto(producto)
    else:
        messagebox.showerror("Error", "No se encontró el producto.")
        root.destroy()

    # Función para guardar las modificaciones
    def guardar_modificaciones():
        try:
            producto_modificado = {
                "nombre": entry_nombre.get(),
                "descripcion": entry_descripcion.get(),
                "precio": float(entry_precio.get()),
                "stock": int(entry_stock.get()),
                "categoria": entry_categoria.get(),
                "proveedor": entry_proveedor.get(),
                "codigo_barras": entry_codigo_barras.get(),
                "codigo_producto": entry_codigo_producto.get()
            }
            db.modificar_producto(id_producto, producto_modificado)  # Implementa esta función
            messagebox.showinfo("Éxito", "Producto modificado exitosamente.")
            if on_close_callback:
                on_close_callback()  # Llama al callback tras guardar
            root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron guardar los cambios: {e}")

    # Función para cancelar las modificaciones
    def cancelar_producto():
        if on_close_callback:
            on_close_callback()  # Llama al callback al cancelar
        root.destroy()

    # Botones para guardar o cancelar
    frame_botones = ctk.CTkFrame(cuadro_blanco, fg_color="#fcf3cf")
    frame_botones.grid(row=9, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

    boton_guardar = ctk.CTkButton(frame_botones, text="Guardar", fg_color="green", command=guardar_modificaciones)
    boton_guardar.grid(row=0, column=1, padx=5, pady=5)

    boton_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", fg_color="red", command=cancelar_producto)
    boton_cancelar.grid(row=0, column=0, padx=5, pady=5)

    # Ejecutar el modal
    root.mainloop()