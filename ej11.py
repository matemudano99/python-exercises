total1 = 0
total2 = 0
i = 0

while i < 15:
    valor1 = int(input(f"Ingrese el valor {i+1} para la lista 1: "))
    total1 += valor1
    i += 1

i = 0
while i < 15:
    valor2 = int(input(f"Ingrese el valor {i+1} para la lista 2: "))
    total2 += valor2
    i += 1

if total1 > total2:
    print("Lista 1 mayor")
elif total2 > total1:
    print("Lista 2 mayor")
else:
    print("Listas iguales")
