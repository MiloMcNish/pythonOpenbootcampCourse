def es_primo(numero):
    marca=0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            marca= marca+1
    if marca == 0:
        return True
    else:
        return False     

   

def primos():
    numero = int(input('Escriba un número para saber si es primo o no: '))
    
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == "__main__":
    primos()