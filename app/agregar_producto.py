import customtkinter as ctk

# Crear ventana principal
def agregarproducto():
    root = ctk.CTk()
    root.resizable(False, False)  # Desactivar redimensionamiento
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    # Cuadro blanco para los widgets
    cuadro_blanco = ctk.CTkFrame(root, fg_color="#fcf3cf")  # Color de fondo
    cuadro_blanco.grid(row=0, column=0, padx=20, pady=20)

    # Título del formulario
    titulo = ctk.CTkLabel(cuadro_blanco, text="Agregar Producto", font=("Arial", 32, "bold"), text_color="black")
    titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="n")

    cuadro_blanco.grid_columnconfigure(0, weight=1)
    cuadro_blanco.grid_columnconfigure(1, weight=2)

    # Crear entradas de datos
    campos = ["Nombre Producto:", "Descripción:", "Precio:", "Stock:", "Categoría:", "Proveedor:"]
    entradas = {}

    for i, campo in enumerate(campos):
        etiqueta = ctk.CTkLabel(cuadro_blanco, text=campo, font=("Arial", 20), text_color="black")
        etiqueta.grid(row=i+1, column=0, padx=10, pady=10, sticky="w")

        entrada = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black", border_color="#f4d03f")
        entrada.grid(row=i+1, column=1, padx=10, pady=10, sticky="ew")

        entradas[campo] = entrada  # Guardar referencia de la entrada en el diccionario

    # Función para agregar el producto
    def agregar_producto():
        datos = {campo: entradas[campo].get() for campo in campos}
        print(f"Producto agregado: {datos}")

    # Función para cerrar la ventana
    def cancelar_producto():
        root.destroy()

    # Frame para los botones
    frame_botones = ctk.CTkFrame(cuadro_blanco, fg_color="#fcf3cf")
    frame_botones.grid(row=len(campos)+1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
    
    frame_botones.grid_columnconfigure(0, weight=1)
    frame_botones.grid_columnconfigure(1, weight=1)

    # Botón Cancelar
    boton_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", font=("Arial", 20), fg_color="red", text_color="white", command=cancelar_producto)
    boton_cancelar.grid(row=0, column=0, padx=5, sticky="e")

    # Botón Guardar
    boton_guardar = ctk.CTkButton(frame_botones, text="Guardar", font=("Arial", 20), fg_color="green", text_color="white", command=agregar_producto)
    boton_guardar.grid(row=0, column=1, padx=5, sticky="e")

    root.mainloop()


