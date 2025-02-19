num = int(input("Ingrese la cantidad de piezas a procesar: "))
aptas = 0
i = 0
while i < num:
    longitud = int(input(f"Ingrese la longitud en cm de la pieza {i+1}: "))
    if 120 <= longitud <= 130:
        aptas += 1
    i += 1

print(f"La cantidad de piezas aptas es: {aptas}")
