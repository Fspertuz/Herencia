class vehiculo: 
    def __init__(self, marca, año):
        self.marca= marca
        self.año = año
        print(f"la marca del vehiculo {self.marca},el año del vehiculo {self.año}")
       
class coche(vehiculo):
    def __init__(self,marca,año, modelo):
        super().__init__ (marca, año)
        self.modelo= modelo
        print(f"el modelo del coche {self.modelo}")



carro1 = coche(" mazda", 2022, "CX-50")
carro2 = coche(" Ford", 2024, "EXPLORE")
carro3 = coche(" KIA", 2012,"PICANTO")

