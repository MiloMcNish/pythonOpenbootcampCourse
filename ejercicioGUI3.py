import tkinter
from tkinter import ttk
from turtle import bgcolor

window = tkinter.Tk()

window.columnconfigure(0,weight=4)
window.columnconfigure(0,weight=4)

frame = ttk.Frame(window)
frame.grid(column=0,row=0)

label=ttk.Label(frame,text="Esto es un label dentro de un frame")
label.grid(column=1, row=1, padx=50, pady=50, sticky=tkinter.W)



frame.mainloop()
window.mainloop()