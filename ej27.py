cantidad_puntos = int(input("Ingrese la cantidad de puntos a procesar: "))
primer_cuadrante = 0
segundo_cuadrante = 0
tercer_cuadrante = 0
cuarto_cuadrante = 0

for i in range(cantidad_puntos):
    x = float(input("Ingrese las coordenadas (x): "))
    y = float(input("Ingrese las coordenadas (y): "))

    if x > 0 and y > 0:
        primer_cuadrante += 1
    elif x < 0 and y > 0:
        segundo_cuadrante += 1
    elif x < 0 and y < 0:
        tercer_cuadrante += 1
    elif x > 0 and y < 0:
        cuarto_cuadrante += 1

print(f"Puntos en el primer cuadrante: {primer_cuadrante}")
print(f"Puntos en el segundo cuadrante: {segundo_cuadrante}")
print(f"Puntos en el tercer cuadrante: {tercer_cuadrante}")
print(f"Puntos en el cuarto cuadrante: {cuarto_cuadrante}")