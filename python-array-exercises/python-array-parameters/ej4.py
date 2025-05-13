def compararCaracteres(palabras):
    palabraMasLarga = palabras[0]
    for i in range(len(palabras)):
        if(len(palabraMasLarga)<len(palabras[i])):
            palabraMasLarga = palabras[i]
    return palabraMasLarga

# main 

palabras = ["enero", "febrero", "marzo", "abril", "mayo", "junio","septiembre"]
print(compararCaracteres(palabras))