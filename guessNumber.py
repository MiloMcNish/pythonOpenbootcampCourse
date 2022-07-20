import random


def guessNumber (x):

    print("=======================")
    print(" ¡Bienvenido al juego! ")
    print("=======================")
    print("Tú meta es adivinar un número generado por la computadora")

    predicción = 0

    numero_aleatorio = random.randint(1,x)

    while predicción != numero_aleatorio:
        predicción = int(input(f"Ingresa un número entre el 1 y {x}: "))

        if predicción <= numero_aleatorio:
            print("Intenta de nuevo, el número es mayor")
        elif predicción >= numero_aleatorio:
            print("Intenta de nuevo, el número es menor")    
    print(f"Felicitaciones, has adivinado el número {predicción} correctamente")
    
guessNumber(20)        
