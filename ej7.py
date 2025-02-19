cantidadAlturas = int(input("Cuantas alturas quieres ingresar?"))
total = 0
i=1
while i<=cantidadAlturas:
    height = int(input(f"Que altura tiene la persona {i}: "))
    total += height
    i+=1
print(f"El promedio de altura es de {total/cantidadAlturas}")