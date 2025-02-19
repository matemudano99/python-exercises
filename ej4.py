print("PROMEDIO DE 10 NUMEROS")
total = 0
i = 1
while i <= 10:
    numero = int(input(f"Dime el numero {i}\n"))
    total = total + numero
    i = i + 1
print(f"El total es de: {total}")
print(f"El promedio es de: {total / 10}")