def multiplicar(lista,num):
    for i in range(len(lista)):
        lista[i] = lista[i]*num
    return lista

# main

lista=[3,6,100,23,40]
resultado = multiplicar(lista,int(input("valor a multiplicar ")))
print(resultado)