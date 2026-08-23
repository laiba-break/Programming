#gui windows
#graphical user interface
from tkinter import *

#widgets = GUI elements such as buttons, textboxes,labels, images
#windows = serves as a container, to hold or contain these widgets

window = Tk() #insitatiate an instance of a window
window.geometry("420x420")
window.title("Laiba Memon First GUI Program")
icon = PhotoImage(file=r"C:\Users\LAIBA MEMON\Downloads\fairytail.png")
window.iconphoto(True,icon)     
window.config(background="black")           

window.mainloop() #this will place window on computer screen,listen for events

