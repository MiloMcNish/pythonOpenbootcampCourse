import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0,weight=4)
window.columnconfigure(0,weight=4)

username = ttk.Label(window, text="Username: ")
username.grid(column=0,row=0,sticky=tkinter.W,padx=5,pady=5)

username_entry = ttk.Entry(window)
username_entry.grid(column=1,row=0,sticky=tkinter.E,padx=5,pady=5)

password = ttk.Label(window, text="Password: ")
password.grid(column=0,row=1,sticky=tkinter.W,padx=5,pady=5)

password_entry = ttk.Entry(window, show="*")
password_entry.grid(column=1,row=1,sticky=tkinter.E,padx=5,pady=5)

button = ttk.Button(window, text="Login")
button.grid(column=3,row=2,sticky=tkinter.E,padx=5,pady=5)




window.mainloop()