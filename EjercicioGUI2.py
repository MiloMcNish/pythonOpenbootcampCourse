import tkinter
import random

window = tkinter.Tk()

window.columnconfigure(0,weight=4)
window.columnconfigure(0,weight=4)


colors = ["purple","red",'blue','yellow','green','gray','cyan','orange']


for x in range(0,30):
    color= random.randint(0,len(colors)-1)
    color2= random.randint(0,len(colors)-1)
    ancho= random.randint(0,30)
    alto= random.randint(0,30)
    label = tkinter.Label(window,text="Hola",padx=ancho, pady=alto, bg=colors[color], fg=colors[color2])
    label.place(x=random.randint(0,500), y=random.randint(0,500))





window.mainloop()