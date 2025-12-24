import pandas as pd

# Cargar datos
df = pd.read_csv("mantenimiento.csv")

# KPIs
costo_por_tecnico = df.groupby("tecnico")["costo_total"].sum()
horas_por_tecnico = df.groupby("tecnico")["horas"].sum()

kpis_generales = pd.DataFrame({
    "Indicador": [
        "Costo total del mes",
        "Costo promedio por orden",
        "Total horas trabajadas",
        "Tecnico con mas horas"
    ],
    "Valor": [
        df["costo_total"].sum(),
        df["costo_total"].mean(),
        df["horas"].sum(),
        horas_por_tecnico.idxmax()
    ]
})

# Exportar a Excel profesional
with pd.ExcelWriter("reporte_mantenimiento_empresa.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Datos", index=False)
    costo_por_tecnico.to_frame("costo_total").to_excel(writer, sheet_name="Costo_por_tecnico")
    horas_por_tecnico.to_frame("horas").to_excel(writer, sheet_name="Horas_por_tecnico")
    kpis_generales.to_excel(writer, sheet_name="KPIs", index=False)

print("Reporte empresarial generado: reporte_mantenimiento_empresa.xlsx")
