#listbox = a listing of seletable text items within its own container

from tkinter import *

def submit():
   food = []
   for index in listbox.curselection():
       food.insert(index,listbox.get(index))
   print(" u have ordered:")
   # print(listbox.get(listbox.curselection())) this is for fine for one
   for index in food:
       print(index)

def add():
    for index in reversed(listbox.curselection()): #normal wont work we reserve
        list.delete(index)

    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

window = Tk()
listbox = Listbox(window,
                  bg = "green",
                  font = ("Comic Sans", 30),
                  width= 12,
                  selectmode= MULTIPLE        
)
listbox.pack()

listbox.insert(1,"Pizza")
listbox.insert(2,"Pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"drinks")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,text="submit",command=submit)
submitButton.pack()

addButton = Button(window,text="add",command=add)
addButton.pack()

deleteButton = Button(window,text="delete",command=delete)
deleteButton.pack()
#function not set up to delete multiple items

window.mainloop()