class Car:
    def __init__(self,make,model,year,color):  #this is an inbuilt function that is used
       #when isnitalizing a class always it used to assign values 
       #without this u would manually need to add names
       self.make = make
       self.model = model
       self.year= year
       self.color = color 

    def drive(self): #a function we def for driving
        print("This" + self.model + "is driving")

    def stop(self):  # function we def for stopping
        print("This" + self.model + "is stopped")

    #we will call all this in our main file