class Persona:

    def __init__(self, name, age, country, city):
        self.name = name
        self.age = age
        self.country = country
        self.city = city

    def __str__(self):
        return f"{self.name,self.age,self.country,self.city}"


persona1 = Persona("Juan", 20, "Argentina", "Buenos Aires")
print(persona1)
