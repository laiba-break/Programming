#multi level inheritance = when a derived (child) class inherits another derived(child) class

# parent 
class Organism:
    alive = True


#child
class Animal(Organism):
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("dog barks")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()
