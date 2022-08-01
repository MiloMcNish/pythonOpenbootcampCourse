import time



def cuantoFalta():
    horaDeInicio = 7
    horaDeSalida = 16
    trabajar = True
    while trabajar == True:
        if int(time.strftime("%H")) >= horaDeInicio:
            print("es hora de trabajar, faltan:", (horaDeSalida - int(time.strftime("%H"))), " Horas para salir")
            trabajar=True
        elif int(time.strftime("%H")) >= horaDeSalida:
            print("se acabó el trabajo, faltan:", (horaDeInicio - int(time.strftime("%H"))),  " Horas para iniciar a trabajar de nuevo" )
            trabajar=False
        return