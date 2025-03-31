import customtkinter as ctk

# Crear ventana principal
root = ctk.CTk()

# Cuadro blanco para los widgets
cuadro_blanco = ctk.CTkFrame(root, fg_color="#fcf3cf")  # Color de fondo
cuadro_blanco.grid(row=0, column=0, padx=20, pady=20)

# Titulo del formulario
titulo = ctk.CTkLabel(cuadro_blanco, text="Modificar Cliente", font=("Arial", 32, "bold"), text_color="black")
titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="n")

# Configurar las columnas del cuadro blanco para distribuir los widgets
cuadro_blanco.grid_columnconfigure(0, weight=1)
cuadro_blanco.grid_columnconfigure(1, weight=2)

# Campo: Nombre
etiqueta_nombre = ctk.CTkLabel(cuadro_blanco, text="Nombre:", font=("Arial", 20), text_color="black")
etiqueta_nombre.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_nombre = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_nombre.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Campo: Apellido
etiqueta_apellido = ctk.CTkLabel(cuadro_blanco, text="Apellido:", font=("Arial", 20), text_color="black")
etiqueta_apellido.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_apellido = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_apellido.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

# Campo: Correo
etiqueta_correo = ctk.CTkLabel(cuadro_blanco, text="Correo:", font=("Arial", 20), text_color="black")
etiqueta_correo.grid(row=3, column=0, padx=10, pady=10, sticky="w")
entry_correo = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_correo.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

# Campo: Teléfono
etiqueta_telefono = ctk.CTkLabel(cuadro_blanco, text="Teléfono:", font=("Arial", 20), text_color="black")
etiqueta_telefono.grid(row=4, column=0, padx=10, pady=10, sticky="w")
entry_telefono = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_telefono.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

# Campo: Dirección
etiqueta_direccion = ctk.CTkLabel(cuadro_blanco, text="Dirección:", font=("Arial", 20), text_color="black")
etiqueta_direccion.grid(row=5, column=0, padx=10, pady=10, sticky="w")
entry_direccion = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_direccion.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

# Campo: RFC
etiqueta_rfc = ctk.CTkLabel(cuadro_blanco, text="RFC:", font=("Arial", 20), text_color="black")
etiqueta_rfc.grid(row=6, column=0, padx=10, pady=10, sticky="w")
entry_rfc = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_rfc.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

# Campo: CURP
etiqueta_curp = ctk.CTkLabel(cuadro_blanco, text="CURP:", font=("Arial", 20), text_color="black")
etiqueta_curp.grid(row=7, column=0, padx=10, pady=10, sticky="w")
entry_curp = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_curp.grid(row=7, column=1, padx=10, pady=10, sticky="ew")

# Campo: Código Postal
etiqueta_codigo_postal = ctk.CTkLabel(cuadro_blanco, text="Código Postal:", font=("Arial", 20), text_color="black")
etiqueta_codigo_postal.grid(row=8, column=0, padx=10, pady=10, sticky="w")
entry_codigo_postal = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_codigo_postal.grid(row=8, column=1, padx=10, pady=10, sticky="ew")

# Botón de Modificar
def modificar_cliente():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    correo = entry_correo.get()
    telefono = entry_telefono.get()
    direccion = entry_direccion.get()
    rfc = entry_rfc.get()
    curp = entry_curp.get()
    codigo_postal = entry_codigo_postal.get()
    # Lógica para modificar cliente en la base de datos
    print(f"Cliente modificado: {nombre} {apellido}, Correo: {correo}")

boton_guardar = ctk.CTkButton(cuadro_blanco, text="Modificar", font=("Arial", 20), fg_color="blue", text_color="white", command=modificar_cliente)
boton_guardar.grid(row=9, column=0, columnspan=2, padx=10, pady=20, sticky="n")

# Iniciar la ventana principal
root.mainloop()