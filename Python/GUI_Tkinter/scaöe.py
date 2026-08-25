from tkinter import *

window = Tk()

def submit():
    print("The temperature is:" + str(scale.get())+ " degress C")

photo = PhotoImage(file=r"C:\Users\LAIBA MEMON\Downloads\fire.png")
hotLabel = Label(image=photo)
hotLabel.pack()

scale = Scale(window,from_= 100,
               to =0,
               length=600,
               orient=VERTICAL,#this is orientation of scale
               font = ("Comic Sans",30),
               tickinterval= 10,
               showvalue=0, #hides current value
               resolution= 5,  #increment of slider
               troughcolor= "blue",
               fg = "red",
               bg= "black", 
               ) #

#scale.set(50) to set ur scale prior u can also set to mid of ur scale
scale.pack()

button = Button(window, text= "submit",command=submit)
button.pack()

window.mainloop()