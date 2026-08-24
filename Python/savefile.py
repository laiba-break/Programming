from tkinter import *
from tkinter import filedialog

def saveFile():
    file= filedialog.asksaveasfile(initialdir= r"C:\Users\LAIBA MEMON\Downloads\SKills_Laiba\Python",
        defaultextension= ".txt",
                                   filetypes= [("Text file", ".txt"),
                                               ("HTML File", ".html"),
                                               ("ALL files", "*")])

   #filetext = str(text.get(1.0,END))
    filetext = input("text i guess")
    file.write(filetext)
    file.close()


window= Tk()

button =  Button(text="save", command=saveFile)
button.pack()
text = Text(window)
text.pack()


window.mainloop()