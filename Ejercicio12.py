from operator import truediv


lista =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def impar(x):
    if x%2 == 0:
        return False
    else:
        return True

def impares(x):
    imparL =filter(impar,lista)
    return imparL

print(list(impares(lista)))
