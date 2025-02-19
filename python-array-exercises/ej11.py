sueldosMañana = []
sueldosTarde = []

for i in range(4):
    sueldosMañana.append(float(input(f"Ingrese el sueldo del operario de la mañana {i+1}: ")))

for i in range(4):
    sueldosTarde.append(float(input(f"Ingrese el sueldo del operario de la tarde {i+1}: ")))

print("Lista de sueldos de la mañana:", sueldosMañana)
print("Lista de sueldos de la tarde:", sueldosTarde)