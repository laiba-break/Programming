from tkinter import *
#import notebook widget
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) #widget that manages a collection of windows/widgets

tabl = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tabl, text="Tab 1")
notebook.add(tab2, text = "Tab 2")
notebook.pack(expand = True, fill="both") #expand to fill any space not otherwise used
#fill will fill space on x and y axis

Label(tabl, text = " Hello, this is tab1",width=50,height = 25).pack()
Label(tab2, text = " Hello, this is tab2",width=50,height = 25).pack()

window.mainloop()

