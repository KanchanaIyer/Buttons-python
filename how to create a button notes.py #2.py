
import tkinter as tk
import tkinter.messagebox as tkm

def display_info():
    tkm.showinfo('personal info' , 'name\nCs\n3456')

window= tk.Tk()

button1 = tk.Button(window,text='show info!',command=display_info)
button1.pack()


window.mainloop()


"""
import tkinter as tk
import tkinter.messagebox as tkm

def display_info():
    tkm.showinfo('personal info' , 'Bakugo is amazing!!!')

window= tk.Tk()

button1 = tk.Button(window,text='click me!',command=display_info)
button1.pack()


window.mainloop()
"""
