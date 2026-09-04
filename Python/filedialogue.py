from tkinter import *
from tkinter import filedialog

def openFile():
    file = filedialog.askopenfilename() #can also pass file path in argument to ppen directly
#file = filedialog.askopenfilename( initaldri ="",title="open file ok",filetypes="")
   # u can also open all files and open them
    files = open(file, "r")
    print(files.read())
    files.close()  #this gets a file button to open a file and read


window = Tk()

button = Button(text="Open",command= openFile)
button.pack()


window.mainloop()