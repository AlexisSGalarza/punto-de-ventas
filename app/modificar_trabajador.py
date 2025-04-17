import customtkinter as ctk
import bcrypt
from tkinter import messagebox
import app.trabajadores as db 

def modificartrabajador(id_trabajador, on_close_callback=None):
    """Abre un modal para modificar los datos de un trabajador."""
    # Crear ventana principal
    root = ctk.CTk()
    root.title("Modificar Trabajador")
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", lambda: cancelar_cliente())

    # Cuadro blanco principal
    cuadro_blanco = ctk.CTkFrame(root, fg_color="#fcf3cf")
    cuadro_blanco.grid(row=0, column=0, padx=20, pady=20)

    # Título del formulario
    titulo = ctk.CTkLabel(cuadro_blanco, text="Modificar Trabajador", font=("Arial", 32, "bold"), text_color="black")
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
    entry_nombre = crear_entry(cuadro_blanco, "Nombre")
    entry_nombre.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    entry_apellido = crear_entry(cuadro_blanco, "Apellido")
    entry_apellido.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    entry_cargo = crear_entry(cuadro_blanco, "Cargo")
    entry_cargo.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    entry_salario = crear_entry(cuadro_blanco, "Salario")
    entry_salario.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    entry_fecha = crear_entry(cuadro_blanco, "Fecha Contratación")
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
        fg_color="white",
        text_color="black",
        border_color="#f4d03f",
        font=("Arial", 20),
        show="*"
    )
    entry_contrasena.grid(row=13, column=1, padx=10, pady=10, sticky="ew")

    # Función para cargar los datos del trabajador
    def cargar_trabajador(trabajador):
        """Carga los datos de un trabajador en los campos del formulario."""
        entry_nombre.insert(0, trabajador["Nombre_tr"])
        entry_apellido.insert(0, trabajador["Apellido_tr"])
        entry_cargo.insert(0, trabajador["Cargo_tr"])
        entry_salario.insert(0, trabajador["Salario"])
        entry_fecha.insert(0, trabajador["Fecha_Contratacion_tr"])
        entry_correo.insert(0, trabajador["Correo_tr"])
        entry_telefono.insert(0, trabajador["Telefono_tr"])
        entry_rfc.insert(0, trabajador["RFC_tr"])
        entry_curp.insert(0, trabajador["CURP_tr"])
        entry_direccion.insert(0, trabajador["Direccion_tr"])
        entry_codigo_postal.insert(0, trabajador["Codigo_Postal_tr"])
        entry_usuario.insert(0, trabajador["Usuario_tr"])

    # Recuperar datos del trabajador de la base de datos
    trabajador = db.obtener_trabajador_por_id(id_trabajador)
    if trabajador:
        cargar_trabajador(trabajador)
    else:
        messagebox.showerror("Error", "No se encontró el trabajador.")
        root.destroy()

    # Función para guardar las modificaciones
    def guardar_modificaciones():
        try:
            trabajador_modificado = {
                "nombre": entry_nombre.get(),
                "apellido": entry_apellido.get(),
                "cargo": entry_cargo.get(),
                "salario": entry_salario.get(),
                "fecha_contratacion": entry_fecha.get(),
                "correo": entry_correo.get(),
                "telefono": entry_telefono.get(),
                "rfc": entry_rfc.get(),
                "curp": entry_curp.get(),
                "direccion": entry_direccion.get(),
                "codigo_postal": entry_codigo_postal.get(),
                "usuario": entry_usuario.get(),
                "contrasena": bcrypt.hashpw(entry_contrasena.get().encode('utf-8'), bcrypt.gensalt())
            }
            db.modificar_trabajador(id_trabajador, trabajador_modificado)
            messagebox.showinfo("Éxito", "Trabajador modificado exitosamente.")
            if on_close_callback:
                on_close_callback()  # Llama al callback tras guardar
            root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron guardar los cambios: {e}")

    def cancelar_cliente():
        if on_close_callback:
            on_close_callback()  # Llama al callback al cancelar
        root.destroy()

    # Botones para guardar o cancelar
    frame_botones = ctk.CTkFrame(cuadro_blanco, fg_color="#fcf3cf")
    frame_botones.grid(row=14, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

    boton_guardar = ctk.CTkButton(frame_botones, text="Guardar", fg_color="green", command=guardar_modificaciones)
    boton_guardar.grid(row=0, column=1, padx=5, pady=5)

    boton_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", fg_color="red", command=cancelar_cliente)
    boton_cancelar.grid(row=0, column=0, padx=5, pady=5)

    # Ejecutar el modal
    root.mainloop()
