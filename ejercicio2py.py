#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

x=int(input("ingrese número inicial: "))
y=int(input("Ingrese número final: "))
numImpares=[]
for impares in range(x,y):
    if impares%2 == 1:
        numImpares = numImpares + [str(impares)]
        
print(numImpares)
