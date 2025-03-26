import os
import importlib
import ui
# Importar todos los módulos dentro de la carpeta ui de manera dinámica
modulos = [
    f[:-3] for f in os.listdir(os.path.dirname(__file__)) 
    if f.endswith('.py') and f != '__init__.py'
]

for modulo in modulos:
    globals()[modulo] = importlib.import_module(f".{modulo}", "ui")