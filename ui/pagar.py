import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import sys
import os

# Agregar el directorio raíz al path para importar ticket
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import ticket as ti

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

        # Botón para calcular el cambio
        boton_calcular = ctk.CTkButton(modal, text="Calcular Cambio", fg_color="#007bff", text_color="white", font=("Arial", 18), )
        boton_calcular.pack(pady=10, fill="x", padx=50)

        # Botón para imprimir ticket
        boton_imprimir = ctk.CTkButton(modal, text="Imprimir Ticket", fg_color="#28a745", text_color="white", font=("Arial", 18), command=lambda: ("Efectivo"))
        boton_imprimir.pack(pady=10, fill="x", padx=50)

    # Botón para cerrar
    boton_cerrar = ctk.CTkButton(modal, text="Cerrar", fg_color="#dc3545", text_color="white", font=("Arial", 18), command=modal.destroy)
    boton_cerrar.pack(pady=10, fill="x", padx=50)

def mostrar_modal_pago(total, id_trabajador):
    """
    Muestra un modal para procesar el pago.
    
    Args:
        total (float): Total de la venta sin impuestos
    """
    # Calcular impuestos y total con impuestos
    impuesto = total * 0.16
    total_con_impuestos = total + impuesto
    
    # Crear ventana modal
    modal = ctk.CTkToplevel()
    modal.title("Procesar Pago")
    modal.geometry("400x500")
    modal.resizable(False, False)
    modal.grab_set()  # Hacer modal
    
    # Frame principal
    frame = ctk.CTkFrame(modal)
    frame.pack(padx=20, pady=20, fill="both", expand=True)
    
    # Título
    ctk.CTkLabel(
        frame,
        text="Detalles del Pago",
        font=("Arial", 20, "bold")
    ).pack(pady=10)
    
    # Desglose de pago
    desglose_frame = ctk.CTkFrame(frame)
    desglose_frame.pack(padx=10, pady=10, fill="x")
    
    # Subtotal
    ctk.CTkLabel(
        desglose_frame,
        text=f"Subtotal: ${total:.2f}",
        font=("Arial", 16)
    ).pack(anchor="w", padx=10, pady=5)
    
    # Impuesto
    ctk.CTkLabel(
        desglose_frame,
        text=f"IVA (16%): ${impuesto:.2f}",
        font=("Arial", 16)
    ).pack(anchor="w", padx=10, pady=5)
    
    # Total
    ctk.CTkLabel(
        desglose_frame,
        text=f"Total: ${total_con_impuestos:.2f}",
        font=("Arial", 18, "bold")
    ).pack(anchor="w", padx=10, pady=5)
    
    # Método de pago
    ctk.CTkLabel(
        frame,
        text="Seleccione método de pago:",
        font=("Arial", 16)
    ).pack(pady=10)
    
    # Variable para método de pago
    metodo_pago = tk.StringVar(value="efectivo")
    
    # Radio buttons para métodos de pago
    ctk.CTkRadioButton(
        frame,
        text="Efectivo",
        variable=metodo_pago,
        value="efectivo",
        font=("Arial", 14)
    ).pack(pady=5)
    
    ctk.CTkRadioButton(
        frame,
        text="Tarjeta",
        variable=metodo_pago,
        value="tarjeta",
        font=("Arial", 14)
    ).pack(pady=5)
    
    # Frame para entrada de efectivo
    efectivo_frame = ctk.CTkFrame(frame)
    efectivo_frame.pack(pady=10, fill="x", padx=20)
    
    ctk.CTkLabel(
        efectivo_frame,
        text="Efectivo recibido:",
        font=("Arial", 14)
    ).pack(side="left", padx=5)
    
    efectivo_entry = ctk.CTkEntry(
        efectivo_frame,
        font=("Arial", 14),
        width=100
    )
    efectivo_entry.pack(side="left", padx=5)
    
    # Función para mostrar/ocultar entrada de efectivo
    def toggle_efectivo():
        if metodo_pago.get() == "efectivo":
            efectivo_frame.pack(pady=10, fill="x", padx=20)
        else:
            efectivo_frame.pack_forget()
    
    # Vincular cambio de método de pago
    metodo_pago.trace("w", lambda *args: toggle_efectivo())
    
    # Botones
    botones_frame = ctk.CTkFrame(frame)
    botones_frame.pack(pady=20, fill="x", padx=20)
    
    def procesar_pago():
        try:
            if metodo_pago.get() == "efectivo":
                efectivo = float(efectivo_entry.get())
                if efectivo < total_con_impuestos:
                    messagebox.showerror("Error", "El efectivo recibido es menor al total")
                    return
                cambio = efectivo - total_con_impuestos
                messagebox.showinfo("Cambio", f"Cambio: ${cambio:.2f}")
            
            # Generar ticket
            ti.generar_ticket_pdf(total_con_impuestos, metodo_pago.get())
            messagebox.showinfo("Éxito", "Pago procesado correctamente")
            modal.destroy()
            
        except ValueError:
            messagebox.showerror("Error", "Ingrese una cantidad válida")
    
    ctk.CTkButton(
        botones_frame,
        text="Procesar Pago",
        command=procesar_pago,
        font=("Arial", 16, "bold"),
        fg_color="#28a745"
    ).pack(side="left", padx=5, expand=True, fill="x")
    
    ctk.CTkButton(
        botones_frame,
        text="Cancelar",
        command=modal.destroy,
        font=("Arial", 16, "bold"),
        fg_color="#dc3545"
    ).pack(side="left", padx=5, expand=True, fill="x")
    
    # Mostrar entrada de efectivo inicialmente
    toggle_efectivo()