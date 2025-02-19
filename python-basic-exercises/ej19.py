multiDe3=0
multiDe5=0
multiDe3y5=0
for x in range (1,11):
    num = int(input(f"Ingrese un el numero {x}: "))
    if(num%3==0 and num%5==0):
        multiDe3y5+=1
    elif(num%3==0):
        multiDe3+=1
    else:
        multiDe5+=1
print(f"Multiplos de 3: {multiDe3}")
print(f"Multiplos de 5: {multiDe5}")
print(f"Multiplos de 3 y 5: {multiDe3y5}")
