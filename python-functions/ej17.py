def retornar_superficie(lado1, lado2):
    return lado1 * lado2

lado1_rect1 = int(input("Ingrese el primer lado del primer rectángulo: "))
lado2_rect1 = int(input("Ingrese el segundo lado del primer rectángulo: "))
lado1_rect2 = int(input("Ingrese el primer lado del segundo rectángulo: "))
lado2_rect2 = int(input("Ingrese el segundo lado del segundo rectángulo: "))

superficie1 = retornar_superficie(lado1_rect1, lado2_rect1)
superficie2 = retornar_superficie(lado1_rect2, lado2_rect2)

if superficie1 > superficie2:
    print("El primer rectángulo tiene mayor superficie.")
else:
    print("El segundo rectángulo tiene mayor superficie.")
