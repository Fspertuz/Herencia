class persona: 
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad = edad
        print(f"hola, mi nombre es {self.nombre}, mi edad es  {self.edad}")
       
class estudiantes(persona):
    def __init__(self,nombre, edad, grado):
        super().__init__ (nombre, edad)
        self.grado = grado
        print(f"mi grado es  {self.grado}")



fabian = estudiantes("fabian", 30, "Quinto grado")
julio = estudiantes("julio", 36, "Cuarto grado")
kevin = estudiantes("kevin", 25, "Tercero")

