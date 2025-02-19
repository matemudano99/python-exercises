n = int(input("Ingrese la cantidad de triángulos: "))
triangulos_mayores = 0

for _ in range(n):
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    superficie = (base * altura) / 2
    print(f"Base: {base}, Altura: {altura}, Superficie: {superficie}")
    if superficie > 12:
        triangulos_mayores += 1

print(f"Cantidad de triángulos con superficie mayor a 12: {triangulos_mayores}")