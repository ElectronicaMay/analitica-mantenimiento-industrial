import os
import shutil
from datetime import datetime

# Mes actual
mes = datetime.now().strftime("%Y_%m")

# Crear carpeta mensual
ruta_mes = f"reportes_mantenimiento/{mes}"
os.makedirs(ruta_mes, exist_ok=True)

# Archivos base
archivos = [
    "mantenimiento.csv",
    "kpis_mantenimiento.py",
    "kpis_avanzados_mantenimiento.py"
]

# Copiar archivos al mes
for archivo in archivos:
    if os.path.exists(archivo):
        shutil.copy(archivo, ruta_mes)

print(f"Entorno mensual creado en: {ruta_mes}")
