notas_mayores_igual_7 = 0
notas_menores_7 = 0

for i in range(10):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    if nota >= 7:
        notas_mayores_igual_7 += 1
    else:
        notas_menores_7 += 1

print(f"Cantidad de notas mayores o iguales a 7: {notas_mayores_igual_7}")
print(f"Cantidad de notas menores a 7: {notas_menores_7}")