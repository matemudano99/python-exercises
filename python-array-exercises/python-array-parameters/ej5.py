def multiplicacion(lista):
    producto=1
    for i in range(len(lista)):
        producto=producto*lista[i]
    return producto

# main

lista=[1,2,3,4,5]
print("Lista: ",lista)
print("multiplicacion: ", multiplicacion(lista))