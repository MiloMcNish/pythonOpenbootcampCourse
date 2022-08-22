import random

def genPass():
    caps = ['A','B','C','D','E']
    mins = ['a','b','c','d','e']
    num = ['1','2','3','4','5']
    sym = ['#','!','$','%','&']
    chars = caps + mins + num + sym 
    contrasena = []

    for i in range(15):
        randomchar = random.choice(chars)
        contrasena.append(randomchar)
    contrasena = ''.join(contrasena)
    return contrasena

def generador():
    contrasena = genPass()
    print("Tu nueva contraseña es: " + str(contrasena))




if __name__ == '__main__':
    generador()