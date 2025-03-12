# Calcular el indice de masa corporal
def calcularIMC(pesoKG,alturaM):
    return pesoKG/(alturaM*alturaM)

pesoKG = float(input("Dime el peso en KG: "))
alturaM = float(input("Dime tu altura en metros: "))

print(calcularIMC(pesoKG,alturaM))