from posixpath import split


paises=[]
ingresados = input("Ingresa una lista de paises separados por coma:")
ordenados = []
ingresados = ingresados.split(", ")
paises = sorted(ingresados)
ordenados=set(paises)
ordenados=sorted(ordenados)
print(ordenados)