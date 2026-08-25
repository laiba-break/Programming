#higher order function = a function that either 
#1. accepts a function as an argument or 
#2. returns a function. in python function are treated ad function

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(funk): #funk is another # function is argument of func hello 
    text = funk("Hello") #call funk which has argument hello
    print(text) #prints hello

print(loud("laiba"))
print(quiet("AAIMA"))
hello(loud)
hello(quiet)