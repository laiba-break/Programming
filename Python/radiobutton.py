#radio button = similiar to checkbox but u can only select one from a group

from tkinter import *

food = ["pizza","hamburger","hotdog"]


def order():
    if (x.get() == 0):
        print("u ordered pizza")
    elif(x.get() == 1):
        print("u ordered hamburger")
    elif(x.get() ==2):
        print("u irdered hotdog")


window= Tk()
#pizzaImage = PhotoImage(file="") u can add photo in exact same waz others
#we add ahmburg and hotdog
#then we make a list of these three images and add to radiobutton 
#image=foodimages[index] and compund allows position to chnage 

x= IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,text=food[index], #adds text to radiobutton
                              variable=x, #groups radiobuttons together if they share the variable x
                              value=index,#assigns each radio button a diff button
                              padx=25,#adds padding on x axis
                              font=("Impact",50),indicatoron= 0,#elimate circle idnicator and sets width of radiobutton
                              width=375,
                              command=order)#set command of rafiobutton to function
    
    radiobutton.pack(anchor=W)

window.mainloop()