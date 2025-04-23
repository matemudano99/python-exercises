class Alumnos:
    def __init__(self):
        self.nombres = []
        self.notas = []

    def menu(self):
        opcion = 0
        while opcion != 4:
            print("1- Cargar alumnos")
            print("2- Listas alumnos")
            print("3- Listado de alumnos con notas >= a 7")
            print("4- Finalizar programa")
            opcion = int(input("Ingrese su opcion: "))
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.listar()
            elif opcion == 3:
                self.listarAltas()
            elif opcion == 4:
                print("Saliendo...")
            else:
                print("Elige una opcion valida")

    def cargar(self):
        for i in range(5):
            nombre = input("ingrese el nombre del alumno: ")
            self.nombres.append(nombre)
            notas = int(input("Nota del alumno: "))
            self.notas.append(notas)

    def listar(self):
        for i in range(5):
            print(self.nombres[i], self.notas[i])
        print("")

    def listarAltas(self):
        for i in range(5):
            if self.notas[i] >= 7:
                print(self.nombres[i], self.notas[i])
        print("")


alumnos = Alumnos()
alumnos.menu()
