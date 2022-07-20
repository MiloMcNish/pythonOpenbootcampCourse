#Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0 :
print("\nCrear IF: \n")
numeroIf = 23

if numeroIf >= 0:
    print("El número es positivo")
elif numeroIf == 0:
    print("El número es 0")
elif numeroIf <= 0:
    print("El número es negativo")

#Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3, el bloque de código que tendrá #el bucle deberá: 1-Incrementar el valor de la variable en uno cada vez que se ejecute. 2-Mostrarlo por pantalla cada vez que se ejecute : 
numeroWhile = 0
print("\nCrear Bucle While: \n")
while numeroWhile <= 3:
    numeroWhile += 1
    print(numeroWhile)

#Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez :
print("\nCrear Bucle Do While: \n")
numeroWhile = 0
while numeroWhile <= 3:
    numeroWhile += 1
    print(numeroWhile)
    break

#Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0 y su condición será que la variable sea igual o menor que 3, se irá incrementando en 1 su valor cada vez que se ejecute y deberá mostrarse por pantalla.

numeroFor = 1
print("\nCrear Bucle For: \n")
for numeroFor in range(0,4):
    numeroFor += 1
    print(numeroFor)

#Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones del año. Dependiendo del valor de la variable estacion se deberá mandar un mensaje por consola informando de la estación en la que está. También habrá que poner un default para cuando el valor de la variable no sea una estación.
print("\nCrear Bucle Switch: \n")
Estación = "Verano"

if Estación == "Verano":
    print("Estamos en Verano")
elif Estación == "Primavera":
    print("Estamos en Primavera")
elif Estación == "Otoño":
    print("Estamos en Otoño")
elif Estación == "Invierno":
    print("Estamos en Invierno")

