lista = [123,31,33,444,22,3321,4,442]
contador = 0
for i in range(len(lista)):
    if lista[i]>100:
        contador+=1
print("Elementos superiores a 100: ")
print(contador)