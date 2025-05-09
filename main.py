import customtkinter as ctk
from tkinter import messagebox
from ui.login_ventana import VentanaLogin
from ui.ventana_principal import VentanaPrincipal
from ui.dashboard_vista import DashboardVista
from ui.ventana_productos import VentanaProductos
from ui.ventan_clientes import VentanaClientes
from ui.ventana_trabajadores import VentanaTrabajadores
from ui.ventana_reportes import VentanaReportes
from ui.graficos_vista import ventanagraficos
from globales import AppState

class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Abarrotes Gael")
        self.geometry("1920x1080")
        self.configure(fg_color="#fcf3cf")
        self.attributes("-fullscreen", True)

        self.app_state = AppState()
        
        # Contenedor principal para los frames
        self.container = ctk.CTkFrame(self, fg_color="#fcf3cf")
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.crear_frames()
        
        # Mostrar el frame de login inicialmente
        self.mostrar_frame("login")

    def crear_frames(self):
        # Crear instancias de todos los frames
        frames_config = [
            ("login", lambda: VentanaLogin(self.container, self.cambiar_a_dashboard, self.app_state)),
            ("dashboard", lambda: DashboardVista(self.container, 
                self.cambiar_a_clientes,
                self.cambiar_a_trabajadores,
                self.cambiar_a_login,
                self.app_state,
                self.cambiar_a_productos,
                self.cambiar_a_reportes,
                self.cambiar_a_graficos,
                self.cambiar_a_principal)),
            ("principal", lambda: VentanaPrincipal(self.container, self.cambiar_a_dashboard, self.app_state)),
            ("productos", lambda: VentanaProductos(self.container, self.cambiar_a_dashboard)),
            ("clientes", lambda: VentanaClientes(self.container, self.cambiar_a_dashboard)),
            ("trabajadores", lambda: VentanaTrabajadores(self.container, self.cambiar_a_dashboard)),
            ("reportes", lambda: VentanaReportes(self.container, self.cambiar_a_dashboard, self.cambiar_a_graficos)),
            ("graficos", lambda: ventanagraficos(self.container, self.cambiar_a_dashboard))
        ]
        
        # Crear e inicializar cada frame
        for name, frame_constructor in frames_config:
            frame = frame_constructor()
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def mostrar_frame(self, nombre_frame):
        """Trae el frame especificado al frente"""
        if nombre_frame not in self.frames:
            print(f"Error: Frame '{nombre_frame}' no encontrado")
            return
        frame = self.frames[nombre_frame]
        frame.tkraise()

    def cambiar_a_login(self):
        self.mostrar_frame("login")

    def cambiar_a_dashboard(self):
        print(f"Intentando cambiar a dashboard. Sesión iniciada: {self.app_state.sesion_iniciada}")
        print(f"Usuario actual: {self.app_state.usuario_actual}")
        print(f"Rol actual: {self.app_state.rol_actual}")
        
        if not self.app_state.sesion_iniciada:
            self.cambiar_a_login()
            return

        # Recrear el frame del dashboard para asegurar que se actualiza con el estado actual
        self.frames["dashboard"] = DashboardVista(self.container, 
            self.cambiar_a_clientes,
            self.cambiar_a_trabajadores,
            self.cambiar_a_login,
            self.app_state,
            self.cambiar_a_productos,
            self.cambiar_a_reportes,
            self.cambiar_a_graficos,
            self.cambiar_a_principal)
        self.frames["dashboard"].grid(row=0, column=0, sticky="nsew")
        
        self.mostrar_frame("dashboard")

    def cambiar_a_principal(self):
        if not self.app_state.sesion_iniciada:
            self.cambiar_a_login()
            return
        self.mostrar_frame("principal")

    def cambiar_a_productos(self):
        if not self.app_state.sesion_iniciada:
            self.cambiar_a_login()
            return
        self.mostrar_frame("productos")

    def cambiar_a_clientes(self):
        if not self.app_state.sesion_iniciada:
            self.cambiar_a_login()
            return
        self.mostrar_frame("clientes")

    def cambiar_a_trabajadores(self):
        if not self.app_state.sesion_iniciada:
            self.cambiar_a_login()
            return
        self.mostrar_frame("trabajadores")

    def cambiar_a_reportes(self):
        if not self.app_state.sesion_iniciada:
            self.cambiar_a_login()
            return
        self.mostrar_frame("reportes")

    def cambiar_a_graficos(self):
        if not self.app_state.sesion_iniciada:
            self.cambiar_a_login()
            return
        self.mostrar_frame("graficos")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()