class Operacion:
    def __init__(self):
        self.valor1 = int(input("Primer valor: "))
        self.valor2 = int(input("Segundo valor: "))
        self.sumar()
        self.restar()
        self.multiplicacion()
        self.division()
        self.automultiplicacion()
        self.autopotencia()

    def sumar(self):
        suma = self.valor1 + self.valor2
        print("La suma es:", suma)

    def restar(self):
        resta = self.valor1 - self.valor2
        print("La resta es:", resta)

    def multiplicacion(self):
        multiplicacion = self.valor1 * self.valor2
        print("La multiplicación es:", multiplicacion)

    def division(self):
        if self.valor2 != 0:
            division = self.valor1 / self.valor2
            print("La división es:", division)
        else:
            print("¡Error! No se puede dividir por cero.")

    def automultiplicacion(self):
        automultiplicacion = self.valor1 * self.valor1
        print(f"La automultiplicación del primer valor ({self.valor1}) es:", automultiplicacion)

    def autopotencia(self):
        autopotencia = self.valor1 ** self.valor1
        print(f"La autopotencia del primer valor ({self.valor1}) es:", autopotencia)

# Main
op1 = Operacion()