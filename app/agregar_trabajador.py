import customtkinter as ctk
import app.trabajadores as db
from tkinter import messagebox
import bcrypt

def agregartrabajador(on_close_callback=None):
    # Crear ventana principal
    root = ctk.CTk()
    root.resizable(False, False)  # Desactivar redimensionamiento
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    # Cuadro blanco para los widgets
    cuadro_blanco = ctk.CTkFrame(root, fg_color="#fcf3cf")
    cuadro_blanco.grid(row=0, column=0, padx=20, pady=20)

    # Título del formulario
    titulo = ctk.CTkLabel(cuadro_blanco, text="Agregar Empleado", font=("Arial", 32, "bold"), text_color="black")
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
    entry_nombre = crear_entry(cuadro_blanco, "Nombre")
    entry_nombre.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    entry_apellido = crear_entry(cuadro_blanco, "Apellido")
    entry_apellido.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    entry_cargo = crear_entry(cuadro_blanco, "Cargo")
    entry_cargo.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    entry_salario = crear_entry(cuadro_blanco, "Salario")
    entry_salario.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    entry_fecha = crear_entry(cuadro_blanco, "Fecha Contratación (YYYY-MM-DD)")
    entry_fecha.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    entry_correo = crear_entry(cuadro_blanco, "Correo")
    entry_correo.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

    entry_telefono = crear_entry(cuadro_blanco, "Teléfono")
    entry_telefono.grid(row=7, column=1, padx=10, pady=10, sticky="ew")

    entry_rfc = crear_entry(cuadro_blanco, "RFC")
    entry_rfc.grid(row=8, column=1, padx=10, pady=10, sticky="ew")

    entry_curp = crear_entry(cuadro_blanco, "CURP")
    entry_curp.grid(row=9, column=1, padx=10, pady=10, sticky="ew")

    entry_direccion = crear_entry(cuadro_blanco, "Dirección")
    entry_direccion.grid(row=10, column=1, padx=10, pady=10, sticky="ew")

    entry_codigo_postal = crear_entry(cuadro_blanco, "Código Postal")
    entry_codigo_postal.grid(row=11, column=1, padx=10, pady=10, sticky="ew")

    entry_usuario = crear_entry(cuadro_blanco, "Usuario")
    entry_usuario.grid(row=12, column=1, padx=10, pady=10, sticky="ew")

    entry_contrasena = ctk.CTkEntry(
        cuadro_blanco,
        placeholder_text="Contraseña",
        width=600, 
        height=40,
        fg_color="white",  # Fondo blanco
        text_color="black",  # Texto negro
        border_color="#f4d03f",  # Borde color dorado
        font=("Arial", 20),
        show="*"
    )
    entry_contrasena.grid(row=13, column=1, padx=10, pady=10, sticky="ew")

    # Función para guardar el empleado
    def guardar_empleado():
        """Guarda el empleado en la base de datos."""
        # Validar campos obligatorios
        if not entry_nombre.get() or not entry_apellido.get() or not entry_cargo.get() or not entry_fecha.get():
            messagebox.showerror("Error", "Por favor, completa todos los campos obligatorios.")
            return
        
        # Obtener datos de los campos
        nuevo_trabajador = {
            "nombre": entry_nombre.get(),
            "apellido": entry_apellido.get(),
            "cargo": entry_cargo.get(),
            "salario": float(entry_salario.get()) if entry_salario.get() else 0.0,
            "fecha_contratacion": entry_fecha.get(),
            "correo": entry_correo.get(),
            "telefono": entry_telefono.get(),
            "rfc": entry_rfc.get(),
            "curp": entry_curp.get(),
            "direccion": entry_direccion.get(),
            "codigo_postal": entry_codigo_postal.get(),
            "rol": 2,  # Por defecto, rol = 2
            "usuario": entry_usuario.get(),
            "contrasena": bcrypt.hashpw(entry_contrasena.get().encode('utf-8'), bcrypt.gensalt())
        }

        # Guardar en la base de datos
        try:
            db.insertar_trabajador(nuevo_trabajador)
            messagebox.showinfo("Éxito", "Empleado guardado correctamente.")
            if on_close_callback:
                on_close_callback()  # Notificar a la ventana principal para actualizar la tabla
            root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el empleado: {e}")

    # Función para cerrar el modal
    def cancelar_cliente():
        root.destroy()

    # Botones
    frame_botones = ctk.CTkFrame(cuadro_blanco, fg_color="#fcf3cf")
    frame_botones.grid(row=14, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

    boton_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", fg_color="red", text_color="white", command=cancelar_cliente)
    boton_cancelar.grid(row=0, column=0, padx=5, sticky="e")

    boton_guardar = ctk.CTkButton(frame_botones, text="Guardar", fg_color="green", text_color="white", command=guardar_empleado)
    boton_guardar.grid(row=0, column=1, padx=5, sticky="e")

    root.mainloop()

    