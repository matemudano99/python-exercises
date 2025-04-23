class Empleado:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleado: ")
        self.sueldo = float(input("Ingrese su sueldo: "))

    def __str__(self):
        return f"Empleado: {self.nombre}, Sueldo: {self.sueldo}"

    def paga_impuestos(self):
        if self.sueldo > 3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")


empleado1 = Empleado()
print(empleado1)
empleado1.paga_impuestos()
