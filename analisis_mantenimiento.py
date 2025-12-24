import pandas as pd

df = pd.read_csv("mantenimiento.csv")

df["costo_mano_obra"] = df["horas"] * df["costo_hora"]
df["costo_total"] = df["costo_mano_obra"] + df["repuestos"]

print(df)