import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import sys
import os

# Agregar el directorio raíz al path para importar ticket
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import ticket as ti

def procesar_pago(metodo, modal, total_con_impuestos):
    # Limpiar ventana modal
    for widget in modal.winfo_children():
        widget.destroy()

    # Función para cerrar el modal de forma segura
    def cerrar_modal():
        try:
            print("Cerrando modal...")  # Depuración
            modal.destroy()
        except Exception as e:
            print(f"Error al cerrar el modal: {e}")

    # Si es tarjeta
    if metodo == "Tarjeta":
        label_confirmacion = ctk.CTkLabel(modal, text="Pago completado con tarjeta.", font=("Arial", 18), text_color="blue")
        label_confirmacion.pack(pady=20)

        # Mostrar mensaje de éxito y cerrar modal
        messagebox.showinfo("Éxito", "Pago completado con tarjeta.")
        cerrar_modal()

    # Si es efectivo
    elif metodo == "Efectivo":
        label_confirmacion = ctk.CTkLabel(modal, text="Ingrese la cantidad recibida:", font=("Arial", 18), text_color="black")
        label_confirmacion.pack(pady=10)

        entry_recibido = ctk.CTkEntry(modal, font=("Arial", 18), text_color="black", width=200, fg_color="white")
        entry_recibido.pack(pady=10)

        label_cambio = ctk.CTkLabel(modal, text="", font=("Arial", 18), text_color="green")
        label_cambio.pack(pady=10)

        def calcular_cambio():
            try:
                efectivo = float(entry_recibido.get())
                if efectivo < total_con_impuestos:
                    messagebox.showerror("Error", "El efectivo recibido es menor al total.")
                    return
                cambio = efectivo - total_con_impuestos
                label_cambio.configure(text=f"Cambio: ${cambio:.2f}")

                # Mostrar mensaje de éxito y cerrar modal
                messagebox.showinfo("Éxito", f"Pago completado. Cambio: ${cambio:.2f}")
                cerrar_modal()
            except ValueError:
                messagebox.showerror("Error", "Ingrese una cantidad válida.")

        # Botón para calcular el cambio y cerrar
        boton_calcular = ctk.CTkButton(modal, text="Calcular y Cerrar", fg_color="#007bff", text_color="white", font=("Arial", 18), command=calcular_cambio)
        boton_calcular.pack(pady=10, fill="x", padx=50)

def mostrar_modal_pago(total, id_trabajador, app_state, carrito):
    """
    Muestra un modal para procesar el pago.
    
    Args:
        total (float): Total de la venta sin impuestos
        id_trabajador (int): ID del trabajador que realiza la venta
        app_state (AppState): Estado global de la aplicación
        carrito (list): Lista de productos en el carrito
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
    metodo_pago = tk.StringVar(value="Efectivo")

    # Radio buttons para métodos de pago
    ctk.CTkRadioButton(
        frame,
        text="Efectivo",
        variable=metodo_pago,
        value="Efectivo",
        font=("Arial", 14)
    ).pack(pady=5)

    ctk.CTkRadioButton(
        frame,
        text="Tarjeta",
        variable=metodo_pago,
        value="Tarjeta",
        font=("Arial", 14)
    ).pack(pady=5)

    # Entrada de efectivo
    efectivo_entry = ctk.CTkEntry(frame, font=("Arial", 14), placeholder_text="Ingrese efectivo recibido")

    def toggle_efectivo(show):
        if show:
            efectivo_entry.pack(pady=10, fill="x", padx=20)
        else:
            efectivo_entry.pack_forget()

    # Mostrar entrada de efectivo inicialmente si el método es efectivo
    toggle_efectivo(metodo_pago.get() == "Efectivo")

    def actualizar_metodo_pago(*args):
        toggle_efectivo(metodo_pago.get() == "Efectivo")

    metodo_pago.trace_add("write", actualizar_metodo_pago)

    def procesar_pago():
        try:
            if metodo_pago.get() == "Efectivo":
                try:
                    efectivo = float(efectivo_entry.get())
                    if efectivo < total_con_impuestos:
                        messagebox.showerror("Error", "El efectivo recibido es menor al total.")
                        return
                    cambio = efectivo - total_con_impuestos
                    messagebox.showinfo("Éxito", f"Pago completado. Cambio: ${cambio:.2f}")

                    # Generar ticket con método de pago y detalles
                    ti.generar_ticket_pdf(
                        total_con_impuestos,
                        "Efectivo",
                        app_state.get_current_user_name(),
                        carrito
                    )
                except ValueError:
                    messagebox.showerror("Error", "Ingrese una cantidad válida.")
            elif metodo_pago.get() == "Tarjeta":
                detalles = [
                    {
                        "Producto": item["nombre"],
                        "Cantidad": item["cantidad"],
                        "Precio": f"${item['precio_unitario']:.2f}",
                        "Subtotal": f"${item['subtotal']:.2f}"
                    }
                    for item in carrito
                ]

                # Generar ticket con método de pago y detalles
                ti.generar_ticket_pdf(
                    total_con_impuestos,
                    "Tarjeta",
                    app_state.get_current_user_name(),
                    detalles
                )
        except Exception as e:
            print(f"Error durante el procesamiento del pago: {e}")
        finally:
            print("Cerrando modal...")
            modal.destroy()

    # Botones
    botones_frame = ctk.CTkFrame(frame)
    botones_frame.pack(pady=20, fill="x", padx=20)

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