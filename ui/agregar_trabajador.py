import customtkinter as ctk

def agregartrabajador():
    # Crear ventana principal
    root = ctk.CTk()
    root.resizable(False, False)  # Desactivar redimensionamiento
    root.protocol("WM_DELETE_WINDOW", lambda: None)
    # Cuadro blanco para los widgets
    cuadro_blanco = ctk.CTkFrame(root,fg_color="#fcf3cf")
    cuadro_blanco.grid(row=0, column=0, padx=20, pady=20)

    # Titulo del formulario
    titulo = ctk.CTkLabel(cuadro_blanco, text="Agregar Empleado", font=("Arial", 32, "bold"), text_color="black")
    titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="n")

    # Configurar las columnas del cuadro blanco para distribuir los widgets
    cuadro_blanco.grid_columnconfigure(0, weight=1)
    cuadro_blanco.grid_columnconfigure(1, weight=2)

    # Campo: Nombre
    etiqueta_nombre = ctk.CTkLabel(cuadro_blanco, text="Nombre:", font=("Arial", 20), text_color="black")
    etiqueta_nombre.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_nombre = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="white",border_color="#f4d03f")
    entry_nombre.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    # Campo: Apellido
    etiqueta_apellido = ctk.CTkLabel(cuadro_blanco, text="Apellido:", font=("Arial", 20), text_color="black")
    etiqueta_apellido.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_apellido = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="white",border_color="#f4d03f")
    entry_apellido.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    # Campo: Cargo
    etiqueta_cargo = ctk.CTkLabel(cuadro_blanco, text="Cargo:", font=("Arial", 20), text_color="black")
    etiqueta_cargo.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    entry_cargo = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="white",border_color="#f4d03f")
    entry_cargo.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    # Campo: Salario
    etiqueta_salario = ctk.CTkLabel(cuadro_blanco, text="Salario:", font=("Arial", 20), text_color="black")
    etiqueta_salario.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    entry_salario = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="white",border_color="#f4d03f")
    entry_salario.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    # Campo: Fecha de Contratación
    etiqueta_fecha = ctk.CTkLabel(cuadro_blanco, text="Fecha de Contratación:", font=("Arial", 20), text_color="black")
    etiqueta_fecha.grid(row=5, column=0, padx=10, pady=10, sticky="w")
    entry_fecha = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="white",border_color="#f4d03f")
    entry_fecha.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    # Campo: Correo
    etiqueta_correo = ctk.CTkLabel(cuadro_blanco, text="Correo:", font=("Arial", 20), text_color="black")
    etiqueta_correo.grid(row=6, column=0, padx=10, pady=10, sticky="w")
    entry_correo = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="white",border_color="#f4d03f")
    entry_correo.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

    # Campo: Teléfono
    etiqueta_telefono = ctk.CTkLabel(cuadro_blanco, text="Teléfono:", font=("Arial", 20), text_color="black")
    etiqueta_telefono.grid(row=7, column=0, padx=10, pady=10, sticky="w")
    entry_telefono = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="white",border_color="#f4d03f")
    entry_telefono.grid(row=7, column=1, padx=10, pady=10, sticky="ew")

    # Campo: RFC
    etiqueta_rfc = ctk.CTkLabel(cuadro_blanco, text="RFC:", font=("Arial", 20), text_color="black")
    etiqueta_rfc.grid(row=8, column=0, padx=10, pady=10, sticky="w")
    entry_rfc = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="white",border_color="#f4d03f")
    entry_rfc.grid(row=8, column=1, padx=10, pady=10, sticky="ew")

    # Campo: CURP
    etiqueta_curp = ctk.CTkLabel(cuadro_blanco, text="CURP:", font=("Arial", 20), text_color="black")
    etiqueta_curp.grid(row=9, column=0, padx=10, pady=10, sticky="w")
    entry_curp = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="white",border_color="#f4d03f")
    entry_curp.grid(row=9, column=1, padx=10, pady=10, sticky="ew")

    # Campo: Dirección
    etiqueta_direccion = ctk.CTkLabel(cuadro_blanco, text="Dirección:", font=("Arial", 20), text_color="black")
    etiqueta_direccion.grid(row=10, column=0, padx=10, pady=10, sticky="w")
    entry_direccion = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="white",border_color="#f4d03f")
    entry_direccion.grid(row=10, column=1, padx=10, pady=10, sticky="ew")

    # Campo: Código Postal
    etiqueta_codigo_postal = ctk.CTkLabel(cuadro_blanco, text="Código Postal:", font=("Arial", 20), text_color="black")
    etiqueta_codigo_postal.grid(row=11, column=0, padx=10, pady=10, sticky="w")
    entry_codigo_postal = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="white",border_color="#f4d03f")
    entry_codigo_postal.grid(row=11, column=1, padx=10, pady=10, sticky="ew")

    # Campo: Usuario
    etiqueta_usuario = ctk.CTkLabel(cuadro_blanco, text="Usuario:", font=("Arial", 20), text_color="black")
    etiqueta_usuario.grid(row=12, column=0, padx=10, pady=10, sticky="w")
    entry_usuario = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="white",border_color="#f4d03f")
    entry_usuario.grid(row=12, column=1, padx=10, pady=10, sticky="ew")

    # Campo: Contraseña
    etiqueta_contrasena = ctk.CTkLabel(cuadro_blanco, text="Contraseña:", font=("Arial", 20), text_color="black")
    etiqueta_contrasena.grid(row=13, column=0, padx=10, pady=10, sticky="w")
    entry_contrasena = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="white",border_color="#f4d03f", show="*")
    entry_contrasena.grid(row=13, column=1, padx=10, pady=10, sticky="ew")



    # Función para guardar el empleado y asignar el rol automáticamente
    def guardar_empleado():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        cargo = entry_cargo.get()
        salario = entry_salario.get()
        fecha_contratacion = entry_fecha.get()
        correo = entry_correo.get()
        telefono = entry_telefono.get()
        rfc = entry_rfc.get()
        curp = entry_curp.get()
        direccion = entry_direccion.get()
        codigo_postal = entry_codigo_postal.get()
        usuario = entry_usuario.get()
        contrasena = entry_contrasena.get()

        # Asignar rol automáticamente
        rol = 2  # Por ejemplo, por defecto, será trabajador (2), puedes cambiar esto si tienes alguna lógica para asignar rol.

        # Lógica para guardar los datos (por ejemplo, en una base de datos)
        print(f"Empleado {nombre} {apellido} guardado con rol {rol}")

    def cancelar_cliente():
        root.destroy()  # Cierra la ventana principal

    # Frame para los botones centrados
    frame_botones = ctk.CTkFrame(cuadro_blanco, fg_color="#fcf3cf")
    frame_botones.grid(row=14, column=0, columnspan=2,padx=20, pady=10, sticky="ew")

    frame_botones.grid_columnconfigure(0, weight=1)
    frame_botones.grid_columnconfigure(1, weight=1)

    boton_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", font=("Arial", 20), fg_color="red", text_color="white", command=cancelar_cliente)
    boton_cancelar.grid(row=0, column=0, padx=5, sticky="e")

    boton_guardar = ctk.CTkButton(frame_botones, text="Guardar", font=("Arial", 20), fg_color="green", text_color="white", command=guardar_empleado)
    boton_guardar.grid(row=0, column=1, padx=5, sticky="e")
    # Iniciar la ventana principal
    root.mainloop()