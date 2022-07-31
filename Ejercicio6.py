class Alumno():
    def __init__(self, nombre, nota) -> None:
        self.nombre = nombre
        self.nota = nota

    def showNota(self):
        
        if self.nota >= 3:
            
            print("La nota de ", self.nombre, " es ", self.nota, " Aprobado")
        elif self.nota < 3:
            print(print("La nota de ", self.nombre, " es ", self.nota, " Reprobado"))
        

alumno1 = Alumno("Camilo", 2)
alumno2 = Alumno("Arturo", 3)
alumno3 = Alumno("Carlos", 5)
print(alumno1.showNota())
print(alumno2.showNota())
print(alumno3.showNota())