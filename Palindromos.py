def palindromo(palabraLu):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_inv = palabra[::-1] 
    if palabra == palabra_inv:
        return True
    else:
        return False    


def palindroproject():

    
    palabra = input("Ingrese una palabra: ")
    es_palindromo = palindromo(palabra)

    if es_palindromo == True:
        print('La palabra es un palíndromo')
    else:
        print('La palabra no es un palíndromo')




if __name__ == '__main__':
    palindroproject()