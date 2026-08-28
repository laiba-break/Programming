#multiple animations
from tkinter import *
from ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,"white")
basketball_ball = Ball(canvas,0,0,50,4,3,"orange")


while True:
    volley_ball.move()
    basketball_ball.move()
    window.update()
    time.sleep(0.01)


window.mainloop()