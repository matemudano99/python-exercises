sumador = 0
for x in range (10):
    num= int(input("Ingrese un número: "))
    if(x>=5):
        sumador=sumador+num

print(f"La suma de los 5 ultimos numeros es: {sumador}")