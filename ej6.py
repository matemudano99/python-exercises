print("Notas")
i=1
mayores=0
menores=0
while i<=10:
    num = int(input(f"Dime el numero {i}:"))
    if(num>=7):
        mayores += 1
    else:
        menores += 1
    i=i+1
print(f"Hay {mayores} mayores a 7, y {menores} menores a 7")