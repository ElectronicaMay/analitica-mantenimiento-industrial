import pandas as pd

# 1. Leer archivo CSV
df = pd.read_csv("horas_trabajo.csv")

# 2. Limpiar filas vacías o inválidas
df = df.dropna()

# 3. Asegurar tipos numéricos
df["horas"] = df["horas"].astype(float)
df["costo_hora"] = df["costo_hora"].astype(float)

# 4. Calcular costo total
df["costo_total"] = df["horas"] * df["costo_hora"]

# 5. Mostrar resultados
print(df)

# 6. Resumen
print("\nCosto total general:")
print(df["costo_total"].sum())
