import customtkinter as ctk

def mostrar_modal_pago(total):
    # Crear ventana modal
    modal = ctk.CTkToplevel()
    modal.title("Pago")
    modal.geometry("400x300")
    modal.configure(fg_color="white")
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
