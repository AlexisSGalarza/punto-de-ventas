import app.Productos as productos

class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto, cantidad):
        """Agrega un producto al carrito."""
        for item in self.items:
            if item['id'] == producto['id']:
                item['cantidad'] += cantidad
                item['subtotal'] = item['cantidad'] * item['precio']
                return True
        self.items.append({
            'id': producto['id'],
            'nombre': producto['nombre'],
            'precio': producto['precio'],
            'cantidad': cantidad,
            'subtotal': producto['precio'] * cantidad
        })
        return True

    def eliminar_producto(self, id_producto):
        """Elimina un producto del carrito."""
        for i, item in enumerate(self.items):
            if item['id'] == id_producto:
                del self.items[i]
                return True
        return False

    def obtener_total(self):
        """Calcula el total del carrito."""
        return sum(item['subtotal'] for item in self.items)

    def vaciar(self):
        """Vacía el carrito."""
        self.items = [] 