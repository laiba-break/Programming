#str.format() = optional method that gives users more control
#when displaying output

animal = "cow"
item = "moon"

print("The " + animal + " jumped over the "+ item)
print("The {} jumped over the {}".format(animal,item))

# these work as placeholder for values

print("The {1} jumped over the {0}".format(animal,item))

text = "the {} jumped over the {}"
print(text.format(animal,item))

name = "bro"
print("Hello, my name is {}".format(name))


number= 3.1449
print("the number pi is {}".format(number))
print("the number pi is {:.3f}".format(number))
