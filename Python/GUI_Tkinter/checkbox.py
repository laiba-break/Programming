#check buttons

from tkinter import *
def display():
    if (x.get()==1):
        print("you agree")
    else:
        print("u dont agree")

window= Tk()
photo = PhotoImage(file=r"C:\Users\LAIBA MEMON\Downloads\fairytail.png")
x = BooleanVar() # by default they equal this to x

check_button = Checkbutton(window,
                           text= " I agree to sth"
                           ,variable=x,onvalue= True,
                           offvalue =False,
                           command = display,font=("Arial",20),
                           fg= "Green", bg= "black",activebackground="black",
                           activeforeground="Green",
                            padx=25,pady= 20,image=photo,
                            compound="top") #activebackgroundfg for flashing

check_button.pack()

window.mainloop()