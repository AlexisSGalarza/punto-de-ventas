import customtkinter as ctk
import app.clientes as db  # Asegúrate de que la función de insertar_cliente esté definida en el archivo de base de datos
from tkinter import messagebox

def agregar_cliente(on_close_callback=None):
    # Crear ventana principal
    root = ctk.CTk()
    root.resizable(False, False)  # Desactivar redimensionamiento
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    # Cuadro blanco para los widgets
    cuadro_blanco = ctk.CTkFrame(root, fg_color="#fcf3cf")
    cuadro_blanco.grid(row=0, column=0, padx=20, pady=20)

    # Título del formulario
    titulo = ctk.CTkLabel(cuadro_blanco, text="Agregar Cliente", font=("Arial", 32, "bold"), text_color="black")
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

    # Función para guardar el cliente
    def guardar_cliente():
        """Guarda el cliente en la base de datos."""
        # Validar campos obligatorios
        if not entry_nombre.get() or not entry_apellido.get() or not entry_correo.get():
            messagebox.showerror("Error", "Por favor, completa todos los campos obligatorios.")
            return
        
        # Obtener datos de los campos
        nuevo_cliente = {
            "nombre": entry_nombre.get(),
            "apellido": entry_apellido.get(),
            "correo": entry_correo.get(),
            "telefono": entry_telefono.get(),
            "direccion": entry_direccion.get(),
            "rfc": entry_rfc.get(),
            "curp": entry_curp.get(),
            "codigo_postal": entry_codigo_postal.get(),
        }

        # Guardar en la base de datos
        try:
            db.insertar_cliente(nuevo_cliente)  # Asegúrate de que esta función esté definida en tu archivo de base de datos
            messagebox.showinfo("Éxito", "Cliente guardado correctamente.")
            if on_close_callback:
                on_close_callback()  # Notificar a la ventana principal para actualizar la tabla
            root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el cliente: {e}")

    # Función para cerrar el modal
    def cancelar_cliente():
        root.destroy()

    # Botones
    frame_botones = ctk.CTkFrame(cuadro_blanco, fg_color="#fcf3cf")
    frame_botones.grid(row=9, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

    boton_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", fg_color="red", text_color="white", command=cancelar_cliente)
    boton_cancelar.grid(row=0, column=0, padx=5, sticky="e")

    boton_guardar = ctk.CTkButton(frame_botones, text="Guardar", fg_color="green", text_color="white", command=guardar_cliente)
    boton_guardar.grid(row=0, column=1, padx=5, sticky="e")

    root.mainloop()


    