class AppState:
    def __init__(self):
        self.usuario_actual = None
        self.rol_actual = None
        self.sesion_iniciada = False

    def iniciar_sesion(self, usuario, rol):
        self.usuario_actual = usuario
        self.rol_actual = rol
        self.sesion_iniciada = True

    def cerrar_sesion(self):
        self.usuario_actual = None
        self.rol_actual = None
        self.sesion_iniciada = False
