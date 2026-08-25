#buttons = u click them and they do stuff 

from tkinter import *
count= 0
def click():
    global count
    count = count +1
    print(count)


windows = Tk()

photo= PhotoImage(file=r"C:\Users\LAIBA MEMON\Downloads\fairytail.png")

button =Button(windows,text="Click me",
               command=click,
               font=("Comic Sans",30)
               ,fg= "Green",
               bg = "black",
               activeforeground="Green",
               activebackground="black",
               state= ACTIVE,image= photo,
               compound="top")



button.pack()

windows.mainloop()