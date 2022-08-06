class Vehiculo():
    def __init__(self,color,puertas,ruedas):
        self.color=None
        self.puertas=4
        self.ruedas=4
    def getPuertas(self):
        return self.puertas
    def getColor(self):
        return self.color
    def getRuedas(self):
        return self.ruedas
coche = Vehiculo('rojo',4,4)
print(coche.color)
def getRuedas():
    return coche.ruedas
