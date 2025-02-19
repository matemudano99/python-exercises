sueldos = []
for i in range(5):
    sueldo = float(input("Ingrese el sueldo del operario {}: ".format(i+1)))
    sueldos.append(sueldo)

print("Lista de sueldos:", sueldos)

promedio = sum(sueldos) / len(sueldos)
print("El promedio de sueldos es:", promedio)