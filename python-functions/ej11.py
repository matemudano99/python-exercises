# Cifrado César. Escribe una función que cifre un texto desplazando las letras un número dado de posiciones en el alfabeto.
while(True):
    texto = input("Dime el texto a cifrar: ")

    for i in range(len(texto)):
        caracter = chr( ord(texto[i])+3)
        print(caracter)