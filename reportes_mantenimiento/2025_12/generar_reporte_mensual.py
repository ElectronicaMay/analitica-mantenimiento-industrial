import pandas as pd
from datetime import datetime
import os

# Configuración
mes = datetime.now().strftime("%Y_%m")
base_path = f"reportes_mantenimiento/{mes}"
os.makedirs(base_path, exist_ok=True)

# Leer datos
df = pd.read_csv("mantenimiento.csv")
df.columns = df.columns.str.strip()

# Exportar reporte
output = f"{base_path}/reporte_mantenimiento_{mes}.xlsx"

with pd.ExcelWriter(output) as writer:
    df.to_excel(writer, sheet_name="Datos", index=False)
    df.groupby("tecnico")["costo_total"].sum().to_excel(writer, sheet_name="Costo_por_tecnico")
    df.groupby("equipo")["costo_total"].sum().to_excel(writer, sheet_name="Costo_por_equipo")

print("Reporte mensual generado:", output)
