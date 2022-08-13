#How to create another button to terminate the program/window!!!

import tkinter as tk
import tkinter.messagebox as tkm

def display_info():
    tkm.showinfo('personal info' , 'name\nCs\n3456')

window= tk.Tk()

button1 = tk.Button(window,text='show info!',command=display_info)
button1.pack()


button2=tk.Button(window,text='quit',command=window.destroy)
button2.pack()

window.mainloop()
