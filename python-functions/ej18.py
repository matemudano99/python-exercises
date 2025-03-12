def contar_a(cadena):
    return cadena.lower().count('a')

texto = input("Ingrese un texto: ")
print("La cantidad de 'a' o 'A' es:", contar_a(texto))
