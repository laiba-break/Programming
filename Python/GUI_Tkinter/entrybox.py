from tkinter import  *

#entry box = textbox that accepts a single line of user input
def submit():
    username=entry.get()
    print("Hello" + username)  #we ask for entry

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

window = Tk()

entry = Entry(window, font =("Arial",50),
              fg= "Green",
              bg="black",show="*") #we creat entry box it takes
#text in arial and has size of 50
#we give our text too by default
entry.pack(side=LEFT) #text will take from left

submit_button= Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)   
# creates button with command submit to take text

delete_button= Button(window,text="delete",command=delete)
delete_button.pack(side=RIGHT)  

backspace_button= Button(window,text="backspace",command=backspace)
backspace_button.pack(side=RIGHT)  


window.mainloop()