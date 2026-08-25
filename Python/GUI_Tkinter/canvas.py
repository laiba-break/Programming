# canvas = widget that is used to draw grpahs, plots and images in a window

from tkinter import *
window = Tk()

canvas = Canvas(window,height=500, width=500)
#blueLine = canvas.create_line(0,0,500,500,fill="blue",width=5) #creates line
#redLine = canvas.create_line(0,500,500,0,fill="red",width=5)#creates line
#canvas.create_rectangle(50,50,250,250,fill = "purple") #creates filled rect
#points = [250,0,500,0,500]

#canvas.create_polygon(250,0,500,500,0,500,fill="yellow",outline="black",width=5)
#canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,extent=180) #can be color also and arc as style
canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
canvas.create_oval(190,190,310,310,fill="white",width=10)

canvas.pack()




window.mainloop()