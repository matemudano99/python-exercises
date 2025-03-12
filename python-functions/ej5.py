# tabla de multiplicar

def multiply(a):
    for i in range(1,10):
        print(f"{a}*{i}",a*i)


while(True):
    multiply(int(input("TABLA DE MULTIPLICAR\nDime un numero:")))