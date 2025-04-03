import customtkinter as ctk

def eliminar_cliente():
    """Crea un modal para confirmar la acción."""
    # Crear la ventana modal
    modal = ctk.CTkToplevel()
    modal.title("Confirmación")
    modal.geometry("400x200")  # Tamaño del modal
    modal.grab_set()  # Bloquear interacción con la ventana principal
    modal.configure(fg_color="#fcf3cf")

    modal.resizable(False, False)
    modal.protocol("WM_DELETE_WINDOW", lambda: None)
    # Centrar el modal en la pantalla
    screen_width = modal.winfo_screenwidth()
    screen_height = modal.winfo_screenheight()
    modal_width = 400
    modal_height = 200
    x = (screen_width - modal_width) // 2
    y = (screen_height - modal_height) // 2
    modal.geometry(f"{modal_width}x{modal_height}+{x}+{y}")

    # Texto de confirmación
    etiqueta_confirmacion = ctk.CTkLabel(
        modal, text="¿Estás seguro de realizar esta acción?", 
        font=("Arial", 18, "bold"), text_color="black"
    )
    etiqueta_confirmacion.pack(pady=20)

    # Botones en el modal
    frame_botones = ctk.CTkFrame(modal, fg_color="transparent")
    frame_botones.pack(pady=20, fill="x")

    def confirmar_accion():
        print("Acción confirmada.")  # Aquí puedes vincular tu lógica
        modal.destroy()

    def cancelar_accion():
        print("Acción cancelada.")  # Cierra el modal si cancelas
        modal.destroy()

    boton_confirmar = ctk.CTkButton(
        frame_botones, text="Confirmar", 
        fg_color="green", text_color="white", 
        command=confirmar_accion
    )
    boton_confirmar.pack(side="left", padx=10)

    boton_cancelar = ctk.CTkButton(
        frame_botones, text="Cancelar", 
        fg_color="red", text_color="white", 
        command=cancelar_accion
    )
    boton_cancelar.pack(side="right", padx=10)




