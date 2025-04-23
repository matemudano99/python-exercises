class Agenda:
    def __init__(self):
        self.nombre = []
        self.telefono = []
        self.mail = []

    def menu(self):
        opcion = 0
        while opcion != 5:
            int(input(
                "1.Cargar contacto\n2.Listar contactos\n3.Buscar contacto\n4.Modificar telefono/mail del contacto\n5.Finalizar programa\n"
            ))
            if opcion==1:
                self.cargar()
            elif opcion==2:
                self.listar()
            elif opcion==3:
                self.buscar()
            elif opcion==4:
                self.modificar()
            elif opcion==5:
                print("Saliendo...")
    def cargar(self):
        for i in range(5):
            self.nombre.append(input("Introduce el nombre del contacto: "))
            self.telefono.append(input("Introduce el numero de telefono: "))
            self.mail.append(input("Introduce el email del contacto: "))
            

# MAIN
agenda = Agenda()
agenda.menu()