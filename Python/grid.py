#grid geomtry manager in python
#grid() = geomtry manager that organizes widgets in a table like structure in
# in a parent like structure
#like we make row and column show where we want widgets to be in
from tkinter import *
window = Tk()
titleLabel = Label(window, text = "Enter ur info:", font = ("Arial",25)).grid(row=0,column=0,columnspan=2)
firstNameLabel = Label(window,text = "First Name: ",width=20, bg= "red",
                       ).grid(row=1, column=0)
firstNameLabel = Entry(window).grid(row =1, column =1)

lastNameLabel = Label(window,text = "Last Name: ",width=30,
                      ).grid(row=2, column=0)
lastNameLabel = Entry(window).grid(row =2, column =1)


EmailLabel = Label(window,text = "Email:", bg= "light blue",
                   ).grid(row=3,column=0)
EmailLabel = Entry(window).grid(row =3, column =1)

submitButton = Button(window,text = "Submit").grid(row=3,column=0, columnspan=2)


window.mainloop()