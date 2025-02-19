nNumeros = int(input("Cuantos numeros quieres evaluar? "))
i=1
contadorPar=0
contadorImpar=0
while i<=nNumeros:
    if(i%2==0):
        contadorPar+=1
    else:
        contadorImpar+=1
    i+=1
print(f"Hay {contadorPar} numeros pares, y {contadorImpar} numeros impares")