nombres = ["Juan", "Maria", "Carlos", "Ana", "Pedro"]
contador = 0
for nombre in nombres:
    if len(nombre) >= 5:
        contador += 1
print("Cantidad de nombres con 5 o más caracteres:", contador)