import customtkinter as ctk
from ui.login_ventana import VentanaLogin
from ui.ventana_principal import VentanaPrincipal
from ui.dashboard_vista import DashboardVista
from ui.ventana_trabajadores import VentanaTrabajadores
from ui.ventan_clientes import VentanaClientes
from ui.ventana_productos import productosventana
from globales import AppState

def main():
    ventana_actual = None  # Variable para rastrear la ventana activa
    app_state = AppState()

    def abrir_dashboard():
        nonlocal ventana_actual
        if ventana_actual:  # Cierra la ventana actual si existe
            ventana_actual.destroy()             
        ventana_dashboard = DashboardVista(abrir_clientes, abrir_trabajadores, abrir_login,app_state,abir_productos)  # Agrega abrir_login
        ventana_actual = ventana_dashboard  # Actualiza la ventana actual
        ventana_dashboard.mainloop()
    
    def abir_productos():
        nonlocal ventana_actual
        if ventana_actual:
            ventana_actual.destroy()
        ventana_productos = productosventana(abrir_dashboard)
        ventana_actual = ventana_productos
        ventana_productos.mainloop()

    def abrir_clientes():
        nonlocal ventana_actual
        if ventana_actual:
            ventana_actual.destroy()
        ventana_clientes = VentanaClientes(abrir_dashboard)
        ventana_actual = ventana_clientes
        ventana_clientes.mainloop()

    def abrir_trabajadores():
        nonlocal ventana_actual
        if ventana_actual:
            ventana_actual.destroy()
        ventana_trabajadores = VentanaTrabajadores(abrir_dashboard)  # Pasar la función abrir_dashboard
        ventana_actual = ventana_trabajadores
        ventana_trabajadores.mainloop()


    def abrir_principal():
        nonlocal ventana_actual
        if ventana_actual:
            ventana_actual.destroy()
        ventana_principal = VentanaPrincipal(abrir_dashboard)
        ventana_actual = ventana_principal
        ventana_principal.mainloop()

    def abrir_login():
        nonlocal ventana_actual
        if ventana_actual:
            ventana_actual.destroy()
        ventana_login = VentanaLogin(abrir_principal,app_state)
        ventana_actual = ventana_login
        ventana_login.mainloop()

    abrir_login()

if __name__ == "__main__":
    main()  