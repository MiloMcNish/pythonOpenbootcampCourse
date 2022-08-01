def crearFicheroTxt():
    f=open("segundoFichero.txt", "w")
    f.write("Aqui escribo desde el primer fichero")
    f.close

f=open("primerFichero.py","w")
f.close
def escribirEnTxt(fichero):
    f=open(fichero,"w")
    f.writelines("import Ejercicio9\n")
    f.writelines("Ejercicio9.crearFicheroTxt()")
    crearFicheroTxt()
    f.close

escribirEnTxt("primerFichero.py")

