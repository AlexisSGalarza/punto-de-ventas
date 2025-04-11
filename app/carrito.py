import db.conexion as co
import app.Productos as productos

class CarritoCompras:
    def __init__(self):
        self.items = {}  # Diccionario para almacenar {id_producto: cantidad}
        self.total = 0.0

    def agregar_producto(self, id_producto, cantidad=1):
        """Agrega un producto al carrito."""
        producto = productos.obtener_producto_por_id(id_producto)
        if not producto:
            raise ValueError(f"Producto con ID {id_producto} no encontrado.")
        
        if int(producto['Stock_pr']) < cantidad:
            raise ValueError(f"Stock insuficiente. Solo hay {producto['Stock_pr']} unidades disponibles.")
        
        if id_producto in self.items:
            self.items[id_producto] += cantidad
        else:
            self.items[id_producto] = cantidad
        
        self.total += float(producto['Precio_pr']) * cantidad

    def remover_producto(self, id_producto, cantidad=1):
        """Remueve una cantidad específica de un producto del carrito."""
        if id_producto not in self.items:
            raise ValueError("Producto no está en el carrito.")
        
        producto = productos.obtener_producto_por_id(id_producto)
        if not producto:
            raise ValueError(f"Producto con ID {id_producto} no encontrado.")
        
        if cantidad >= self.items[id_producto]:
            # Remover el producto completamente
            self.total -= float(producto['Precio_pr']) * self.items[id_producto]
            del self.items[id_producto]
        else:
            # Reducir la cantidad
            self.items[id_producto] -= cantidad
            self.total -= float(producto['Precio_pr']) * cantidad

    def obtener_total(self):
        """Retorna el total actual del carrito."""
        return self.total

    def obtener_items(self):
        """Retorna los items en el carrito con sus detalles."""
        items_detallados = []
        for id_producto, cantidad in self.items.items():
            producto = productos.obtener_producto_por_id(id_producto)
            if producto:
                items_detallados.append({
                    'id': id_producto,
                    'nombre': producto['Nombre_pr'],
                    'precio_unitario': producto['Precio_pr'],
                    'cantidad': cantidad,
                    'subtotal': float(producto['Precio_pr']) * cantidad
                })
        return items_detallados

    def vaciar_carrito(self):
        """Vacía el carrito de compras."""
        self.items.clear()
        self.total = 0.0

    def finalizar_compra(self, id_cliente, id_trabajador):
        """Finaliza la compra y actualiza el inventario."""
        if not self.items:
            raise ValueError("El carrito está vacío.")
        
        conn = co.obtener_conexion()
        if not conn:
            raise ConnectionError("No se pudo conectar a la base de datos.")
        
        try:
            cursor = conn.cursor()
            
            # Crear el ticket
            query_ticket = """
            INSERT INTO ticket (ID_cl_ti, ID_tr_ti, Total_ti, Estado_ti)
            VALUES (%s, %s, %s, 'Completado')
            """
            cursor.execute(query_ticket, (id_cliente, id_trabajador, self.total))
            id_ticket = cursor.lastrowid
            
            # Insertar detalles de venta y actualizar inventario
            for id_producto, cantidad in self.items.items():
                # Insertar detalle de venta
                query_detalle = """
                INSERT INTO detalles_venta (ID_ti_dv, ID_pr_dv, Cantidad_dv)
                VALUES (%s, %s, %s)
                """
                cursor.execute(query_detalle, (id_ticket, id_producto, cantidad))
                
                # Actualizar stock
                query_stock = """
                UPDATE productos
                SET Stock_pr = Stock_pr - %s
                WHERE ID_pr = %s
                """
                cursor.execute(query_stock, (cantidad, id_producto))
            
            conn.commit()
            self.vaciar_carrito()
            return id_ticket
            
        except Exception as e:
            conn.rollback()
            raise Exception(f"Error al finalizar la compra: {str(e)}")
        finally:
            cursor.close()
            conn.close() 