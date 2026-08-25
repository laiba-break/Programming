#duck typing = concept where the cöass of an objectis less important that 
#the methods and attrbutes that that class type might have
#class type is not checked if min methods/attributes are present 
#if it walks like a duck quacks like a duckthen it must be a duck

class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")

class Chicken:

  # def walk(self):
   #    print("This chicken is waiting")

    def talk(self):
        print("This is chicken is clucking")

class Person:

    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("you caught it")

duck = Duck()
person = Person()
chicken = Chicken()

person.catch(chicken)
