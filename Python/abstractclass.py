#prevents a user from creating an object of that class
# compels the user to overrif abstract method in a child class
#anstract class is a class which contains one or more abstract methods
#abstract method = a method that has declartion but does not have an implementation
#its like an idea, not real

# we want user to make a car but not use vehicle not parent class lock it
#to do this we will make this an abstract class
#abc class abstract class
from abc import ABC, abstractmethod 
#ABC is a prebuilt class you can inehrit from abstarct way

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("car stop")

class Motorcycle(Vehicle):
    #notice that are overriting the go method in vehicle above
    #this what abstract classes are for 
    #if i where to remove the the function then it would say abstract error
    def go(self):
        print("You drive the motor")

    def stop(self):
        print("motor stop")

vehicle = Vehicle() # assign object
car = Car()
motor = Motorcycle()

vehicle.go()  #doest print anything empty when normal pass
#says error abtract class if u inheirt ABC
car.go()
motor.go()

car.stop()
motor.stop()