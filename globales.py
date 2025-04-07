from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent

# Rutas específicas para assets (imágenes, archivos estáticos)
ASSETS_DIR = BASE_DIR / 'assets'

# Ruta para la base de datos
DB_PATH = BASE_DIR / 'db' / 'mi_base_de_datos.db'

# Directorio para la UI (interfaz gráfica)
UI_DIR = BASE_DIR / 'ui'

# Rutas de los archivos principales y tickets
APP_DIR = BASE_DIR / 'app'