from operator import truediv
from functools import reduce


lista =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def impar(x):
    if x%2 == 0:
        return False
    else:
        return True
def suma(a,b):
    return a+b
def impares(x):
    imparL =filter(impar,lista)
    print(list(imparL))
    imparL =filter(impar,lista)
    imparL = reduce(suma,imparL)
    
    print(imparL)
    return imparL
    

impares(lista)
