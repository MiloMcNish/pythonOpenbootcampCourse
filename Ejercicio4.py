from math import pi




def areaTri(base, altura):
    area=((base*altura)/2)
    print("El area del triángulo es: " + str(area))
    return
pi=3.14
def areaCir(radio):
    area=pi*(radio**2)
    print("El area del circulo es: " + str(area))

areaCir(2)

areaTri(18,8)