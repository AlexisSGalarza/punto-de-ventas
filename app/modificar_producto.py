import customtkinter as ctk

def modificar_producto():
    # Crear ventana principal
    root = ctk.CTk()
    root.resizable(False, False)  # Desactivar redimensionamiento
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    # Cuadro blanco para los widgets
    cuadro_blanco = ctk.CTkFrame(root, fg_color="#fcf3cf")  # Color de fondo
    cuadro_blanco.grid(row=0, column=0, padx=20, pady=20)

    # Titulo del formulario
    titulo = ctk.CTkLabel(cuadro_blanco, text="Modificar Producto", font=("Arial", 32, "bold"), text_color="black")
    titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="n")

    # Configurar las columnas del cuadro blanco para distribuir los widgets
    cuadro_blanco.grid_columnconfigure(0, weight=1)
    cuadro_blanco.grid_columnconfigure(1, weight=2)

    # Campo: Nombre Producto
    etiqueta_nombre = ctk.CTkLabel(cuadro_blanco, text="Nombre Producto:", font=("Arial", 20), text_color="black")
    etiqueta_nombre.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_nombre_producto = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black",border_color="#f4d03f")
    entry_nombre_producto.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    # Campo: Descripción
    etiqueta_descripcion = ctk.CTkLabel(cuadro_blanco, text="Descripción:", font=("Arial", 20), text_color="black")
    etiqueta_descripcion.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_descripcion = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black",border_color="#f4d03f")
    entry_descripcion.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    # Campo: Precio
    etiqueta_precio = ctk.CTkLabel(cuadro_blanco, text="Precio:", font=("Arial", 20), text_color="black")
    etiqueta_precio.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    entry_precio = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black",border_color="#f4d03f")
    entry_precio.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    # Campo: Stock
    etiqueta_stock = ctk.CTkLabel(cuadro_blanco, text="Stock:", font=("Arial", 20), text_color="black")
    etiqueta_stock.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    entry_stock = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black",border_color="#f4d03f")
    entry_stock.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    # Campo: Categoría
    etiqueta_categoria = ctk.CTkLabel(cuadro_blanco, text="Categoría:", font=("Arial", 20), text_color="black")
    etiqueta_categoria.grid(row=5, column=0, padx=10, pady=10, sticky="w")
    entry_categoria = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black",border_color="#f4d03f")
    entry_categoria.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    # Campo: Proveedor
    etiqueta_proveedor = ctk.CTkLabel(cuadro_blanco, text="Proveedor:", font=("Arial", 20), text_color="black")
    etiqueta_proveedor.grid(row=6, column=0, padx=10, pady=10, sticky="w")
    entry_proveedor = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black",border_color="#f4d03f")
    entry_proveedor.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

    def modificar_producto():
        nombre_producto = entry_nombre_producto.get()
        descripcion = entry_descripcion.get()
        precio = entry_precio.get()
        stock = entry_stock.get()
        categoria = entry_categoria.get()
        proveedor = entry_proveedor.get()
        
        # Lógica para modificar producto en la base de datos
        print(f"Producto modificado: {nombre_producto}, Precio: {precio}, Stock: {stock}")
    def cancelar_cliente():
        root.destroy()  # Cierra la ventana principal

    # Frame para los botones centrados
    frame_botones = ctk.CTkFrame(cuadro_blanco, fg_color="#fcf3cf")
    frame_botones.grid(row=7, column=0, columnspan=2,padx=20, pady=10, sticky="ew")

    frame_botones.grid_columnconfigure(0, weight=1)
    frame_botones.grid_columnconfigure(1, weight=1)

    boton_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", font=("Arial", 20), fg_color="red", text_color="white", command=cancelar_cliente)
    boton_cancelar.grid(row=0, column=0, padx=5, sticky="e")

    boton_guardar = ctk.CTkButton(frame_botones, text="Guardar", font=("Arial", 20), fg_color="green", text_color="white", command=modificar_producto)
    boton_guardar.grid(row=0, column=1, padx=5, sticky="e")

    root.mainloop()

