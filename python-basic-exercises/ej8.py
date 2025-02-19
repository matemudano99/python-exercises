nEmpleados = int(input("Ingrese la cantidad de empleados"))
i=1
contadorMedio = 0
contadorMayor = 0
while i<=nEmpleados:
    sueldoEmpleado = int(input(f"Ingrese el sueldo del empleado {i}"))
    if(sueldoEmpleado>=100 and sueldoEmpleado<=300):
        contadorMedio +=1
    else:
        contadorMayor +=1
    i+=1
print(f"Hay {contadorMedio} empleados con un sueldo entre 100 y 300, y {contadorMayor} empleados con un sueldo mayor a 300")
