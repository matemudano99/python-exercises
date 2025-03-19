
def sumar(lista):
    suma = 0
    for i in range(len(lista)):
        suma+=lista[i]
    return suma

def mayor(lista):
    may=lista[0]
    for i in range(len(lista)):
        if lista[i]>may:
            may = lista[i]
    return may

def menor(lista):
    men=lista[0]
    for i in range(len(lista)):
        if lista[i]< men:
            men = lista[i]
    return men

# main

listavalores=[10, 56, 23, 20, 94]
print("La lista completa es")
print(listavalores)
print("La suma de todos su elementos es", sumar(listavalores))
print("El mayor valor de la lista es", mayor(listavalores))
print("El menor valor de la lista es", menor(listavalores))