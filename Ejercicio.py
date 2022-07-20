
#Parte A 1.Crear una función con tres parámetros que sean números que se suman entre sí. 2. Llamar a la función en el main y darle valores.

def sumar (a,b,c):
    sumar = a+b+c
    print(f"Hola, la suma de {a} + {b} + {c} es: " +  str(sumar))
sumar(2,3,1) 
sumar(29,-12,350)

print("=========================")
print("===== Bienvenido a ======")
print("=====  tu garage   ======")
print("=========================")

#Parte B 1. Crear una clase coche 2. Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.
#3. Una función que incremente el número de puertas que tiene el coche. 4. Crear un objeto miCoche en el main y añadirle una puerta.
#5. Mostrar el número de puertas que tiene el objeto.


class coche:
    def __init__(self, NumPuertas):
       self.NumPuertas = NumPuertas
       puertasAumentadas = 0


    def aumentarPuertas(self, puertasAumentadas):
        
        self.NumPuertas += puertasAumentadas

miCoche = coche(4)

print("Tu coche tiene: " + str(miCoche.NumPuertas) + " puertas \n")

puertasAumentadas = int(input("Cuantas Puertas va a aumentar?: " +"\n"))

miCoche.aumentarPuertas(puertasAumentadas)

print("\nAhora este es el número de puertas:" + str(miCoche.NumPuertas) )