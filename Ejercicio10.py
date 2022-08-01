


f=open("ficheroVehiculo.py","w")
f.close
def escribirFichero(fichero):
    f=open(fichero,"w")
    f.writelines("")
    f.writelines("class Vehiculo():\n")
    
    f.writelines("    def __init__(self,color,puertas,ruedas):\n")
    f.writelines("        self.color=None\n")
    f.writelines("        self.puertas=4\n")
    f.writelines("        self.ruedas=4\n")
    f.writelines("    def getPuertas(self):\n")
    f.writelines("        return self.puertas\n")
    f.writelines("    def getColor(self):\n")
    f.writelines("        return self.color\n")
    f.writelines("    def getRuedas(self):\n")
    f.writelines("        return self.ruedas\n")
    f.writelines("coche = Vehiculo('rojo',4,4)\n")
    f.writelines("print(coche.color)\n")
    f.writelines("def getRuedas():\n")
    f.writelines("    return coche.ruedas\n")
    f.writelines("")
    f.writelines("")
    f.writelines("")
    f.writelines("")
    f.writelines("")
    
    f.close



escribirFichero("ficheroVehiculo.py")


import pickle
from ficheroVehiculo import *

print(coche.ruedas)

f = open("Vehiculo_objeto","wb")
pickle.dumps(coche,f)

pickle.load(f)
f.close()

f.seek(0)
e=pickle.load(f)

print(e)
e.close()
