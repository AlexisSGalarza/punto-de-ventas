from ui.gestor_transiciones import GestorTransiciones
from ui.login import VentanaLogin
from ui.ventana_principal import VentanaPrincipal
from ui.dashboard_vista import DashboardVista
from ui.ventana_trabajadores import VentanaTrabajadores

def main():
    app = GestorTransiciones()

    def cambiar_a_trabajadores():
       ventana_trabajadores = VentanaTrabajadores()
       app.cambiar_con_transicion(ventana_trabajadores)
       print("Navegando a trabajadores...")
       
    def cambiar_a_dashboard():
        ventana_dashboard = DashboardVista(app, cambiar_a_trabajadores)
        app.cambiar_con_transicion(ventana_dashboard)

    def cambiar_a_principal():
        ventana_principal = VentanaPrincipal(app, cambiar_a_dashboard)
        app.cambiar_con_transicion(ventana_principal)

    ventana_login = VentanaLogin(app, cambiar_a_principal)
    app.mostrar_ventana(ventana_login)
    app.mainloop()


if __name__ == "__main__":
    main()
