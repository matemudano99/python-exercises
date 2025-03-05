# Crear una calculadora utilizando return en las funciones

def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b != 0:
        return a/b
    else: return "can't divide by 0"

# main
opt=0
while opt!=5:
    opt=int(input("1: addition  2: substraction  3: multiplication  4: division  5: quit\n"))

    total=0
    if opt==1:
        a=int(input("First number: "))
        b=int(input("Second number: "))
        total = add(a,b)
        print(total)        
    elif opt==2:
        a=int(input("First number: "))
        b=int(input("Second number: "))
        total = substract(a,b)
        print(total)        
    elif opt==3:
        a=int(input("First number: "))
        b=int(input("Second number: "))
        total = multiply(a,b)
        print(total)        
    elif opt==4:
        a=int(input("First number: "))
        b=int(input("Second number: "))
        total = divide(a,b)
        print(total)        
