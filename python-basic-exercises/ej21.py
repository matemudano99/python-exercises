
cantidad = int(input("Cuantos valores va a ingresar? "))

negativos = 0

for _ in range(cantidad):
    valor = float(input("Ingrese un valor: "))
    if valor < 0:
        negativos += 1

print(f"Se ingresaron {negativos} números negativos.")