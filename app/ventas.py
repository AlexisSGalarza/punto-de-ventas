import customtkinter as ctk
from PIL import Image, ImageOps, ImageDraw
from tkinter import Scrollbar


def redondear_bordes(imagen, radio):
    mascara = Image.new("L", imagen.size, 0)
    draw = ImageDraw.Draw(mascara)
    draw.rounded_rectangle(
        (0, 0, imagen.size[0], imagen.size[1]),
        radius=radio, fill=255
    )

    imagen_redondeada = imagen.convert("RGBA")
    imagen_redondeada.putalpha(mascara)
    return imagen_redondeada

def encabezado(ventana):
    # Encabezado principal
    encabezado = ctk.CTkFrame(ventana, fg_color="#f4d03f", height=100)
    encabezado.grid(row=0, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

    franja_roja = ctk.CTkFrame(encabezado, fg_color="#f11919", height=20)
    franja_roja.grid(row=1, column=0, columnspan=3, sticky="ew")
    
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=1)
    ventana.grid_columnconfigure(2, weight=1)
    
    logo_imagen = Image.open("assets/logo.jpg")
    logo_imagen_redondeada = redondear_bordes(logo_imagen, radio=75)
    logo_imagen_ctk = ctk.CTkImage(logo_imagen_redondeada, size=(100, 100))
    
    logo = ctk.CTkLabel(encabezado, image=logo_imagen_ctk, text="")
    logo.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    
    texto_encabezado = ctk.CTkLabel(
        encabezado,
        text="Tienda 'Abarrotes Gael'",
        font=("Arial", 50, "bold"),
        text_color="black"
    )
    texto_encabezado.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    encabezado.grid_columnconfigure(1, weight=1)

def informacion_venta(ventana):
    # Información de venta (nueva sección)
    info_venta = ctk.CTkFrame(ventana, fg_color="#fcf3cf")
    info_venta.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

    info_venta.grid_columnconfigure(0, weight=1)
    info_venta.grid_columnconfigure(1, weight=1)
    info_venta.grid_columnconfigure(2, weight=1)

    etiqueta_fecha = ctk.CTkLabel(
        info_venta,
        text="Fecha: 23/03/2025",
        font=("Arial", 20),
        text_color="black"
    )
    etiqueta_fecha.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    etiqueta_hora = ctk.CTkLabel(
        info_venta,
        text="Hora: 07:05 p.m.",
        font=("Arial", 20),
        text_color="black"
    )
    etiqueta_hora.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    etiqueta_numero_venta = ctk.CTkLabel(
        info_venta,
        text="No. de Venta: 0000000001",
        font=("Arial", 20, "bold"),
        text_color="black"
    )
    etiqueta_numero_venta.grid(row=0, column=2, rowspan=2, padx=10, pady=5, sticky="e")

def tabla_encabezados(ventana):
    # Tabla de encabezados (nueva sección)
    cuadro_campos = ctk.CTkFrame(ventana, fg_color="#f4d03f", corner_radius=10)
    cuadro_campos.grid(row=2, column=0, columnspan=3, padx=20, pady=(10), sticky="nsew")

    cuadro_campos.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

    etiquetas = ["No.", "Producto", "Código", "Precio", "Cantidad"]
    for i, texto in enumerate(etiquetas):
        etiqueta = ctk.CTkLabel(
            cuadro_campos,
            text=texto,
            font=("Arial", 20, "bold"),
            text_color="black"
        )
        etiqueta.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")
    
    

    contenedor_scroll = ctk.CTkFrame(ventana)
    contenedor_scroll.grid(row=3, column=0, columnspan=3, padx=20, pady=(10), sticky="nsew")
    contenedor_scroll.grid_columnconfigure(0, weight=1)
    contenedor_scroll.grid_rowconfigure(0, weight=1)

    # Canvas para habilitar scroll
    canvas = ctk.CTkCanvas(contenedor_scroll, highlightthickness=0, width=900, height=500, bg="white")
    canvas.grid(row=0, column=0, sticky="nsew")

    # Scrollbar vinculado al canvas
    scrollbar = Scrollbar(contenedor_scroll, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Cuadro amarillo dentro del canvas con tamaño ajustado
    cuadro_productos = ctk.CTkFrame(canvas, fg_color="white", corner_radius=10)
    canvas.create_window((0, 0), window=cuadro_productos, anchor="nw", width=1900)

    # Ajustar automáticamente el área del scroll
    def ajustar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    cuadro_productos.bind("<Configure>", ajustar_scroll)

    # Configurar el cuadro amarillo para ocupar todo el espacio disponible
    cuadro_productos.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

    # Añadir filas dinámicas de datos
    datos = [
        {"No.": f"{i+1}", "Producto": f"Producto {i+1}", "Código": f"Código {i+1}", "Precio": f"${22.00+i}", "Cantidad": f"{3+i}"}
        for i in range(10)  # Generar 50 productos para probar el scroll
    ]

    for fila, dato in enumerate(datos):
        etiqueta_no = ctk.CTkLabel(cuadro_productos, text=dato["No."], font=("Arial", 18), text_color="black")
        etiqueta_no.grid(row=fila, column=0, padx=10, pady=5, sticky="nsew")

        etiqueta_producto = ctk.CTkLabel(cuadro_productos, text=dato["Producto"], font=("Arial", 18), text_color="black")
        etiqueta_producto.grid(row=fila, column=1, padx=10, pady=5, sticky="nsew")

        etiqueta_codigo = ctk.CTkLabel(cuadro_productos, text=dato["Código"], font=("Arial", 18), text_color="black")
        etiqueta_codigo.grid(row=fila, column=2, padx=10, pady=5, sticky="nsew")

        etiqueta_precio = ctk.CTkLabel(cuadro_productos, text=dato["Precio"], font=("Arial", 18), text_color="black")
        etiqueta_precio.grid(row=fila, column=3, padx=10, pady=5, sticky="nsew")

        campo_cantidad = ctk.CTkEntry(cuadro_productos, font=("Arial", 18), text_color="black", justify="center")
        campo_cantidad.insert(0, dato["Cantidad"])  # Inicializar con el valor actual
        campo_cantidad.grid(row=fila, column=4, padx=10, pady=10, sticky="nsew")


        boton_eliminar = ctk.CTkButton(
            cuadro_productos,
            text="Eliminar",
            font=("Arial", 18, "bold"),
            fg_color="#f5b7b1",
            text_color="black",
            width=10,  # Ancho del botón
            height=30,
            command=lambda id=dato["No."]: print(f"Eliminar fila: {id}")
        )
        boton_eliminar.grid(row=fila, column=5, padx=10, pady=5, sticky="nsew")

        contenedor_final = ctk.CTkFrame(ventana, fg_color="#f4d03f", corner_radius=10)
        contenedor_final.grid(row=4, column=0, columnspan=3, padx=20, pady=(10, 20), sticky="nsew")
        contenedor_final.grid_columnconfigure((0, 1, 2,4, 5), weight=1)

    

    # Botón para completar venta
    boton_completar = ctk.CTkButton(
        contenedor_final,
        text="Completar venta",
        font=("Arial", 18, "bold"),
        fg_color="#28a745",  # Verde
        text_color="white",
        command=lambda: print("Venta completada")  # Acción del botón
    )
    boton_completar.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    # Botón para cancelar venta
    boton_cancelar = ctk.CTkButton(
        contenedor_final,
        text="Cancelar venta",
        font=("Arial", 18, "bold"),
        fg_color="#dc3545",  # Rojo
        text_color="white",
        command=lambda: print("Venta cancelada")  # Acción del botón
    )
    boton_cancelar.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    # Botón para ir (puedes personalizar el texto y acción)
    boton_ir = ctk.CTkButton(
        contenedor_final,
        text="Ir",
        font=("Arial", 18, "bold"),
        fg_color="#007bff",  # Azul
        text_color="white",
        command=lambda: print("Navegando...")  # Acción del botón
    )
    boton_ir.grid(row=1, column=2, padx=10, pady=10, sticky="ew")
    
    # Espacio para mostrar la suma total
    etiqueta_total = ctk.CTkLabel(
        contenedor_final,
        text="Total a pagar:",
        font=("Arial", 20, "bold"),
        text_color="black"
    )
    etiqueta_total.grid(row=1, column=3, padx=10, pady=10, sticky="w")

    etiqueta_suma = ctk.CTkLabel(
        contenedor_final,
        text="$146.00",  # Ejemplo del total
        font=("Arial", 20),
        text_color="black"
    )
    etiqueta_total.grid(row=1, column=4, padx=10, pady=10, sticky="w")



if __name__ == "__main__":
    ventana = ctk.CTk()
    ventana.geometry("1920x1080")
    encabezado(ventana)
    informacion_venta(ventana)
    tabla_encabezados(ventana)
    ventana.mainloop()