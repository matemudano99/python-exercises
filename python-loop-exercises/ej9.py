cantidad = int(input("Dime cuántos números evaluar si son primos: "))

i = 1
while i <= cantidad:
    es_primo = True
    if i < 2:
        es_primo = False
    else:
        j = 2
        while j< i:
            if i % j == 0:
                es_primo = False
                break
            j += 1

    if es_primo:
        print(f"{i} es primo")
    else:
        print(f"{i} no es primo")

    i += 1
