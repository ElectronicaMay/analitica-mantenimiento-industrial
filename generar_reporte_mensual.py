import os
import pandas as pd
from datetime import datetime

# Nombre del archivo origen
archivo_csv = "mantenimiento.csv"

# Cargar datos
df = pd.read_csv(archivo_csv)

# Crear carpeta por año_mes
anio_mes = datetime.now().strftime("%Y_%m")
carpeta = os.path.join("reportes_mantenimiento", anio_mes)
os.makedirs(carpeta, exist_ok=True)

# Nombre del archivo de salida
salida = os.path.join(carpeta, f"kpis_avanzados_{anio_mes}.xlsx")

# Exportar
with pd.ExcelWriter(salida, engine="xlsxwriter") as writer:
    df.to_excel(writer, index=False, sheet_name="Base_Datos")

print("Reporte generado:", salida)

