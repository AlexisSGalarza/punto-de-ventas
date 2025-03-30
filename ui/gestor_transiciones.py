import customtkinter as ctk

class GestorTransiciones(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")  # Tamaño de la ventana principal
        self.title("Sistema Abarrotes Gael")
        self.configure(fg_color="#fcf3cf")  # Fondo claro como en tus ventanas
        self.attributes('-fullscreen', True)  # Modo pantalla completa
        self.ventana_actual = None  # Referencia a la ventana actualmente visible

    def mostrar_ventana(self, ventana):
        """Muestra una nueva ventana."""
        if self.ventana_actual:
            self.ventana_actual.pack_forget()  # Oculta la ventana anterior
        self.ventana_actual = ventana
        self.ventana_actual.pack(fill="both", expand=True)

    def cambiar_con_transicion(self, nueva_ventana):
        """Realiza una transición suave entre ventanas."""
        self.fade_out(lambda: [self.mostrar_ventana(nueva_ventana), self.fade_in()])

    def fade_out(self, on_complete):
        """Efecto de desvanecimiento."""
        alpha = self.attributes('-alpha')
        if alpha > 0.1:
            self.attributes('-alpha', alpha - 0.1)  # Reducir opacidad gradualmente
            self.after(50, self.fade_out, on_complete)
        else:
            on_complete()  # Mostrar la nueva ventana
            self.attributes('-alpha', 1)  # Restaurar opacidad

    def fade_in(self):
        """Efecto de aumento de opacidad."""
        alpha = self.attributes('-alpha')
        if alpha < 1:
            self.attributes('-alpha', alpha + 0.1)  # Incrementar opacidad gradualmente
            self.after(50, self.fade_in)  # Continuar hasta alcanzar opacidad completa

