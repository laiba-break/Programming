from tkinter import *

def doSth(event):
    print("You Pressed: " + event.keysym )

window = Tk()

window.bind("<q>",doSth) #basically put button #u can get all sorts
#of keys q,key ,etc like if put q and press q it will call func
label = Label(window,font=("comic Sans",100))
label.pack()


window.mainloop()