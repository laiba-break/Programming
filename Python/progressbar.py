from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB= 100
    download = 0
    speed = 1
    taks = 10
    x = 0 # we can even show in GB downloading 
    # we input this in string 
    # we can adjust the speed too
    while (x<taks):
         time.sleep(1)
         bar["value"] += 10
         x+=1
         percent.set(str((x/taks) *100)+"%")
         text.set(str(x)+"/" + str(taks))
         window.update_idletasks()
    

window = Tk()

percent = StringVar()
text= StringVar()
bar = Progressbar(window, orient= HORIZONTAL,length=300)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()

button = Button(window,text= "download", command=start).pack()

window.mainloop()
