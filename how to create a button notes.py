import tkinter as tk
import tkinter.messagebox as tkm

def display_info():
    tkm.showinfo('response' , 'thank you for clicking')

window= tk.Tk()

button1 = tk.Button(window,text='click me!',command=display_info)
button1.pack()


window.mainloop()


