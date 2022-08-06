import random
from re import A

def adivina_numero_comp(x):

    limite_superior = x
    limite_inferior = 1

    respuesta=""
    
    while respuesta != "c":
        
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior,limite_superior)
        else:
            prediccion = limite_inferior

        respuesta = input(f'He predecido el número: {prediccion}, si el número es muy alto escriba A, si el número es muy bajo escriba B, si la respuesta es correcta escriba C: ').lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f"He adivinado el número, es: {prediccion}")


adivina_numero_comp(10)
