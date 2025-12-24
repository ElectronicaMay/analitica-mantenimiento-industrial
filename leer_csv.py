import csv

costo_total = 0

with open("horas_trabajo.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        costo_total += int(fila["horas"]) * float(fila["costo_hora"])

print(f"Costo total de mano de obra: ${costo_total}")

