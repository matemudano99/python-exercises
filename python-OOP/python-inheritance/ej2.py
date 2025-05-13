class Operacion:
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.resultado = 0

    def cargar(self):
        self.valor1 = int(input("Primer valor: "))
        self.valor2 = int(input("Ingrese segundo valor: "))

    def mostrarResultado(self):
        print(f"Resultado: {self.resultado}")

    def operar(self):
        pass


class Suma(Operacion):
    
    def operar(self):
        self.resultado = self.valor1 + self.valor2


class Resta(Operacion):
    def operar(self):
        self.resultado = self.valor1 - self.valor2

class Multiplicacion(Operacion):
    def operar(self):
        self.resultado = self.valor1 * self.valor2

class Division(Operacion):
    def operar(self):
        self.resultado = self.valor1 / self.valor2 if self.valor2 !=0 else "ERROR: No se puede dividir por 0"

print("SUMA")
suma1=Suma()
suma1.cargar()
suma1.operar()
suma1.mostrarResultado()
print("RESTA")
resta1=Resta()
resta1.cargar()
resta1.operar()
resta1.mostrarResultado()
print("MULTIPLICACION")
multiplicacion1=Multiplicacion()
multiplicacion1.cargar()
multiplicacion1.operar()
multiplicacion1.mostrarResultado()
print("DIVISION")
division1=Division()
division1.cargar()
division1.operar()
division1.mostrarResultado()