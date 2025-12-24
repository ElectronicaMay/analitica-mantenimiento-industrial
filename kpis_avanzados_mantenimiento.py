import pandas as pd

df = pd.read_csv("mantenimiento.csv")

df.columns = df.columns.str.strip()

df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m-%d")

df["costo_hora"] = df["costo_total"] / df["horas"]

mttr = df["horas"].mean()
mtbf = df["horas"].sum() / len(df)

costo_por_equipo = df.groupby("equipo")["costo_total"].sum().sort_values(ascending=False)

pareto = costo_por_equipo.reset_index()
pareto["acumulado_%"] = pareto["costo_total"].cumsum() / pareto["costo_total"].sum() * 100

writer = pd.ExcelWriter("kpis_avanzados.xlsx", engine="xlsxwriter")
df.to_excel(writer, sheet_name="Base_datos", index=False)
pareto.to_excel(writer, sheet_name="Pareto_costos", index=False)

resumen = pd.DataFrame({
    "KPI": ["MTTR (hrs)", "MTBF (hrs)", "Costo promedio por hora"],
    "Valor": [mttr, mtbf, df["costo_hora"].mean()]
})

resumen.to_excel(writer, sheet_name="KPIs_Avanzados", index=False)

writer.close()

print("Archivo generado: kpis_avanzados.xlsx")

