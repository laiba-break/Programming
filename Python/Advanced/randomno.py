import random

x = random.randint(1,6)
y = random.random()
print(y)

myList = ["rock","scisscors","paper"]
z = random.choice(myList)
print(z)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","A", "K"]

random.shuffle(cards)

print(cards)
