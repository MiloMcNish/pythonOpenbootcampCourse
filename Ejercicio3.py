#1.Crear clase Persona.

class persona:
    #2.Crear variables las privadas edad, nombre y telefono de la clase Persona.
    def __init__(self,edad,nombre,telefono):
        self.edad = edad
        self.nombre = nombre
        self.telefono = telefono
    #3.Crear gets y sets de cada propiedad.
    def mostrarInfo(self):
        info = print("Nombre: " + str(self.nombre) + " Edad: " + str(self.edad) + " Telefono: " + str(self.telefono))
        return print(info)
    
    def mostrarEdad(self):
        return self.edad
    def mostrarNombre(self):
        return self.nombre
    def mostrarTelefono(self):
        return self.telefono

    def modEdad(self, nuevaEdad):
        self.edad = nuevaEdad
        return self.edad
    def modNombre(self, nuevoNombre):
        self.nombre = nuevoNombre
        return self.nombre
    def modTelefono(self, nuevoTelefono):
        self.telefono = nuevoTelefono
        return self.telefono

#4.Crear un objeto persona en el main.
persona1 = persona(12,"Camilo",3116658609)

#5.Utiliza los gets y sets para darle valores a las propiedades edad, nombre y telefono, por último muéstralas por consola.
print(persona.mostrarInfo(persona1))
print(persona.mostrarEdad(persona1))
print(persona.modEdad(persona1,45))
print(persona.mostrarNombre(persona1))
print(persona.modNombre(persona1,"Arturo"))
print(persona.mostrarTelefono(persona1))
print(persona.modTelefono(persona1,3153510106))
