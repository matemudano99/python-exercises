# Desarrollar un programa que solicite la carga de tres valores y muestre el menor.
# Desde el bloque principal del programa llamar 2 veces a dicha función
# (sin utilizar una estructura repetitiva)

def calcularMenor(a,b,c):
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    c = int(input("Tercer número: "))
    if a <= b and a <= c:
        menor = a
    elif b <= a and b <= c:
        menor = b
    else:
        menor = c
    return menor

a = int(input("Ingresa el valor 1/3\n"))
b = int(input("Ingresa el valor 2/3\n"))
c = int(input("Ingresa el valor 3/3\n"))

print (calcularMenor())