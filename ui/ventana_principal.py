import customtkinter as ctk
from PIL import Image, ImageDraw
from tkinter import Scrollbar
import ui.pagar as pa
import os
from datetime import datetime
import app.Productos as ve
import tkinter.messagebox as messagebox
import app.carrito as ca

class VentanaPrincipal(ctk.CTk):
    def __init__(self,abrir_dashboard, app_state,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.abrir_dashboard = abrir_dashboard
        self.app_state = app_state
        self.title("Abarrotes Gael")
        self.geometry("1920x1080")
        self.configure(fg_color="#fcf3cf")
        self.attributes("-fullscreen", True)
        self.carrito = []
        self.crear_ui() 

    def crear_ui(self):
            """Crea toda la interfaz visual de la ventana principal."""
            self.encabezado()
            self.informacion_venta()
            self.tabla_encabezados()

    def encabezado(self):
       """Crea el encabezado principal."""
       encabezado = ctk.CTkFrame(self, fg_color="#f4d03f", height=100)
       encabezado.grid(row=0, column=0, columnspan=3, sticky="ew", padx=10, pady=10)
       
       franja_roja = ctk.CTkFrame(encabezado, fg_color="#f11919", height=20)
       franja_roja.grid(row=1, column=0, columnspan=3, sticky="ew")

       self.grid_columnconfigure(0, weight=1)
       self.grid_columnconfigure(1, weight=1)
       self.grid_columnconfigure(2, weight=1)
       
       # Logo
       BASE_DIR = os.path.dirname(os.path.abspath(__file__))
       image_path = os.path.join(BASE_DIR, '..', 'assets', 'logo.jpg')

       if not os.path.exists(image_path):
            raise FileNotFoundError(f"El archivo no existe: {image_path}")
       else:
            print(f"Imagen encontrada en la ruta: {image_path}")
       logo_imagen = Image.open(image_path)
       logo_imagen_redondeada = self.redondear_bordes(logo_imagen, radio=75)
       # Guardar la referencia como atributo
       self.logo_imagen_ctk = ctk.CTkImage(logo_imagen_redondeada, size=(100, 100))

        # Usar la imagen en el CTkLabel
       logo = ctk.CTkLabel(encabezado, image=self.logo_imagen_ctk, text="")
       logo.grid(row=0, column=0, padx=10, pady=10, sticky="w")

       texto_encabezado = ctk.CTkLabel(
            encabezado,
            text="Tienda 'Abarrotes Gael'",
            font=("Arial", 50, "bold"),
            text_color="black"
        )
       texto_encabezado.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
       encabezado.grid_columnconfigure(1, weight=1)


    def informacion_venta(self):
        # Información de venta (nueva sección)
        info_venta = ctk.CTkFrame(self, fg_color="#fcf3cf")
        info_venta.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

        info_venta.grid_columnconfigure(0, weight=1)
        info_venta.grid_columnconfigure(1, weight=2)  # Mayor peso para el centro
        info_venta.grid_columnconfigure(2, weight=1)
        info_venta.grid_columnconfigure(1, weight=1)

        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        # Etiqueta de la fecha
        etiqueta_fecha = ctk.CTkLabel(
            info_venta,
            text=f"Fecha: {fecha_actual}",  # Texto inicial
            font=("Arial", 20),
            text_color="black"
        )
        etiqueta_fecha.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        etiqueta_hora = ctk.CTkLabel(
            info_venta,
            text="Hora: --:-- --",  # Texto inicial, será actualizado dinámicamente
            font=("Arial", 20),
            text_color="black"
        )
        etiqueta_hora.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        def actualizar_hora():
            """Actualiza la hora en la etiqueta dinámicamente."""
            hora_actual = datetime.now().strftime("%I:%M %p")
            etiqueta_hora.configure(text=f"Hora: {hora_actual}")  # Actualiza el texto de la etiqueta
            etiqueta_hora.after(1000, actualizar_hora)  # Vuelve a llamar a esta función después de 1 segundo (1000 ms)

        actualizar_hora()

        # Etiqueta para el número de venta
        etiqueta_numero_venta = ctk.CTkLabel(
            info_venta,
            text="No. de Venta: 0000000001",
            font=("Arial", 20, "bold"),
            text_color="black"
        )
        etiqueta_numero_venta.grid(row=0, column=3, rowspan=2, padx=10, pady=5, sticky="e")
        
        # Botón de búsqueda
        self.search_button = ctk.CTkButton(
            info_venta,
            text="Buscar",
            fg_color="#58d68d",
            text_color="white",
            command=self.abrir_modal_busqueda
        )
        self.search_button.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    def abrir_modal_busqueda(self):
        """Abre un modal para buscar y mostrar productos con paginación mejorada."""
        # Crear la ventana modal
        self.modal_busqueda = ctk.CTkToplevel(self)
        self.modal_busqueda.title("Buscar Productos")
        self.modal_busqueda.geometry("866x580")
        self.modal_busqueda.configure(fg_color="#fcf3cf")
        self.modal_busqueda.grab_set()

        # Encabezado del modal
        modal_encabezado = ctk.CTkFrame(self.modal_busqueda, fg_color="#f4d03f", corner_radius=10)
        modal_encabezado.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)
        modal_encabezado.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # Título y barra de búsqueda
        titulo_modal = ctk.CTkLabel(
            modal_encabezado,
            text="Buscar Productos",
            font=("Arial", 20, "bold"),
            text_color="black"
        )
        titulo_modal.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.modal_search_entry = ctk.CTkEntry(
            modal_encabezado,
            placeholder_text="🔍 Buscar por nombre o código de barras...",
            width=300,
            fg_color="white",
            text_color="black"
        )
        self.modal_search_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        self.modal_search_button = ctk.CTkButton(
            modal_encabezado,
            text="Buscar",
            fg_color="#58d68d",
            text_color="white",
            command=self.buscar_productos_en_modal
        )
        self.modal_search_button.grid(row=0, column=2, padx=10, pady=5, sticky="e")

        self.modal_close_button = ctk.CTkButton(
            modal_encabezado,
            text="Cerrar",
            fg_color="#f5b7b1",
            text_color="black",
            command=self.cerrar_modal
        )
        self.modal_close_button.grid(row=0, column=3, padx=10, pady=5, sticky="e")

        # Contenedor de resultados
        self.resultados_frame = ctk.CTkFrame(self.modal_busqueda, fg_color="white", corner_radius=10)
        self.resultados_frame.grid(row=1, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

        # Contenedor de paginación
        self.pagination_frame = ctk.CTkFrame(self.modal_busqueda, fg_color="#fcf3cf", corner_radius=10)
        self.pagination_frame.grid(row=2, column=0, columnspan=5, sticky="nsew", padx=10, pady=5)

        # Botones de paginación
        self.prev_button = ctk.CTkButton(
            self.pagination_frame,
            text="⬅ Anterior",
            command=self.previous_page,
            fg_color="white",
            text_color="black"
        )
        self.prev_button.grid(row=0, column=2, padx=5, sticky="e")

        self.next_button = ctk.CTkButton(
            self.pagination_frame,
            text="Siguiente ➡",
            command=self.next_page,
            fg_color="white",
            text_color="black"
        )
        self.next_button.grid(row=0, column=3, padx=5, sticky="e")

        # Número de página
        self.page_label = ctk.CTkLabel(
            self.pagination_frame,
            text="Página 1",
            font=("Arial", 16, "bold"),
            text_color="black"
        )
        self.page_label.grid(row=0, column=1, padx=5, sticky="w")

        # Inicializar variables de paginación
        self.current_page = 0
        self.items_per_page = 5
        self.productos_encontrados = []

        # Cargar productos iniciales
        self.cargar_productos_iniciales()

    def cargar_productos_iniciales(self):
        """Carga los productos iniciales en el modal."""
        try:
            # Obtener todos los productos
            productos = ve.obtener_productos()
            
            if not productos:
                ctk.CTkLabel(
                    self.resultados_frame,
                    text="No hay productos disponibles.",
                    font=("Arial", 16),
                    text_color="red"
                ).grid(row=0, column=0, columnspan=5, pady=10)
                return

            # Transformar los productos al formato necesario
            self.productos_encontrados = [
                {
                    "No.": producto[0],
                    "Producto": producto[1],
                    "CodigoBarras": producto[3],
                    "Stock": producto[7],
                    "Precio": producto[6]
                }
                for producto in productos
            ]

            # Mostrar la primera página
            self.mostrar_resultados_modal(self.productos_encontrados)
        except Exception as e:
            print(f"Error al cargar productos: {e}")
            messagebox.showerror("Error", f"No se pudieron cargar los productos: {str(e)}")

    def buscar_productos_en_modal(self):
        """Busca productos en el modal según el texto ingresado."""
        texto_busqueda = self.modal_search_entry.get().strip()

        try:
            if not texto_busqueda:
                # Si no hay texto de búsqueda, mostrar todos los productos
                productos = ve.obtener_productos()
            else:
                # Buscar productos por nombre o código de barras
                productos = ve.obtener_productos(texto_busqueda)

            if not productos:
                # Limpiar resultados anteriores
                for widget in self.resultados_frame.winfo_children():
                    widget.destroy()
                
                ctk.CTkLabel(
                    self.resultados_frame,
                    text="No se encontraron productos.",
                    font=("Arial", 16),
                    text_color="red"
                ).grid(row=0, column=0, columnspan=5, pady=10)
                return

            # Transformar los productos al formato necesario
            self.productos_encontrados = [
                {
                    "No.": producto[0],
                    "Producto": producto[1],
                    "CodigoBarras": producto[3],
                    "Stock": producto[7],
                    "Precio": producto[6]
                }
                for producto in productos
            ]

            # Mostrar la primera página
            self.current_page = 0
            self.mostrar_resultados_modal(self.productos_encontrados)
        except Exception as e:
            print(f"Error al buscar productos: {e}")
            messagebox.showerror("Error", f"No se pudieron buscar los productos: {str(e)}")

    def validar_y_agregar_al_carrito(self, producto, cantidad):
        try:
            cantidad = int(cantidad)  # Convertir la cantidad ingresada a entero

            # Validar si la cantidad es mayor que 0
            if cantidad <= 0:
                return False, "La cantidad debe ser mayor que 0."

            # Validar si la cantidad excede el stock
            if cantidad > producto["Stock"]:
                return False, f"La cantidad máxima permitida es {producto['Stock']}."

            # Crear el nuevo producto con el formato correcto
            nuevo_producto = {
                "No.": producto["No."],
                "Producto": producto["Producto"],
                "Código": producto["CodigoBarras"],
                "Precio": f"${float(producto['Precio']):.2f}",
                "Cantidad": cantidad,
                "Subtotal": f"${float(producto['Precio']) * cantidad:.2f}"
            }

            # Verificar si el producto ya está en el carrito
            for i, item in enumerate(self.carrito):
                if item["No."] == nuevo_producto["No."]:
                    # Actualizar cantidad y subtotal
                    self.carrito[i]["Cantidad"] += cantidad
                    self.carrito[i]["Subtotal"] = f"${float(producto['Precio']) * self.carrito[i]['Cantidad']:.2f}"
                    self.actualizar_total()  # Actualizar el total
                    return True, f"Actualizado: {nuevo_producto['Producto']} (Cantidad: {self.carrito[i]['Cantidad']})"

            # Si no está en el carrito, agregarlo
            self.carrito.append(nuevo_producto)
            self.actualizar_total()  # Actualizar el total
            return True, f"Agregado: {nuevo_producto['Producto']} (Cantidad: {cantidad})"
        
        except ValueError:
            return False, "La cantidad debe ser un número válido."
        except Exception as e:
            return False, f"Error al agregar al carrito: {str(e)}"

    def mostrar_resultados_modal(self, productos):
        """Muestra los productos dentro del modal con validación de cantidad."""
        for widget in self.resultados_frame.winfo_children():
            widget.destroy()  # Limpiar resultados previos

        # Obtener productos para la página actual
        start_index = self.current_page * self.items_per_page
        end_index = start_index + self.items_per_page
        productos_pagina = productos[start_index:end_index]

        if not productos_pagina:
            ctk.CTkLabel(
                self.resultados_frame,
                text="No hay productos en esta página.",
                font=("Arial", 18),
                text_color="red"
            ).grid(row=0, column=0, columnspan=5, pady=10, sticky="nsew")
            return

        # Actualizar número de página
        self.page_label.configure(text=f"Página {self.current_page + 1}")

        # Crear encabezados
        encabezados = ["Producto", "Código de Barras", "Stock", "Cantidad", "Acción"]
        for i, encabezado in enumerate(encabezados):
            ctk.CTkLabel(
                self.resultados_frame,
                text=encabezado,
                font=("Arial", 16, "bold"),
                text_color="black"
            ).grid(row=0, column=i, padx=10, pady=10, sticky="nsew")

        # Mostrar productos
        for fila, producto in enumerate(productos_pagina, start=1):
            ctk.CTkLabel(self.resultados_frame, text=producto["Producto"], font=("Arial", 16), text_color="black").grid(
                row=fila, column=0, padx=10, pady=5, sticky="nsew"
            )
            ctk.CTkLabel(self.resultados_frame, text=producto["CodigoBarras"], font=("Arial", 16), text_color="black").grid(
                row=fila, column=1, padx=10, pady=5, sticky="nsew"
            )
            ctk.CTkLabel(self.resultados_frame, text=producto["Stock"], font=("Arial", 16), text_color="black").grid(
                row=fila, column=2, padx=10, pady=5, sticky="nsew"
            )

            # Campo para cantidad
            campo_cantidad = ctk.CTkEntry(self.resultados_frame, font=("Arial", 16), justify="center", fg_color="white", text_color="black", border_color="black")
            campo_cantidad.insert(0, "1")
            campo_cantidad.grid(row=fila, column=3, padx=10, pady=5, sticky="nsew")

            # Botón "Agregar" con validación activa
            def validar_y_mostrar(producto, cantidad_entry):
                cantidad = cantidad_entry.get().strip()
                es_valido, mensaje = self.validar_y_agregar_al_carrito(producto, cantidad)
                
                # Mostrar mensaje de resultado
                mensaje_label = ctk.CTkLabel(
                    self.resultados_frame,
                    text=mensaje,
                    font=("Arial", 14),
                    text_color="green" if es_valido else "red"
                )
                mensaje_label.grid(row=fila + 1, column=0, columnspan=5, pady=5, sticky="nsew")
                
                # Eliminar el mensaje después de 2 segundos
                self.after(2000, lambda: mensaje_label.destroy())
                
                # Actualizar la tabla del carrito si la operación fue exitosa
                if es_valido:
                    self.tabla_encabezados()

            boton_agregar = ctk.CTkButton(
                self.resultados_frame,
                text="Agregar",
                fg_color="#58d68d",
                text_color="white",
                command=lambda p=producto, c=campo_cantidad: validar_y_mostrar(p, c)
            )
            boton_agregar.grid(row=fila, column=4, padx=10, pady=5, sticky="nsew")

    def next_page(self):
        """Muestra la siguiente página de productos."""
        if (self.current_page + 1) * self.items_per_page < len(self.productos_encontrados):
            self.current_page += 1
            self.mostrar_resultados_modal(self.productos_encontrados)

    def previous_page(self):
        """Muestra la página anterior de productos."""
        if self.current_page > 0:
            self.current_page -= 1
            self.mostrar_resultados_modal(self.productos_encontrados)
    def cerrar_modal(self):
        """Cierra el modal de búsqueda."""
        self.modal_busqueda.destroy()

    def tabla_encabezados(self):
        """Crea la tabla que actúa como carrito de compras."""
        # Inicializar el carrito como una lista vacía
        if not hasattr(self, 'carrito'):
            self.carrito = []  # Lista para gestionar los productos del carrito

        # Encabezados de la tabla
        cuadro_campos = ctk.CTkFrame(self, fg_color="#f4d03f", corner_radius=10)
        cuadro_campos.grid(row=2, column=0, columnspan=3, padx=20, pady=(10), sticky="nsew")

        cuadro_campos.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        etiquetas = ["No.", "Producto", "Código", "Precio", "Cantidad", "Subtotal", "Acción"]
        for i, texto in enumerate(etiquetas):
            etiqueta = ctk.CTkLabel(
                cuadro_campos,
                text=texto,
                font=("Arial", 20, "bold"),
                text_color="black"
            )
            etiqueta.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")
        
        # Contenedor con scroll para los productos
        contenedor_scroll = ctk.CTkFrame(self)
        contenedor_scroll.grid(row=3, column=0, columnspan=3, padx=20, pady=(10), sticky="nsew")
        contenedor_scroll.grid_columnconfigure(0, weight=1)
        contenedor_scroll.grid_rowconfigure(0, weight=1)

        # Canvas para habilitar el scroll
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
        cuadro_productos.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        # Mostrar productos en el carrito
        def actualizar_tabla_carrito():
            """Actualiza las filas de la tabla según los productos en el carrito."""
            for widget in cuadro_productos.winfo_children():
                widget.destroy()  # Limpiar filas previas
            
            # Añadir filas dinámicas desde el carrito
            for fila, producto in enumerate(self.carrito, start=1):
                etiqueta_no = ctk.CTkLabel(cuadro_productos, text=producto["No."], font=("Arial", 18), text_color="black")
                etiqueta_no.grid(row=fila, column=0, padx=10, pady=5, sticky="nsew")

                etiqueta_producto = ctk.CTkLabel(cuadro_productos, text=producto["Producto"], font=("Arial", 18), text_color="black")
                etiqueta_producto.grid(row=fila, column=1, padx=10, pady=5, sticky="nsew")

                etiqueta_codigo = ctk.CTkLabel(cuadro_productos, text=producto["Código"], font=("Arial", 18), text_color="black")
                etiqueta_codigo.grid(row=fila, column=2, padx=10, pady=5, sticky="nsew")

                etiqueta_precio = ctk.CTkLabel(cuadro_productos, text=producto["Precio"], font=("Arial", 18), text_color="black")
                etiqueta_precio.grid(row=fila, column=3, padx=10, pady=5, sticky="nsew")

                etiqueta_cantidad = ctk.CTkLabel(cuadro_productos, text=producto["Cantidad"], font=("Arial", 18), text_color="black")
                etiqueta_cantidad.grid(row=fila, column=4, padx=10, pady=5, sticky="nsew")

                etiqueta_subtotal = ctk.CTkLabel(cuadro_productos, text=producto["Subtotal"], font=("Arial", 18), text_color="black")
                etiqueta_subtotal.grid(row=fila, column=5, padx=10, pady=5, sticky="nsew")

                # Botón "Eliminar" para quitar productos del carrito
                boton_eliminar = ctk.CTkButton(
                    cuadro_productos,
                    text="Eliminar",
                    font=("Arial", 18, "bold"),
                    fg_color="#f5b7b1",
                    text_color="black",
                    command=lambda id=fila-1: eliminar_del_carrito(id)
                )
                boton_eliminar.grid(row=fila, column=6, padx=10, pady=5, sticky="nsew")

        def eliminar_del_carrito(indice):
            """Elimina un producto del carrito según su índice."""
            if 0 <= indice < len(self.carrito):
                eliminado = self.carrito.pop(indice)
                print(f"Producto eliminado: {eliminado}")
                actualizar_tabla_carrito()
                self.actualizar_total()

        # Inicializar la tabla con los productos actuales en el carrito
        actualizar_tabla_carrito()

        # Pie final
        contenedor_final = ctk.CTkFrame(self, fg_color="#f4d03f", corner_radius=10, height=100)
        contenedor_final.grid(row=4, column=0, columnspan=3, padx=20, pady=(10, 20), sticky="nsew")
        contenedor_final.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        # Botón para completar venta
        boton_completar = ctk.CTkButton(
            contenedor_final,
            text="Completar venta",
            font=("Arial", 18, "bold"),
            fg_color="#28a745",  # Verde
            text_color="white",
            command=self.completar_venta
        )
        boton_completar.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Botón para cancelar venta
        boton_cancelar = ctk.CTkButton(
            contenedor_final,
            text="Cancelar venta",
            font=("Arial", 18, "bold"),
            fg_color="#dc3545",  # Rojo
            text_color="white",
            command=self.cancelar_venta
        )
        boton_cancelar.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        # Botón para ir al dashboard
        boton_dashboard = ctk.CTkButton(
            contenedor_final,
            text="Ir al Dashboard",
            font=("Arial", 18, "bold"),
            fg_color="#3498db",  # Azul
            text_color="white",
            command=self.abrir_dashboard
        )
        boton_dashboard.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        # Espacio para mostrar la suma total
        etiqueta_total = ctk.CTkLabel(
            contenedor_final,
            text="Total a pagar:",
            font=("Arial", 20, "bold"),
            text_color="black"
        )
        etiqueta_total.grid(row=1, column=3, padx=10, sticky="w")

        # Etiqueta para mostrar el total calculado
        self.etiqueta_suma = ctk.CTkLabel(
            contenedor_final,
            text="$0.00",  # Inicialmente en 0
            font=("Arial", 20),
            text_color="black"
        )
        self.etiqueta_suma.grid(row=1, column=4, sticky="w")
        # Calcular y mostrar el total inicial
        self.actualizar_total()

    def actualizar_total(self):
        """Calcula y actualiza el total de la venta."""
        total = 0.0
        for producto in self.carrito:
            # Extraer el valor numérico del precio (eliminando el símbolo $)
            precio = float(producto["Precio"].replace("$", ""))
            total += precio * producto["Cantidad"]
        
        self.etiqueta_suma.configure(text=f"${total:.2f}")

    def completar_venta(self):
        """Procesa la venta y muestra el modal de pago."""
        if not self.carrito:
            messagebox.showwarning("Carrito vacío", "No hay productos en el carrito.")
            return

        try:
            total = float(self.etiqueta_suma.cget("text").replace("$", ""))

            # Validar ID del trabajador
            id_trabajador = self.app_state.get_current_user_id()  # Cambiado a get_current_user_id
            if not id_trabajador:
                messagebox.showerror("Error", "No se ha iniciado sesión correctamente.")
                return

            # Preguntar si se desea generar factura
            generar_factura = messagebox.askyesno("Generar factura", "¿Deseas generar una factura?")
            id_cliente = None

            if generar_factura:
                # Abrir modal para seleccionar o crear cliente
                id_cliente = self.seleccionar_o_crear_cliente()
                if not id_cliente:
                    messagebox.showerror("Error", "Debes seleccionar o crear un cliente para generar la factura.")
                    return

            # Mostrar modal de pago
            pa.mostrar_modal_pago(total, id_trabajador)

            # Generar ticket o factura
            if generar_factura:
                print(f"Generando factura para el cliente con ID {id_cliente}...")
                # Aquí puedes agregar la lógica para generar la factura
            else:
                print("Generando solo el ticket...")
                # Aquí puedes agregar la lógica para generar solo el ticket

            # Limpiar el carrito después de completar la venta
            self.carrito.clear()
            self.tabla_encabezados()  # Refrescar la tabla
        except Exception as e:
            print(f"Error al completar la venta: {e}")
            messagebox.showerror("Error", f"Error al completar la venta: {str(e)}")


    def cancelar_venta(self):
        """Cancela la venta actual y vacía el carrito."""
        if messagebox.askyesno("Cancelar venta", "¿Está seguro de que desea cancelar la venta?"):
            self.carrito.clear()
            self.tabla_encabezados()  # Refrescar la tabla

    def redondear_bordes(self, imagen, radio):
        """Redondea los bordes de una imagen."""
        mascara = Image.new("L", imagen.size, 0)
        draw = ImageDraw.Draw(mascara)
        draw.rounded_rectangle(
            (0, 0, imagen.size[0], imagen.size[1]),
            radius=radio, fill=255
        )
        imagen_redondeada = imagen.convert("RGBA")
        imagen_redondeada.putalpha(mascara)
        return imagen_redondeada

    def obtener_y_mostrar_productos(self):
        """Obtiene productos de la base de datos y los muestra en el modal."""
        try:
            productos_encontrados = ve.obtener_productos()  # Obtener productos de la base de datos
            print(f"Productos encontrados: {productos_encontrados}")  # Debug

            if not productos_encontrados:
                print("No se encontraron productos en la base de datos")
                return

            # Transformar los productos en un diccionario con las claves correctas
            productos_transformados = [
                {
                    "No.": producto[0],  # ID_pr
                    "Producto": producto[1],  # Nombre_pr
                    "CodigoBarras": producto[3],  # codigo_barras_pr
                    "Stock": producto[7],  # Stock_pr
                    "Precio": producto[6]  # Precio_pr
                }
                for producto in productos_encontrados
            ]

            print(f"Productos transformados: {productos_transformados}")  # Debug
            self.mostrar_resultados_modal(productos_transformados)
        except Exception as e:
            print(f"Error al obtener y mostrar productos: {e}")  # Debug
            messagebox.showerror("Error", f"No se pudieron cargar los productos: {str(e)}")

    def abrir_dashboard(self):
        """Abre la ventana del dashboard."""
        try:
            # Ocultar la ventana principal
            self.withdraw()
            # Llamar a la función de callback para abrir el dashboard
            if hasattr(self, 'abrir_dashboard'):
                self.abrir_dashboard()
            else:
                raise Exception("No se encontró la función para abrir el dashboard")
        except Exception as e:
            print(f"Error al abrir el dashboard: {e}")
            messagebox.showerror("Error", f"No se pudo abrir el dashboard: {str(e)}")
            # Si hay error, volver a mostrar la ventana principal
            self.deiconify()



if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()