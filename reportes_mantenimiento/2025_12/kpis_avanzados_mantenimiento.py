import pandas as pd

# Leer CSV
df = pd.read_csv("mantenimiento.csv")

# Limpiar nombres de columnas (quita espacios ocultos)
df.columns = df.columns.str.strip()

# Convertir fecha
df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m-%d")

# =========================
# KPIs AVANZADOS
# =========================

# Costo por hora
df["costo_hora_real"] = df["costo_total"] / df["horas"]

# MTTR (promedio de horas por intervención)
mttr = df["horas"].mean()

# MTBF (días promedio entre mantenimientos)
df = df.sort_values("fecha")
mtbf = df["fecha"].diff().dt.days.mean()

# Pareto de costos por equipo
pareto_equipo = (
    df.groupby("equipo")["costo_total"]
    .sum()
    .sort_values(ascending=False)
)

print("MTTR (horas promedio):", round(mttr, 2))
print("MTBF (dias promedio):", round(mtbf, 2))
print("\nCosto por hora promedio:", round(df["costo_hora_real"].mean(), 2))
print("\nPareto de costos por equipo:")
print(pareto_equipo)
