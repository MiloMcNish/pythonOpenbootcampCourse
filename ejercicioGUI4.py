import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0,weight=4)
window.columnconfigure(1,weight=4)


lista = ['windows','mac','linux','ms dos']
lista_items= tkinter.StringVar(value=lista)

listbox=tkinter.Listbox(window,height=50,width=50, listvariable=lista_items)
listbox.grid(column=0,row=0,sticky=tkinter.W)


window.mainloop()