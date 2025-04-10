class animal: 
    def __init__(self, nombre, especie):
        self.nombre= nombre
        self.especie = especie
        print(f"su  nombre es {self.nombre}, su especie es   {self.especie}")
       
class perro(animal):
    def __init__(self,nombre, especie, raza):
        super().__init__ (nombre, especie)
        self.raza = raza
        print(f"su raza es {self.raza}")



kenia = perro("kenia", "mamifero", "labrador")
betove = perro("betove", "mamifero", "Chau chau")
sultan = perro("sultan", "mamifero","pastor aleman")

