
def sumar (a,b,c):
    sumar = a+b+c
    print(f"Hola, la suma de {a} + {b} + {c} es: " +  str(sumar))
sumar(2,3,1) 
sumar(29,-12,350)

print("=========================")
print("===== Bienvenido a ======")
print("=====  tu garage   ======")
print("=========================")




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