class AppState:
    def __init__(self):
        self.id_actual = None
        self.usuario_actual = None
        self.rol_actual = None
        self.sesion_iniciada = False

    def iniciar_sesion(self, id,usuario, rol):

        self.id_actual = id
        self.usuario_actual = usuario
        self.rol_actual = rol
        self.sesion_iniciada = True
        print(f"Sesión iniciada: ID={self.id_actual}, Usuario={self.usuario_actual}, Rol={self.rol_actual}")

    def cerrar_sesion(self):
        self.id_actual = None
        self.usuario_actual = None
        self.rol_actual = None
        self.sesion_iniciada = False

    def get_current_user_id(self):
        if not self.sesion_iniciada:
                    print("Error: La sesión no está iniciada.")
                    return None
        return self.id_actual

    def get_current_user_name(self):
        if not self.sesion_iniciada:
            print("Error: La sesión no está iniciada.")
            return None
        return self.usuario_actual