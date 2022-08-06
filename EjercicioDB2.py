import sqlite3


def main():
    ingresar_alumno(1, 'Camilo', 'McNish')
    ingresar_alumno(2, 'Arnoldo', 'Iguaran')
    ingresar_alumno(3, 'Bruno', 'Mars')
    ingresar_alumno(4, 'Lorena', 'Sierra')
    ingresar_alumno(5, 'David', 'Razero')
    ingresar_alumno(6, 'Beto', 'Cuevas')
    ingresar_alumno(7, 'Julio', 'Navas')
    ingresar_alumno(8, 'Andres', 'Ferreira')

    buscar_alumno()
    
    
def ingresar_alumno(id, nombre, apellido):
    conn=sqlite3.connect("Alumnos.db")
    cursor =conn.cursor()

    query = f'INSERT INTO Alumnos(id, nombre, apellido) VALUES({id},"{nombre}","{apellido}")'
    print(cursor.execute(query))
    
    

    conn.commit()
    cursor.close()
    conn.close()

def buscar_alumno():
    conn = sqlite3.connect("Alumnos.db")
    cursor = conn.cursor()

    nombre = input("Ingrese un nombre: ")

    name=cursor.execute(f'SELECT nombre, apellido FROM Alumnos WHERE nombre="{nombre}"')
    
    for nom in name:
        print(nom)

    cursor.close()
    conn.close()



if __name__ == "__main__":
    main()