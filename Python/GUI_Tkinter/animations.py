from tkinter import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500
xVelocity = 1
yVelocity = 1

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

photo_image = PhotoImage(file='racecar.png')
photo_image = photo_image.subsample(12,12)
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

image_width = photo_image.width()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>=WIDTH-image_width or coordinates[0]<0):
        xVelocity = -xVelocity
    canvas.move(my_image,xVelocity,0)
   # canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)


window.mainloop()
