#frames = a rectangular container to group and hold widgets 

from tkinter import *

window = Tk()

frame = Frame(window,bg= "pink", relief=SUNKEN)
frame.pack(side= BOTTOM) #place can also be used
# x and y used for positoning


button = Button(frame,text ="W",font = ("Consoles",25),width=3).pack(side=TOP)
#button.pack()
button = Button(frame,text ="A",font = ("Consoles",25),width=3).pack(side=LEFT)
button = Button(frame,text ="S",font = ("Consoles",25),width=3).pack(side=LEFT)
button = Button(frame,text ="D",font = ("Consoles",25),width=3).pack(side=LEFT)

window.mainloop()