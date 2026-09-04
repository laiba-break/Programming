from tkinter import *

def doSth(event):
    print("You did a good thing:"+ str(event.x)+ "," +str(event.y))

window= Tk()


#window.bind("<Button-1>",doSth)  #left mmouse 
#window.bind("<Button-2>",doSth)  #scroll wheel
#window.bind("<Button-3>",doSth) #right mouse click
# window.bind("<ButtonRelease>",doSth)
# window.bind("<Enter>",doSth) #right mouse click
# window.bind("<Leave>",doSth)
# window.bind("<Motion>",doSth) 


window.mainloop()