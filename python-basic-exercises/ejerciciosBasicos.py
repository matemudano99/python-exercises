# Ejercicio 1
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
suma = num1 + num2
producto = num1 * num2
print("El resultado de la suma es:")
print(suma)
print("El resultado de la multiplicacion es:")
print(producto)


# Ejercicio 2
lado = int(input("Digite el lado del cuadrado: "))
perimetro = lado * 4
print("El perimetro del cuadrado es igual a:", perimetro)


# Ejercicio 3
num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))
num4 = int(input("Digite el cuarto numero: "))

suma = num1 + num2
producto = num3 * num4

print("El resultado de sumar los dos primeros numeros es:", suma)
print("El resultado de multiplicar el tercer numero por el cuarto es:", producto)


# Ejercicio 4
num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))
num4 = int(input("Digite el cuarto numero: "))

suma = num1 + num2 + num3 + num4
promedio = suma / 4

print("La suma total de los numeros es:", suma)
print("El promedio calculado es:", promedio)


# Ejercicio 5
horas_trabajadas = int(input("Digite la cantidad de horas trabajadas: "))
valor_hora = float(input("Digite el valor por hora: "))

sueldo = horas_trabajadas * valor_hora
print("El monto del sueldo mensual es:", sueldo)


# Ejercicio 8
num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))

if num1 > num2:
    print("La suma de los numeros es:", num1 + num2)
    print("La diferencia entre ellos es:", num1 - num2)
else:
    print("El producto de los numeros es:", num1 * num2)
    print("El resultado de la division es:", num1 / num2)


# Ejercicio 9
nota1 = float(input("Digite la primera nota: "))
nota2 = float(input("Digite la segunda nota: "))
nota3 = float(input("Digite la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 7:
    print("Felicidades, has promocionado")


# Ejercicio 10
num = int(input("Digite un numero (1-99): "))

if num >= 10:
    print("Se trata de un numero de dos digitos")
else:
    print("Se trata de un numero de un digito")


# Ejercicio 12
num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))

mayor = max(num1, num2, num3)
print("El numero mayor es:", mayor)


# Ejercicio 13
num = int(input("Digite un numero: "))

if num > 0:
    print("El numero ingresado es positivo")
elif num < 0:
    print("El numero ingresado es negativo")
else:
    print("El numero ingresado es cero")


# Ejercicio 14
num = int(input("Digite un numero positivo de hasta tres cifras: "))

if num < 10:
    print("El numero tiene 1 cifra")
elif num < 100:
    print("El numero tiene 2 cifras")
elif num < 1000:
    print("El numero tiene 3 cifras")
else:
    print("Error: el numero tiene mas de tres cifras")


# Reto 1
nota = float(input("Digite la nota: "))

if 0 <= nota < 4.5:
    print("La calificacion obtenida es: Suspenso")
elif 4.5 <= nota < 5.5:
    print("La calificacion obtenida es: Aprobado")
elif 5.5 <= nota < 6.5:
    print("La calificacion obtenida es: Bien")
elif 6.5 <= nota < 8.5:
    print("La calificacion obtenida es: Notable")
elif 8.5 <= nota <= 10:
    print("La calificacion obtenida es: Sobresaliente")
else:
    print("Valor no valido")


# Ejercicio 17
dia = int(input("Digite el dia: "))
mes = int(input("Digite el mes: "))

if dia == 25 and mes == 12:
    print("La fecha ingresada es Navidad")
else:
    print("La fecha ingresada no es Navidad")


# Ejercicio 18
num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))

if num1 < 10 and num2 < 10 and num3 < 10:
    print("Todos los numeros son menores que diez")


# Ejercicio 19
if num1 < 10 or num2 < 10 or num3 < 10:
    print("Al menos uno de los numeros es menor que diez")


# Ejercicio 20
if num1 == num2 == num3:
    resultado = (num1 + num2) * num3
    print("El valor resultante es:", resultado)


# Ejercicio 21
x = int(input("Digite la coordenada X: "))
y = int(input("Digite la coordenada Y: "))

if x > 0 and y > 0:
    print("El punto se ubica en el primer cuadrante")
elif x < 0 and y > 0:
    print("El punto se ubica en el segundo cuadrante")
elif x < 0 and y < 0:
    print("El punto se ubica en el tercer cuadrante")
elif x > 0 and y < 0:
    print("El punto se ubica en el cuarto cuadrante")


# Ejercicio 22
sueldo = float(input("Digite el sueldo: "))
antiguedad = int(input("Digite los anos de antiguedad: "))

if sueldo < 500:
    if antiguedad >= 10:
        sueldo *= 1.2
    else:
        sueldo *= 1.05

print("El salario final es:", sueldo)


# Ejercicio 23
num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))

rango = max(num1, num2, num3) - min(num1, num2, num3)
print("El rango de variacion es:", rango)


# Reto 2
peso = float(input("Digite su peso en kg: "))
altura = float(input("Digite su altura en metros: "))

imc = peso / (altura ** 2)
print("Su indice de masa corporal es:", imc)
