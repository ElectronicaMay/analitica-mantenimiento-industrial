import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("mantenimiento.csv")

# Asegurar cálculo base
df["costo_mano_obra"] = df["horas"] * df["costo_hora"]
df["costo_total"] = df["costo_mano_obra"] + df["repuestos"]

# =========================
# 📊 1. Costo total por técnico
# =========================
costo_tecnico = df.groupby("tecnico")["costo_total"].sum()

plt.figure()
costo_tecnico.plot(kind="bar")
plt.title("Costo total por técnico")
plt.xlabel("Técnico")
plt.ylabel("Costo total")
plt.tight_layout()
plt.show()

# =========================
# 📊 2. Distribución de costos
# =========================
plt.figure()
df[["costo_mano_obra", "repuestos"]].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Distribución de costos de mantenimiento")
plt.ylabel("")
plt.tight_layout()
plt.show()

# =========================
# 📊 3. Horas trabajadas por técnico
# =========================
horas_tecnico = df.groupby("tecnico")["horas"].sum()

plt.figure()
horas_tecnico.plot(kind="bar")
plt.title("Horas trabajadas por técnico")
plt.xlabel("Técnico")
plt.ylabel("Horas")
plt.tight_layout()
plt.show()
