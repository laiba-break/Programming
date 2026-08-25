from tkinter import *
from tkinter import filedialog

def openFile():
    file = filedialog.askopenfilename()
    files = open(file, "r")
    print(files.read())
    files.close()

window = Tk()

button = Button(text="Open",command= openFile)
button.pack()


window.mainloop()