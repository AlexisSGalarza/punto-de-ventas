import customtkinter as ctk
import bcrypt
from tkinter import messagebox
import app.clientes as db

def modificar_cliente(id_cliente, on_close_callback=None):
    """Abre un modal para modificar los datos de un cliente."""
    # Crear ventana principal
    root = ctk.CTk()
    root.title("Modificar Cliente")
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", lambda: cancelar_cliente())

    # Cuadro blanco principal
    cuadro_blanco = ctk.CTkFrame(root, fg_color="#fcf3cf")
    cuadro_blanco.grid(row=0, column=0, padx=20, pady=20)

    # Título del formulario
    titulo = ctk.CTkLabel(cuadro_blanco, text="Modificar Cliente", font=("Arial", 32, "bold"), text_color="black")
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

    entry_correo = crear_entry(cuadro_blanco, "Correo")
    entry_correo.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    entry_telefono = crear_entry(cuadro_blanco, "Teléfono")
    entry_telefono.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

    entry_direccion = crear_entry(cuadro_blanco, "Dirección")
    entry_direccion.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    entry_rfc = crear_entry(cuadro_blanco, "RFC")
    entry_rfc.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

    entry_curp = crear_entry(cuadro_blanco, "CURP")
    entry_curp.grid(row=7, column=1, padx=10, pady=10, sticky="ew")

    entry_codigo_postal = crear_entry(cuadro_blanco, "Código Postal")
    entry_codigo_postal.grid(row=8, column=1, padx=10, pady=10, sticky="ew")

    # Función para cargar los datos del cliente
    def cargar_cliente(cliente):
        print(cliente) 
        """Carga los datos de un cliente en los campos del formulario."""
        entry_nombre.insert(0, cliente["Nombre_cl"])  # Cambiar a 'Nombre_cl'
        entry_apellido.insert(0, cliente["Apellido_cl"])  # Cambiar a 'Apellido_cl'
        entry_correo.insert(0, cliente["Correo_cl"])  # Cambiar a 'Correo_cl'
        entry_telefono.insert(0, cliente["Telefono_cl"])  # Cambiar a 'Telefono_cl'
        entry_direccion.insert(0, cliente["Direccion_cl"])  # Cambiar a 'Direccion_cl'
        entry_rfc.insert(0, cliente["RFC_cl"])  # Cambiar a 'RFC_cl'
        entry_curp.insert(0, cliente["CURP_cl"])  # Cambiar a 'CURP_cl'
        entry_codigo_postal.insert(0, cliente["Codigo_Postal_cl"])

    # Recuperar datos del cliente de la base de datos
    cliente = db.obtener_cliente_por_id(id_cliente)  # Debes implementar esta función
    if cliente:
        cargar_cliente(cliente)
    else:
        messagebox.showerror("Error", "No se encontró el cliente.")
        root.destroy()

    # Función para guardar las modificaciones
    def guardar_modificaciones():
        try:
            cliente_modificado = {
                "nombre": entry_nombre.get(),
                "apellido": entry_apellido.get(),
                "correo": entry_correo.get(),
                "telefono": entry_telefono.get(),
                "direccion": entry_direccion.get(),
                "rfc": entry_rfc.get(),
                "curp": entry_curp.get(),
                "codigo_postal": entry_codigo_postal.get()
            }
            db.modificar_cliente(id_cliente, cliente_modificado)  # Implementa esta función para guardar en la base de datos
            messagebox.showinfo("Éxito", "Cliente modificado exitosamente.")
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
    frame_botones.grid(row=9, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

    boton_guardar = ctk.CTkButton(frame_botones, text="Guardar", fg_color="green", command=guardar_modificaciones)
    boton_guardar.grid(row=0, column=1, padx=5, pady=5)

    boton_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", fg_color="red", command=cancelar_cliente)
    boton_cancelar.grid(row=0, column=0, padx=5, pady=5)

    # Ejecutar el modal
    root.mainloop()
