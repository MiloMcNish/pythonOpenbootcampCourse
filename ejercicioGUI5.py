import tkinter
from tkinter import N, W, Variable, ttk

window = tkinter.Tk()

def reset():
    seleccionado.set(None)
    seleccionado2.set(None)

window.columnconfigure(0,weight=4)
window.columnconfigure(1,weight=4)
seleccionado=tkinter.StringVar()
seleccionado2=tkinter.StringVar()
seleccionado.set(None)
r1=tkinter.Radiobutton(window,text='sí', value='1',variable=seleccionado)
r2=tkinter.Radiobutton(window,text='no', value='2',variable=seleccionado)
r3=tkinter.Radiobutton(window,text='tal vez', value='3',variable=seleccionado)

r4=tkinter.Button(window,text='reiniciar', command=reset)
r4.grid(column=2,row=3,padx=5,pady=5)

checkbox=ttk.Checkbutton(window,text='acepto', variable=seleccionado2)

r1.grid(column=0,row=1,padx=5,pady=5)
r2.grid(column=0,row=2,padx=5,pady=5)
r3.grid(column=0,row=3,padx=5,pady=5)
checkbox.grid(column=0,row=4,padx=5,pady=5)


window.mainloop()