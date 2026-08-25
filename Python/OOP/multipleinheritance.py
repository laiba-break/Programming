# multiple inheritance =when a child class is derived from more than one parent class

class Prey:
    def flee(self):
        print("flee")

class Predator:

    def hunt(self):
        print("hunt")

class Rabbit(Prey):
    pass

class Hawak(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit()
hawk = Hawak()
fish = Fish()

fish.flee()
fish.hunt()
