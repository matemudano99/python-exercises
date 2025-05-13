# HERENCIA -> ej200

class Persona:
    def __init__(self):
      self.name = input("Nombre: ")
      self.age = int(input("Edad: "))
      self.gender = input("Sexo: ")
    
    def imprimir(self):
       print(f"Nombre: {self.name}   Edad: {self.age}   Sexo: {self.gender}")
       
class Empleado(Persona):
    def __init__(self):
      super().__init__()
      self.category=input("Puesto: ")
      self.sueldo=float(input("Sueldo: "))
    
    def imprimir(self):
        super().imprimir()
        print(f"Sueldo: {self.sueldo}  Puesto: {self.category} ")
        
    def paga_impuestos(self):
        if self.sueldo>3000:
            print("Debe pagar impuestos")
        else:
            print("No debe pagar impuestos")
#main

empleado=Empleado()
empleado.imprimir()
empleado.paga_impuestos()