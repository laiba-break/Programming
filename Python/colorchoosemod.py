from tkinter import *
from tkinter import colorchooser #submodule

def click():
    color = colorchooser.askcolor()
    print(color)
    colorHex = color[1]
    print(colorHex)
    window.config(bg = colorHex) #change bg color
    #can also be written in one line of code
    #window.config(--)

window = Tk()

window.geometry("420x420")
button = Button(text="click me", command=click)
button.pack()


window.mainloop()