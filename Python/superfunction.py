# super()=function is used to give access to the methods of a parent clas
#returns sa temporary object of a parent class when used

class Rectangle:

    def __init__(self,length, width):
        self.length= length
        self.width = width
#see this has length and width below they also have it

class Square(Rectangle):
    def __init__(self,length, width):
          # self.lenght= length
          # self.width = width
          # we basicaly want to avoide writing this two again
          super().__init__(length,width)
    def area(self):
         return self.length*self.width

class Cube(Rectangle):
    def __init__(self,length,width, height):
          super().__init__(length,width)
          self.height = height

    def volume(self):
     return self.length*self.width*self.height 

square = Square(3,3).area()
cube = Cube(2,3,4).volume()
print(square)
print(cube)

