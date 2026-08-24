from tkinter import *

def create_window():
    new_window = Toplevel() 
    # toplevel()= new window on top of other windows
    #linked to get other windows
    #bottom closes top doesnt
    #top closes bottom doesnt
    old_window.destroy()

old_window = Tk()


Button(old_window,text = "create new window",command= create_window).pack()


old_window.mainloop()