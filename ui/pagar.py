import customtkinter as ctk

def procesar_pago(metodo, modal):
    # Limpiar ventana modal
    for widget in modal.winfo_children():
        widget.destroy()

    # Si es tarjeta
    if metodo == "Tarjeta":
        label_confirmacion = ctk.CTkLabel(modal, text="Por favor, complete el pago en la terminal de tarjeta.", font=("Arial", 18), text_color="blue")
        label_confirmacion.pack(pady=20)

        # Botón para cerrar
        boton_cerrar = ctk.CTkButton(modal, text="Cerrar", fg_color="#dc3545", text_color="white", font=("Arial", 18), command=modal.destroy)
        boton_cerrar.pack(pady=10, fill="x", padx=50)

    # Si es efectivo
    elif metodo == "Efectivo":
        label_confirmacion = ctk.CTkLabel(modal, text="Ingrese la cantidad recibida:", font=("Arial", 18), text_color="black")
        label_confirmacion.pack(pady=10)

        entry_recibido = ctk.CTkEntry(modal, font=("Arial", 18), text_color="black", width=200, fg_color="white")
        entry_recibido.pack(pady=10)

        label_cambio = ctk.CTkLabel(modal, text="", font=("Arial", 18), text_color="green")
        label_cambio.pack(pady=10)

        ####








        # Botón para calcular el cambio
        boton_calcular = ctk.CTkButton(modal, text="Calcular Cambio", fg_color="#007bff", text_color="white", font=("Arial", 18), )
        boton_calcular.pack(pady=10, fill="x", padx=50)

        # Botón para imprimir ticket
        boton_imprimir = ctk.CTkButton(modal, text="Imprimir Ticket", fg_color="#28a745", text_color="white", font=("Arial", 18), command=lambda: ("Efectivo"))
        boton_imprimir.pack(pady=10, fill="x", padx=50)

    # Botón para cerrar
    boton_cerrar = ctk.CTkButton(modal, text="Cerrar", fg_color="#dc3545", text_color="white", font=("Arial", 18), command=modal.destroy)
    boton_cerrar.pack(pady=10, fill="x", padx=50)

def mostrar_modal_pago(total):
    # Crear ventana modal
    modal = ctk.CTkToplevel()
    modal.title("Pago")
    modal.geometry("600x400")
    modal.configure(fg_color="#fcf3cf")
    modal.grab_set()  # Para hacerla modal

    # Título
    label_titulo = ctk.CTkLabel(modal, text="Confirmar Pago", font=("Arial", 24, "bold"), text_color="black")
    label_titulo.pack(pady=20)

    # Mostrar total
    label_total = ctk.CTkLabel(modal, text=f"Total a Pagar: ${total}", font=("Arial", 20), text_color="black")
    label_total.pack(pady=10)

    # Botones de Pago
    boton_tarjeta = ctk.CTkButton(modal, text="Pagar con Tarjeta", fg_color="#007bff", text_color="white", font=("Arial", 18), command=lambda: procesar_pago("Tarjeta", modal))
    boton_tarjeta.pack(pady=10, fill="x", padx=50)

    boton_efectivo = ctk.CTkButton(modal, text="Pagar con Efectivo", fg_color="#28a745", text_color="white", font=("Arial", 18), command=lambda: procesar_pago("Efectivo", modal))
    boton_efectivo.pack(pady=10, fill="x", padx=50)

    # Botón Cancelar
    boton_cancelar = ctk.CTkButton(modal, text="Cancelar", fg_color="#dc3545", text_color="white", font=("Arial", 18), command=modal.destroy)
    boton_cancelar.pack(pady=20, fill="x", padx=50)