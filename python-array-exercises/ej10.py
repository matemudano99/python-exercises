alturas = []
contador = 0
suma = 0
for i in range(5):
    alturas.append(float(input(f"Ingrese la altura de la persona {i}:")))
    suma += alturas[i]
promedio = suma / 5
for altura in alturas:
    if altura > promedio:
        contador += 1
print("Lista de alturas:", alturas)
print("Número de personas con altura superior al promedio:", contador)
