import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("mantenimiento.csv")

df["costo_total"] = pd.to_numeric(df["costo_total"], errors="coerce")

pareto = (
    df.groupby("equipo")["costo_total"]
    .sum()
    .sort_values(ascending=False)
)

porcentaje_acumulado = pareto.cumsum() / pareto.sum() * 100

plt.figure()
pareto.plot(kind="bar")
plt.ylabel("Costo total")

plt.twinx()
porcentaje_acumulado.plot(marker="o")
plt.ylabel("% acumulado")

plt.title("Pareto costos por equipo")

plt.savefig("reportes_mantenimiento/2025_12/pareto_costos.png", bbox_inches="tight")
plt.close()

print("Pareto generado correctamente")
