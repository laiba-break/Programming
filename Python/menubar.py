from tkinter import *

def openfile():
    print("File has been opened")

def savefile():
    print("File has been saved")

def quit():
    print("File has been exited")

def cut():
    print("u cut sth")

def copy():
    print("u copy sth")

def paste():
    print("u pasted")


window = Tk()

menubar = Menu(window)
window.config(menu = menubar)

fileMenu = Menu(menubar,tearoff=0,font=("Comic Sans",15))
menubar.add_cascade(label="File",menu=fileMenu)
#we are creating open,file and exit
fileMenu.add_command(label = " Open", command=openfile)
fileMenu.add_command(label = " Save",command = savefile)
#seperator will seperate diff commands from each other
fileMenu.add_separator()
fileMenu.add_command(label = " Exit",command=quit)

editMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "Edit", menu= editMenu)
editMenu.add_command(label= "Cut", command = cut)
editMenu.add_command(label = "Copy" , command = copy)
editMenu.add_command(label = "Paste" , command = paste)

window.mainloop()
