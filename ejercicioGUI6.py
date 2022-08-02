import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0,weight=4)
window.columnconfigure(0,weight=4)

def salir(event):
    print('adios')
    window.quit()
def saludar(event):
    print('Ha hecho click')

def saludar2(event):
    print('Ha hecho doble click')

boton=tkinter.Button(window,text='Presiona')
boton.pack()
boton.bind('<Button-1>', saludar)
boton.bind('<Double-1>', saludar2)
boton2=tkinter.Button(window,text='Salir')

boton2.pack()
boton2.bind('<Button-1>', salir)


window.mainloop()