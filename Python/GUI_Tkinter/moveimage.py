from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(), y= label.winfo_y()-1)

def move_down(event):
    label.place(x=label.winfo_x(), y= label.winfo_y()+10)

def move_left(event):
    label.place(x=label.winfo_x()-10, y= label.winfo_y())

def move_right(event):
    label.place(x=label.winfo_x()+10, y= label.winfo_y())

window = Tk()
window.geometry("500x500")

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

myimage = PhotoImage(file= r"C:\Users\LAIBA MEMON\Downloads\SKills_Laiba\Programming\Python\GUI_Tkinter\racecar.png")
myimage = myimage.subsample(12,12)
label= Label(window,image=myimage,bg="red")
label.place(x=0,y=0)

window.mainloop()


#canvas = Canvas(window,width=50,height=50)
#canvas.pack()
#photoimage same way
#myimage = canvas.create_image(0,0,image=Photoimage,anchor=NW)
#then to move image we use key bindings
# you use event and functions
#like to move up and down as above
#define and use canvas.move(myimage,0,-10) and so on

