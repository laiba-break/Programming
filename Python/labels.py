#labels  = an area widhet that holds text and/or an image within a window 
from tkinter import *
window = Tk()

photo = PhotoImage(file=r"C:\Users\LAIBA MEMON\Downloads\fairytail.png")

label = Label(window,text= "Hello World",
              font=("Arial",40,"bold"),
              fg="green",
             bg="black", relief = SUNKEN,
               bd=10, padx= 20, pady=20,
               image= photo,compound = "top")
#label.pack() this puts text in center

label.place(x=0,y=0) #to give position we use place
label.pack()


window.mainloop()





