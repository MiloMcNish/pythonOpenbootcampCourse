class Vehiculo():
    def __init__(self):
        self.Color = None
        self.Ruedas = 4
        self.Puertas = 2

class Coche(Vehiculo):
    def __init__(self):
        super().__init__()
        self.Velocidad = 125
        self.Cilindrada = True 

miCoche = Coche()
print(miCoche.Velocidad)
print(miCoche.Puertas)
print(miCoche.Cilindrada)