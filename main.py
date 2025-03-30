from ui.gestor_transiciones import GestorTransiciones
from ui.login import VentanaLogin
from ui.ventana_principal import VentanaPrincipal
from ui.dashboard_vista import DashboardVista


def main():
    app = GestorTransiciones()

    def cambiar_a_dashboard():
        ventana_dashboard = DashboardVista(app)
        app.cambiar_con_transicion(ventana_dashboard)

    def cambiar_a_principal():
        ventana_principal = VentanaPrincipal(app, cambiar_a_dashboard)
        app.cambiar_con_transicion(ventana_principal)

    ventana_login = VentanaLogin(app, cambiar_a_principal)
    app.mostrar_ventana(ventana_login)
    app.mainloop()


if __name__ == "__main__":
    main()
