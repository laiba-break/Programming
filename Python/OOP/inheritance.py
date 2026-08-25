#claases can inherit everything so objects inehrit from classes
#basically like gentics 

class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("Bro run")
    pass

class Fish(Animal):
    def fish(self):
        print("swim bro")
    pass

class Hawk(Animal):
    def fly(self):
        print("fly")
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# the rabbit has inerhited the animal class so we dont need to copy
print(rabbit.alive)
fish.eat()
hawk.sleep()
rabbit.run()
hawk.fly()
