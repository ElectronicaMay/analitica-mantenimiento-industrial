import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar datos
df = pd.read_csv("mantenimiento.csv")

# Verificación rápida (opcional, puedes borrarlo luego)
print(df.columns)

# 2. Cálculos base
# Columnas reales detectadas:
# tecnico, horas, costo_total, repuestos

# KPIs por técnico
costo_por_tecnico = df.groupby("tecnico")["costo_total"].sum()
horas_por_tecnico = df.groupby("tecnico")["horas"].sum()

# KPIs generales
costo_total_mes = df["costo_total"].sum()
costo_promedio_orden = df["costo_total"].mean()
total_horas = df["horas"].sum()
tecnico_mas_horas = horas_por_tecnico.idxmax()

# 3. Mostrar KPIs
print("\nCosto total por tecnico:")
print(costo_por_tecnico)

print("\nKPIs generales")
print(f"Costo total del mes: ${costo_total_mes}")
print(f"Costo promedio por orden: ${costo_promedio_orden:.2f}")
print(f"Total horas trabajadas: {total_horas}")
print(f"Tecnico con mas horas: {tecnico_mas_horas}")

# 4. Graficas
costo_por_tecnico.plot(kind="bar", title="Costo total por tecnico")
plt.ylabel("Costo")
plt.xlabel("Tecnico")
plt.tight_layout()
plt.show()

horas_por_tecnico.plot(kind="bar", title="Horas trabajadas por tecnico")
plt.ylabel("Horas")
plt.xlabel("Tecnico")
plt.tight_layout()
plt.show()

# 5. Exportar a Excel (nivel empresa)
with pd.ExcelWriter("reporte_mantenimiento.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Datos", index=False)
    costo_por_tecnico.to_frame("costo_total").to_excel(
        writer, sheet_name="Costo_por_tecnico"
    )
    horas_por_tecnico.to_frame("horas").to_excel(
        writer, sheet_name="Horas_por_tecnico"
    )

print("\nReporte generado: reporte_mantenimiento.xlsx")

# Validaciones de calidad de datos

errores = []

if (df["horas"] < 0).any():
    errores.append("Existen horas negativas")

if (df["costo_total"] < 0).any():
    errores.append("Existen costos negativos")

if df.isnull().any().any():
    errores.append("Existen valores nulos")

if errores:
    print("\nErrores de calidad de datos:")
    for e in errores:
        print("-", e)
else:
    print("\nDatos validados correctamente")
