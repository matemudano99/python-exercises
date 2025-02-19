n = int(input("Ingrese la cantidad de valores a ingresar: "))

contador = 0

for _ in range(n):
    numero = int(input("Ingrese un número entero: "))
    if numero >= 1000:
        contador += 1

print(f"La cantidad de valores mayores o iguales a 1000 es: {contador}")