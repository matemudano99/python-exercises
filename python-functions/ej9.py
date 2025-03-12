#Ordenar una lista. Pide al usuario una lista de números y ordénalos de menor a mayor.

item1 = int(input("Dime el primer numero: "))
item2 = int(input("Dime el segundo numero: "))
item3 = int(input("Dime el tercer numero: "))
item4 = int(input("Dime el cuarto numero: "))
item5 = int(input("Dime el quinto numero: "))

lista = [item1,item2,item3,item4,item5]
lista.sort()
print(lista)