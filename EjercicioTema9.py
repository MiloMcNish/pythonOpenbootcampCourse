#1. Crea una clase Persona con las siguientes variables: La edad El nombre El teléfono
class persona:
    
    def __init__(self,edad,nombre,telefono):
        self.edad = edad
        self.nombre = nombre
        self.telefono = telefono
    
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
#2. Una vez creada la clase, crea una nueva clase Cliente que herede de Persona, esta nueva clase tendrá la variable credito solo para esa clase.
class cliente(persona):

    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    def __init__(self, credito):
        self.credito = credito
        
    def mostrarInfo(self):
        info = print("Nombre: " + str(self.nombre) + " Edad: " + str(self.edad) + " Telefono: " + str(self.telefono)+ " Credito: $" + str(self.credito))
        return print(info)

    def modCredito(self, nuevoCredito):
        self.credito = nuevoCredito
        return self.credito

class trabajador(cliente):

    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    def __init__(self, salario):
        self.salario = salario
    def mostrarInfo(self):
        info = print("Nombre: " + str(self.nombre) + " Edad: " + str(self.edad) + " Telefono: " + str(self.telefono)+ " Credito: $" + str(self.credito) + " Salario: $" + str(self.salario))
        return print(info)
    def modSalario(self, nuevoSalario):
        self.nuevoSalario = nuevoSalario
        return self.nuevoSalario

persona1 = persona(12,"Camilo",3116658609)

print(persona1.mostrarInfo())
#3.Crea ahora un objeto de la clase Cliente que debe tener como propiedades la edad, el telefono, el nombre y el credito, tienes que darles valor y mostrarlas por pantalla.
PersonaCliente = cliente(450)
cliente.modEdad(PersonaCliente,15)
cliente.modNombre(PersonaCliente,"Arturo")
cliente.modTelefono(PersonaCliente,3153510106)

print(PersonaCliente.mostrarInfo())
#4.Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de Persona, y con una variable salario que solo tenga la clase Trabajador.
PersonaClienteTrabajador = trabajador(1500000)
trabajador.modEdad(PersonaClienteTrabajador,28)
trabajador.modNombre(PersonaClienteTrabajador,"Camilo Arturo")
trabajador.modTelefono(PersonaClienteTrabajador,3213398659)
trabajador.modCredito(PersonaClienteTrabajador,950)

print(PersonaClienteTrabajador.mostrarInfo())