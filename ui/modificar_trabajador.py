import customtkinter as ctk

# Crear ventana principal
root = ctk.CTk()

# Cuadro blanco para los widgets
cuadro_blanco = ctk.CTkFrame(root, fg_color="#fcf3cf")  # Color de fondo
cuadro_blanco.grid(row=0, column=0, padx=20, pady=20)

# Titulo del formulario
titulo = ctk.CTkLabel(cuadro_blanco, text="Modificar Empleado", font=("Arial", 32, "bold"), text_color="black")
titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="n")

# Configurar las columnas del cuadro blanco para distribuir los widgets
cuadro_blanco.grid_columnconfigure(0, weight=1)
cuadro_blanco.grid_columnconfigure(1, weight=2)

# Campos del formulario
etiqueta_nombre = ctk.CTkLabel(cuadro_blanco, text="Nombre:", font=("Arial", 20), text_color="black")
etiqueta_nombre.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_nombre = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_nombre.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

etiqueta_apellido = ctk.CTkLabel(cuadro_blanco, text="Apellido:", font=("Arial", 20), text_color="black")
etiqueta_apellido.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_apellido = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_apellido.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

etiqueta_cargo = ctk.CTkLabel(cuadro_blanco, text="Cargo:", font=("Arial", 20), text_color="black")
etiqueta_cargo.grid(row=3, column=0, padx=10, pady=10, sticky="w")
entry_cargo = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_cargo.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

etiqueta_salario = ctk.CTkLabel(cuadro_blanco, text="Salario:", font=("Arial", 20), text_color="black")
etiqueta_salario.grid(row=4, column=0, padx=10, pady=10, sticky="w")
entry_salario = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_salario.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

etiqueta_fecha = ctk.CTkLabel(cuadro_blanco, text="Fecha de Contratación:", font=("Arial", 20), text_color="black")
etiqueta_fecha.grid(row=5, column=0, padx=10, pady=10, sticky="w")
entry_fecha = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_fecha.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

etiqueta_correo = ctk.CTkLabel(cuadro_blanco, text="Correo:", font=("Arial", 20), text_color="black")
etiqueta_correo.grid(row=6, column=0, padx=10, pady=10, sticky="w")
entry_correo = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_correo.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

etiqueta_telefono = ctk.CTkLabel(cuadro_blanco, text="Teléfono:", font=("Arial", 20), text_color="black")
etiqueta_telefono.grid(row=7, column=0, padx=10, pady=10, sticky="w")
entry_telefono = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_telefono.grid(row=7, column=1, padx=10, pady=10, sticky="ew")

etiqueta_rfc = ctk.CTkLabel(cuadro_blanco, text="RFC:", font=("Arial", 20), text_color="black")
etiqueta_rfc.grid(row=8, column=0, padx=10, pady=10, sticky="w")
entry_rfc = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_rfc.grid(row=8, column=1, padx=10, pady=10, sticky="ew")

etiqueta_curp = ctk.CTkLabel(cuadro_blanco, text="CURP:", font=("Arial", 20), text_color="black")
etiqueta_curp.grid(row=9, column=0, padx=10, pady=10, sticky="w")
entry_curp = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_curp.grid(row=9, column=1, padx=10, pady=10, sticky="ew")

etiqueta_direccion = ctk.CTkLabel(cuadro_blanco, text="Dirección:", font=("Arial", 20), text_color="black")
etiqueta_direccion.grid(row=10, column=0, padx=10, pady=10, sticky="w")
entry_direccion = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_direccion.grid(row=10, column=1, padx=10, pady=10, sticky="ew")

etiqueta_codigo_postal = ctk.CTkLabel(cuadro_blanco, text="Código Postal:", font=("Arial", 20), text_color="black")
etiqueta_codigo_postal.grid(row=11, column=0, padx=10, pady=10, sticky="w")
entry_codigo_postal = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_codigo_postal.grid(row=11, column=1, padx=10, pady=10, sticky="ew")

etiqueta_usuario = ctk.CTkLabel(cuadro_blanco, text="Usuario:", font=("Arial", 20), text_color="black")
etiqueta_usuario.grid(row=12, column=0, padx=10, pady=10, sticky="w")
entry_usuario = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black")
entry_usuario.grid(row=12, column=1, padx=10, pady=10, sticky="ew")

etiqueta_contrasena = ctk.CTkLabel(cuadro_blanco, text="Contraseña:", font=("Arial", 20), text_color="black")
etiqueta_contrasena.grid(row=13, column=0, padx=10, pady=10, sticky="w")
entry_contrasena = ctk.CTkEntry(cuadro_blanco, width=600, height=40, font=("Arial", 20), fg_color="white", text_color="black", show="*")
entry_contrasena.grid(row=13, column=1, padx=10, pady=10, sticky="ew")

# Función para cargar datos del trabajador (aquí colocas los datos del trabajador a modificar)
def cargar_trabajador(trabajador):
    entry_nombre.delete(0, ctk.END)
    entry_nombre.insert(0, trabajador['nombre'])
    entry_apellido.delete(0, ctk.END)
    entry_apellido.insert(0, trabajador['apellido'])
    entry_cargo.delete(0, ctk.END)
    entry_cargo.insert(0, trabajador['cargo'])
    entry_salario.delete(0, ctk.END)
    entry_salario.insert(0, trabajador['salario'])
    entry_fecha.delete(0, ctk.END)
    entry_fecha.insert(0, trabajador['fecha_contratacion'])
    entry_correo.delete(0, ctk.END)
    entry_correo.insert(0, trabajador['correo'])
    entry_telefono.delete(0, ctk.END)
    entry_telefono.insert(0, trabajador['telefono'])
    entry_rfc.delete(0, ctk.END)
    entry_rfc.insert(0, trabajador['rfc'])
    entry_curp.delete(0, ctk.END)
    entry_curp.insert(0, trabajador['curp'])
    entry_direccion.delete(0, ctk.END)
    entry_direccion.insert(0, trabajador['direccion'])
    entry_codigo_postal.delete(0, ctk.END)
    entry_codigo_postal.insert(0, trabajador['codigo_postal'])
    entry_usuario.delete(0, ctk.END)
    entry_usuario.insert(0, trabajador['usuario'])
    entry_contrasena.delete(0, ctk.END)
    entry_contrasena.insert(0, trabajador['contrasena'])

# Función para guardar los datos del trabajador modificado
def modificar_trabajador():
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
        "contrasena": entry_contrasena.get()
    }
    
    # Aquí iría la lógica para actualizar el trabajador (por ejemplo, base de datos)
    print(f"Datos del trabajador modificados: {trabajador_modificado}")

# Lista de trabajadores (solo ejemplo)
trabajadores = [
    {"id_trabajador": 1, "nombre": "Juan", "apellido": "Pérez", "cargo": "Gerente", "salario": 30000, "fecha_contratacion": "2020-01-01", "correo": "juan@example.com", "telefono": "555123456", "rfc": "JUPJ800101", "curp": "JUPJ800101HDFRRR01", "direccion": "Calle Ficticia 123", "codigo_postal": "12345", "usuario": "juanperez", "contrasena": "1234"},
]

# Crear botones para modificar
for trabajador in trabajadores:
    boton_modificar = ctk.CTkButton(root, text=f"Modificar {trabajador['nombre']} {trabajador['apellido']}",
                                    command=lambda trabajador=trabajador: cargar_trabajador(trabajador))
    boton_modificar.grid(row=trabajadores.index(trabajador) + 1, column=0, padx=10, pady=10)

# Botón de Guardar
boton_guardar = ctk.CTkButton(cuadro_blanco, text="Guardar", font=("Arial", 20), fg_color="green", text_color="white", command=modificar_trabajador)
boton_guardar.grid(row=14, column=0, columnspan=2, padx=10, pady=20, sticky="n")

# Iniciar la ventana principal
root.mainloop()
