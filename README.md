# Sistema Punto de Ventas

Sistema de punto de ventas desarrollado en Python con interfaz gráfica, gestión de productos, clientes, trabajadores y generación de reportes.

## Características

- 🔐 Sistema de login para trabajadores
- 📦 Gestión de productos (agregar, modificar, eliminar)
- 👥 Gestión de clientes (agregar, modificar, eliminar)
- 👤 Gestión de trabajadores (agregar, modificar, eliminar)
- 🛒 Carrito de compras
- 📊 Visualización de gráficos y estadísticas
- 📝 Generación de tickets de venta en PDF
- 📈 Sistema de reportes

## Requisitos del Sistema

- Python 3.13+
- Base de datos (configurada en db/conexion.py)
- Dependencias listadas en requirements.txt

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/[tu-usuario]/punto-de-ventas.git
cd punto-de-ventas
```

2. Crear y activar entorno virtual:
```bash
python -m venv mi_entorno
# En Windows:
mi_entorno\Scripts\activate
# En Linux/Mac:
source mi_entorno/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

- `app/`: Módulos principales de la aplicación
- `assets/`: Recursos gráficos
- `db/`: Configuración de la base de datos
- `ui/`: Interfaces gráficas
- `reportes/`: Archivos de reportes generados
- `tickets/`: Tickets de venta generados en PDF

## Ejecución

Para iniciar la aplicación:
```bash
python main.py
```

## Funcionalidades

### Gestión de Productos
- Agregar nuevos productos
- Modificar productos existentes
- Eliminar productos
- Visualización de inventario

### Gestión de Clientes
- Registro de nuevos clientes
- Modificación de datos
- Historial de compras

### Gestión de Ventas
- Carrito de compras
- Generación de tickets
- Registro de transacciones

### Reportes y Gráficos
- Visualización de estadísticas
- Generación de reportes de ventas
- Gráficos de rendimiento

## Contribución

Si deseas contribuir al proyecto:
1. Haz un Fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Haz commit de tus cambios (`git commit -am 'Agrega nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crea un Pull Request

